# Source - https://stackoverflow.com/a/3207973
# Posted by pycruft, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-14, License - CC BY-SA 4.0

from os import listdir
from os.path import isfile, join
print ("\"")
print ('a')
mypath="c:\\icon_db\\"
list_dir=listdir(mypath)


ll=list_dir[:5]
for abcd in ll:
    print (abcd)

asked_count=5

real_count=0
for k in list_dir:
    print(k)
    real_count=real_count+1
    if real_count == asked_count :
        break

newlist=[]
for k in list_dir:
    fullpath=mypath+k
    print (fullpath)
    bisfile=isfile(fullpath)
    if bisfile == False:
        print (k)
    newlist.append(k)

for file in newlist:
    print(file)







for f in listdir(mypath):
    print(f)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    print (file)
