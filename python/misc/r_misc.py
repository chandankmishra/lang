#!/usr/bin/python
#find * | grep "/"|awk '{printf "mv "$0; gsub("pechip", "zephyr", $0);print " "$0;}'|sh
import os
import string
import re

def inplace_change(filename, old_string, new_string):
        s=open(filename).read()
        if old_string in s:
                print 'Changing "{old_string}" to "{new_string}"'.format(**locals())
                s=s.replace(old_string, new_string)
                #lreplace(old_string, new_string,s)
                #s=re.sub('^%s' % old_string, new_string, s)
                f=open(filename, 'w')
                f.write(s)
                f.flush()
                f.close()
        else:
                print 'No occurances of "{old_string}" found.'.format(**locals())

def replace_file(filename):
    print (filename)
    #inplace_change(filename, "", "")
    inplace_change(filename, "zhchip", "btchip")
    inplace_change(filename, "ZHCHIP", "BTCHIP")
    inplace_change(filename, "ZH ", "BT ")
    inplace_change(filename, "ZH_", "BT_")
    inplace_change(filename, "zh_", "bt_")
    inplace_change(filename, "zh ", "bt ")
    #inplace_change(filename, "Debug.set_debug(True)", "Debug.set_debug()")
    #inplace_change(filename, "Debug.set_debug(\"True\")", "Debug.set_debug()")
    #inplace_change(filename, "Debug.set_debug('True')", "Debug.set_debug()")
    #inplace_change(filename, "Debug.set_debug(False)", "Debug.set_debug()")
    #inplace_change(filename, "", "")
    #inplace_change(filename, "ZEPHYR_SLU", "EXPR_SLU")

#for root, directories, filenames in os.walk('/b/cmishra/PVT_ZH_BRINGUP_JUNOS_BRANCH/src/pfe/common/pfe-arch/mzphr/'):
for root, directories, filenames in os.walk(os.getcwd()):
    for filename in filenames: 
        #if filename.endswith(".py"):
        #if filename.endswith(".robot") or filename.endswith(".py"):
        #if filename.endswith(".txt") or filename.endswith(".py") or filename.endswith(".robot"):
        if filename.endswith(".c") or filename.endswith(".h") or filename.endswith(".gram") or filename.endswith(".inc"):
            print (filename)
            #print os.path.join(root,filename)
            replace_file(os.path.join(root, filename))
#end of file
