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
    inplace_change(filename, "zephyr_encap_erw.h", "priv_zephyr_encap_erw.h")
    inplace_change(filename, "zephyr_epp_init.h", "priv_zephyr_epp_init.h")
    inplace_change(filename, "zephyr_dlu_init.h", "priv_zephyr_dlu_init.h")
    inplace_change(filename, "zephyr_filter.h", "priv_zephyr_filter.h")
    inplace_change(filename, "zephyr_clist.h", "priv_zephyr_clist.h")
    inplace_change(filename, "zephyr_headers.h", "priv_zephyr_headers.h")
    inplace_change(filename, "zephyr_viqm.h", "priv_zephyr_viqm.h")
    inplace_change(filename, "zephyr_ps.h", "priv_zephyr_ps.h")
    inplace_change(filename, "zephyr_zeg.h", "priv_zephyr_zeg.h")
    inplace_change(filename, "zephyr_zig.h", "priv_zephyr_zig.h")
    inplace_change(filename, "zephyr_oqm.h", "priv_zephyr_oqm.h")
    inplace_change(filename, "zephyr_cm.h", "priv_zephyr_cm.h")
    inplace_change(filename, "zephyr_plct.h", "priv_zephyr_plct.h")
    inplace_change(filename, "zephyr_slu_init.h", "priv_zephyr_slu_init.h")
    inplace_change(filename, "zephyr_sa_learning.h", "priv_zephyr_sa_learning.h")
    inplace_change(filename, "zephyr_mce.h", "priv_zephyr_mce.h")
    inplace_change(filename, "zephyr_pg.h", "priv_zephyr_pg.h")
    inplace_change(filename, "zephyr_hdrparser_igp.h", "priv_zephyr_hdrparser_igp.h")
    inplace_change(filename, "zephyr_igp_misc.h", "priv_zephyr_igp_misc.h")
    inplace_change(filename, "zephyr_igp.h", "priv_zephyr_igp.h")
    inplace_change(filename, "zephyr_hdrparser_egp.h", "priv_zephyr_hdrparser_egp.h")
    inplace_change(filename, "zephyr_cbuf.h", "priv_zephyr_cbuf.h")

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
        print (filename)
        #print os.path.join(root,filename)
        replace_file(os.path.join(root,filename))
