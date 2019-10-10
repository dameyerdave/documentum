# Splunk Documentation
## Machine information
{"localsplunk": { "content": "serverinfo" }}

## License information
{"localsplunk": { "content": "licenseinfo" }}

## License pool information
{"localsplunk": { "content": "licensepoolinfo" }}

## Indexes
{"localsplunk": { "content": "indexes" }}

## Events per index
{"localsplunk": { "search": "| eventcount summarize=f | table server, index, count" }}

## Apps
{"localsplunk": { "content": "apps" }}

## Roles
{"localsplunk": { "content": "roles" }}

## Users
{"localsplunk": { "content": "users" }}

## Forwarders
{"localsplunk": { "search": "search index=_internal earliest=0 source=*metrics.log group=tcpin_connections | eval sourceHost=if(isnull(hostname), sourceHost, hostname) | eval fwdType=case(fwdType==\"uf\", \"Universal Forwarder\", fwdType==\"full\", \"Heavy Forwarder\") | stats count by fwdType connectionType version sourceHost sourceIp splunk_server destPort | rename fwdType as ForwarderType connectionType as ConnectionType sourceHost as SourceHost version as Version destPort as DestPort splunk_server as Indexer sourceIp as SourceIP | fields - count" }}

## Deployment Clients
{"localsplunk": { "content": "deployclients" }}

## Active Saved Searches
{"localsplunk": { "content": "activesavedsearches" }}
