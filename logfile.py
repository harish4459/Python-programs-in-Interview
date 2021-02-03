# Python Program to find the total bytes of data and unique clients count from the log file having the log lines of format with "clientname client_url logline date time" 


import re
import sys
log_data=sys.stdin.read()
bytes_sent=0
clients=0
clients_data=[]
for log_line in log_data.split('\n'):
    r=re.match("^(\S+) (\S+) (\[.*\]) (\".*?\") (\d+) (\d+) .*$", log_line)
    ip_add=r.groups()[0]
    if ip_add not in clients_data:
        clients_data.append(ip_add)
        clients += 1
    bytes_sent += int(r.groups()[-1])
print("Summary: total bytes sent=" +str(bytes_sent) +', unique clients=' +str(clients))
