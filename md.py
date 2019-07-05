from collections import OrderedDict
import re, math

class Renderer:
    def table(self, table):
        first_row = True
        header = ''
        separator = ''
        first_line = ''
        for row in table:
            ll = ''
            for field, value in row.items():
                if first_row:
                    header += '|' + field
                    separator += '|---'
                    first_line += '|' + str(value)
                else:
                    ll += '|' + str(value)
            if first_row: 
                print(header + '|')
                print(separator + '|')
                print(first_line + '|')
                first_row = False
            else:
                print(ll + '|')
