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
    inplace_change(filename, "!zph_", "!zephyr_")
    inplace_change(filename, " ZPH$", " ZPH$")
    inplace_change(filename, " ZPH ", " ZPH ")
    inplace_change(filename, " ZPH.", " ZPH.")
    inplace_change(filename, "/zph/", "/zephyr/")
#    inplace_change(filename, "PIZEPHYR", "PIZPH")
#    inplace_change(filename, "REZEPHYRAT", "REZPHAT")
#    inplace_change(filename, "TYZEPHYR", "TYZPH")
#    inplace_change(filename, "SZEPHYRED", "SZPHED")
#    inplace_change(filename, "SZEPHYRCIAL", "SZPHCIAL")
#    inplace_change(filename, "SWAPZEPHYRD", "SWAPZPHD")
#    inplace_change(filename, "MZEPHYRRR", "MZPHRR")
#    inplace_change(filename, "LVZEPHYRCL", "LVZPHCL")
#    inplace_change(filename, "pizephyr", "pizph")
#    inplace_change(filename, "rezephyrat", "rezphat")
#    inplace_change(filename, "tyzephyr", "tyzph")
#    inplace_change(filename, "szephyred", "szphed")
#    inplace_change(filename, "szephyrcial", "szphcial")
#    inplace_change(filename, "swapzephyrd", "swapzphd")

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
