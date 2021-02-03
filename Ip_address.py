#write a python program to check whether entered Ip address in IPv4 or IPv6 or Neither

#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'validateAddresses' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY addresses as parameter.
#
def validateAddresses(addresses):
    result=[]
    for ip in addresses:
        if ":" in ip:
           if ("::" not in ip) and (len(ip.split(':'))!=8):
                result.append('Neither')
                continue
           else:
                if len(ip.split('::'))>2:
                    result.append('Neither')
                    continue
                flag=False
                for r in ip.split(':'):
                    if r:
                        if len(r)<=4:
                            try:
                                int(r,16)
                            except:
                                break
                        else:
                            result.append('Neither')
                            flag=True
                            break                               
                else:
                    result.append('IPv6')
                    continue
                if not flag:
                     result.append('Neither')
        elif "." in ip:
            if len(ip.split('.'))!=4:
                result.append( 'Neither')
                continue
            for r in ip.split('.'):
                if not r:
                    result.append( 'Neither')
                    break
                if len(r)>3:
                    result.append( 'Neither')
                    break
                if not(0<=int(r)<=255):
                    result.append( 'Neither')
                    break
                if r.startswith('0') and int(r)>0:
                    if int(r)>7:
                        result.append( 'Neither')
                        break
            else:
                result.append( 'IPv4')
        else:
            result.append('Neither')
    return result
if __name__ == '__main__':

validateAddresses(addresses)
