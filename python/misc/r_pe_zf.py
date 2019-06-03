#!/usr/bin/python
#find * | grep "/"|awk '{printf "mv "$0; gsub("pechip", "zephyr", $0);print " "$0;}'|sh
import os

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
    inplace_change(filename, "MEXPR_PE_", "MEXPR_ZEPHYR_")
    inplace_change(filename, "_PE_", "_ZEPHYR_")
    inplace_change(filename, "_pe_", "_zephyr_")
    inplace_change(filename, "=PE_", "=ZEPHYR_")
    inplace_change(filename, "(PE_", "(ZEPHYR_")
    inplace_change(filename, ")PE_", ")ZEPHYR_")
    inplace_change(filename, "\"PE_", "\"ZEPHYR_")
    inplace_change(filename, " PE_", " ZEPHYR_")
    inplace_change(filename, "[PE_", "[ZEPHYR_")
    inplace_change(filename, "(pe_", "(zephyr_")
    inplace_change(filename, ")pe_", ")zephyr_")
    inplace_change(filename, "\"pe_", "\"zephyr_")
    inplace_change(filename, " pe_", " zephyr_")
    inplace_change(filename, "[pe_", "[zephyr_")

    inplace_change(filename, " PECHIP ", " ZEPHYR ")
    inplace_change(filename, "PECHIP", "ZEPHYR")
    inplace_change(filename, " pechip ", " zephyr ")
    inplace_change(filename, "pechip", "zephyr")
    #inplace_change(filename, "#include \"zephyr_struct.h\"", "")
    #inplace_change(filename, "#include \"include/zephyr_struct.h\"", "")
    #inplace_change(filename, "#include <zephyr_struct.h>", "")
    #inplace_change(filename, "#include <include/zephyr_struct.h>", "")
    #inplace_change(filename, "#include \"zephyr/include/zephyr_struct.h\"", "")
    #inplace_change(filename, "#include <zephyr/include/zephyr_struct.h>", "")

def walk_dir():
    l = os.listdir(os.getcwd())
    for i in l:
        if os.path.isdir(i) == True:
            print (i)
            #replace_file(i)

#walk_dir()

#for root, directories, filenames in os.walk('/b/cmishra/PVT_ZH_BRINGUP_JUNOS_BRANCH/src/pfe/common/pfe-arch/mexpr/'):
for root, directories, filenames in os.walk(os.getcwd()):
    for filename in filenames: 
        #print os.path.join(root,filename)
        replace_file(os.path.join(root,filename))
