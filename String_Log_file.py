# Log file with url and data ,need to print with unique site urls with count how many lines it is there in log file and write to other file.

# read the string filename
filename = input()
out={}
with open(filename,'r') as fp:
    data=fp.readlines()
for x in data:
    site_url,site_data =x.split(' - - ')
    if out.get(site_url):
        out[site_url]+=1
    else:
        out[site_url]=1
with open('records_'+filename,'w')as fp:
    for x in sorted(out.keys()):
        fp.write(x+" "+str(out[x]))
        fp.write('\n')
