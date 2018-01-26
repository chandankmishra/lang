#!/usr/bin/python
# This script is used to replace patricular string with another string
# in the given list of files

#find * | grep "/"|awk '{printf "mv "$0; gsub("pechip", "zephyr", $0);print " "$0;}'|sh
import os
import string
import re

def inplace_change(filename, old_string, new_string):
        s=open(filename).read()
        if old_string in s:
                print 'Changing "{old_string}" to "{new_string}"'.format(**locals())
                s=s.replace(old_string, new_string)
                f=open(filename, 'w')
                f.write(s)
                f.flush()
                f.close()
        else:
                print 'No occurances of "{old_string}" found.'.format(**locals())

def replace_file(filename):
    print (filename)
    #inplace_change(filename, "", "")
    inplace_change(filename, "old_string", "new_string")

#for root, directories, filenames in os.walk('/b/cmishra/PVT_ZH_BRINGUP_JUNOS_BRANCH/src/pfe/common/pfe-arch/mzphr/'):
for root, directories, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith(".cpp") or filename.endswith(".h"):
            print (filename)
            #print os.path.join(root,filename)
            replace_file(os.path.join(root, filename))
