import sys, os
sys.path.append(os.path.dirname(__file__) + '/lib')

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import json

from module import Module
from converter import Converter
from md import Renderer

class Splunk(Module):
    def __init__(self, proto, host, port):
        self.baseurl = proto + '://' + host + ':' + str(port)
        self.conv = Converter()
        self.render = Renderer()
    
    def login(self, user, pw):
        headers = {}
        data = {'username':user, 'password':pw}
        resp = requests.post(self.baseurl + '/services/auth/login?output_mode=json',
                            headers=headers, data=data, verify=False)
        if (resp.status_code == 200):
            resp = json.loads(resp.text)
            self.sessionkey = resp['sessionKey']

    def query(self, service, data = {}, method = 'POST'):
        headers = {'Authorization': 'Bearer ' + self.sessionkey}
        data['output_mode'] = 'json'
        if 'POST' == method:
            resp = requests.post(self.baseurl + service,
                            headers=headers, data=data, verify=False)
        else:
            resp = requests.get(self.baseurl + service,
                            headers=headers, data=data, verify=False)
        return resp

    def search(self, search):
        resp = self.query('/services/search/jobs/export', {'search': search})
        ret = []
        for row in resp.iter_lines():
            _row = json.loads(row)
            ret.append(_row['result'])
            if 'lastrow' in _row and _row['lastrow']:
                break
        return ret
    
    def indexes(self):
        resp = self.query(service='/servicesNS/-/-/data/indexes?count=0', method='GET')
        ret = json.loads(resp.text)
        indexes = ret['entry']
        table = []
        for index in indexes:
            row = {}
            row['Name'] = index['name']
            row['Type'] = index['content']['datatype']
            row['App'] = index['acl']['app']
            row['Current Size'] = self.conv.mbs(index['content']['currentDBSizeMB'])
            row['Max Size'] = self.conv.mbs(index['content']['maxTotalDataSizeMB'])
            row['Event Count'] = index['content']['totalEventCount']
            row['Earliest Event'] = index['content']['minTime']
            row['Latest Event'] = index['content']['maxTime']
            row['Home Path'] = index['content']['homePath']
            row['Cold Path'] = index['content']['coldPath']
            row['Frozen Path'] = index['content']['frozenPath'] if 'frozenPath' in index['content'] else 'N/A'
            row['Frozen Time Period'] = self.conv.timeperiod(index['content']['frozenTimePeriodInSecs'])
            table.append(row)
        return table
    
    def serverinfo(self):
        resp = self.query(service='/services/server/info', method='GET')
        ret = json.loads(resp.text)
        servers = ret['entry']
        table = []
        for server in servers:
            row = {}
            row['Machine'] = server['content']['host']
            row['Splunk Version'] = server['content']['product_type'] + ' v' + server['content']['version'] 
            row['CPU Cores (Physical / Virutal)'] = str(server['content']['numberOfCores']) + ' / ' + str(server['content']['numberOfVirtualCores'])
            row['Physical Memory Capacity'] = self.conv.mbs(server['content']['physicalMemoryMB'])
            row['Operating System'] = server['content']['os_name'] + ' ' + server['content']['os_version']
            row['CPU Arch'] = server['content']['cpu_arch']
            table.append(row)
        return table

    def licenseinfo(self):
        resp = self.query(service='/services/licenser/licenses', method='GET')
        ret = json.loads(resp.text)
        licenses = ret['entry']
        table = []
        for license in licenses:
            row = {}
            row['License'] = license['content']['label']
            row['Quota'] = self.conv.bytes(license['content']['quota'])
            table.append(row)
        return table

    def licensepoolinfo(self):
        resp = self.query(service='/services/licenser/pools', method='GET')
        ret = json.loads(resp.text)
        pools = ret['entry']
        table = []
        for pool in pools:
            row = {}
            row['License Pool'] = pool['name']
            row['Quota'] = self.conv.bytes(pool['content']['quota'])
            table.append(row)
        return table
    
    def apps(self):
        resp = self.query(service='/servicesNS/-/-/apps/local?count=0', method='GET')
        ret = json.loads(resp.text)
        apps = ret['entry']
        table = []
        for app in apps:
            row = {}
            row['App'] = app['content']['label']
            #row['Description'] = app['content']['description'] if 'description' in app['content'] else 'N/A'
            row['Name'] = app['name']
            row['Author'] = app['content']['author'] if 'author' in app['content'] else 'N/A'
            row['Version'] = app['content']['version'] if 'version' in app['content'] else 'N/A'
            row['Build'] = app['content']['build'] if 'build' in app['content'] else 'N/A'
            row['State'] = self.conv.state(app['content']['disabled'])
            table.append(row)
        return table

    def users(self):
        resp = self.query(service='/servicesNS/-/-/authentication/users?count=0', method='GET')
        ret = json.loads(resp.text)
        users = ret['entry']
        table = []
        for user in users:
            row = {}
            row['Name'] = user['name']
            row['Full Name'] = user['content']['realname']
            row['Email address'] = user['content']['email']
            row['Authentication System'] = user['content']['type']
            row['Lang'] = user['content']['lang']
            row['Time Zone'] = user['content']['tz']
            row['Default App'] = user['content']['defaultApp']
            row['Roles'] = ', '.join(user['content']['roles'])
            row['Status'] = self.conv.status(user['content']['locked-out'])
            table.append(row)
        return table
    
    def roles(self):
        resp = self.query(service='/servicesNS/-/-/authorization/roles?count=0', method='GET')
        ret = json.loads(resp.text)
        roles = ret['entry']
        table = []
        for role in roles:
            row = {}
            row['Role'] = role['name']
            row['Imported Roles'] = ', '.join(role['content']['imported_roles'])
            row['Allowed Indexes'] = ', '.join(set(role['content']['srchIndexesAllowed'] + role['content']['imported_srchIndexesAllowed']))
            row['Default Indexes'] = ', '.join(set(role['content']['srchIndexesDefault'] + role['content']['imported_srchIndexesDefault']))
            row['Max Search Jobs'] = role['content']['srchJobsQuota']
            row['Max RT Search Jobs'] = role['content']['rtSrchJobsQuota']
            table.append(row)
        return table

    def deployclients(self):
        resp = self.query(service='/servicesNS/-/-/deployment/server/clients?count=0', method='GET')
        ret = json.loads(resp.text)
        clients = ret['entry']
        table = []
        for client in clients:
            row = {}
            row['Host Name'] = client['content']['hostname']
            row['Client Name'] = client['content']['clientName']
            row['Instance Name'] = client['content']['instanceName']
            row['IP Address'] = client['content']['ip']
            row['Machine Type'] = client['content']['utsname']
            row['Version'] = client['content']['splunkVersion']
            row['Apps'] = ', '.join(client['content']['applications']) if client['content']['applications'] else 'None'
            row['Server Classes'] = ', '.join(client['content']['serverClasses']) if client['content']['serverClasses'] else 'None'
            table.append(row)
        return table

    def activesavedsearches(self):
        resp = self.query(service='/servicesNS/-/-/saved/searches?count=0', method='GET')
        ret = json.loads(resp.text)
        searches = ret['entry']
        table = []
        for search in searches:
            if search['content']['disabled'] or not search['content']['is_scheduled']:
                continue
            row = {}
            row['Name'] = search['name']
            row['App'] = search['acl']['app']
            row['State'] = self.conv.state(search['content']['disabled'])
            row['Scheduled'] = search['content']['is_scheduled']
            row['Schedule'] = search['content']['cron_schedule']
            row['Next Run'] = search['content']['next_scheduled_time']
            table.append(row)
        return table

    def process(self, block):
        block = block[next(iter(block))]
        if 'search' in block:
            table = self.search(block['search'])
            self.render.table(table)
        if 'content' in block:
            if 'indexes' == block['content']:
                table = self.indexes()
                self.render.table(table)
            if 'serverinfo' == block['content']:
                table = self.serverinfo()
                self.render.table(table)
            if 'licenseinfo' == block['content']:
                table = self.licenseinfo()
                self.render.table(table)
            if 'licensepoolinfo' == block['content']:
                table = self.licensepoolinfo()
                self.render.table(table)
            if 'apps' == block['content']:
                table = self.apps()
                self.render.table(table)
            if 'roles' == block['content']:
                table = self.roles()
                self.render.table(table)
            if 'users' == block['content']:
                table = self.users()
                self.render.table(table) 
            if 'deployclients' == block['content']:
                table = self.deployclients()
                self.render.table(table) 
            if 'activesavedsearches' == block['content']:
                table = self.activesavedsearches()
                self.render.table(table) 
        
if __name__ == '__main__':
    splunk = Splunk('https', '127.0.0.1', '8089')
    splunk.login('admin', '5plunk>%Txy')
    data = splunk.search('| eventcount summarize=f | table index')
    print(data)
