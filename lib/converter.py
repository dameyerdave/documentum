from collections import OrderedDict
import re, math

class Converter:
    # Splunk calculates with 364 days per year!!
    interval_dict = OrderedDict([("Y", 364*86400),  # 1 year
                             ("M", 30*86400),   # 1 month
                             ("W", 7*86400),    # 1 week
                             ("D", 86400),      # 1 day
                             ("h", 3600),       # 1 hour
                             ("m", 60),         # 1 minute
                             ("s", 1)])         # 1 second

    def timeperiod(self, seconds):
        seconds = int(seconds)
        string = ""
        for unit, value in self.interval_dict.items():
            subres = int(seconds / value)
            if subres:
                seconds -= value * subres
                string += str(subres) + unit + ' '
        return string[:-1]
           
    def mbs(self, mb):
        mb = int(mb)
        return self.bytes(mb * 1024 * 1024)

    def bytes(self, byte):
        try:
            byte = int(byte)
            if (byte == 0):
                return '0 B'
            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            index = int(math.floor(math.log(byte, 1024)))
            power = math.pow(1024, index)
            size = round(byte / power, 2)
            return "{} {}".format(size, size_name[index])
        except ValueError as ve:
            return byte

    def state(self, state):
        if not state:
            return 'Enabled'
        else:
            return 'Disabled'

    def status(self, state):
        if not state:
            return 'Active'
        else:
            return 'Inactive'
