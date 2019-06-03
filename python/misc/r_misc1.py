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
    #inplace_change(filename, "jmexpr_if_l2d_ht_ent_t", "jif_l2d_ht_ent_t")
    #inplace_change(filename, "mexpr_fdb_app_data_t", "jfdb_app_data_t")
    #inplace_change(filename, "jp_mexpr_if_plugin_cr_tr.h", "jp_mexpr_if_plugin.h")
    #inplace_change(filename, "public_cr_tr.h", "public.h")
    #inplace_change(filename, "trace_cr_tr.h", "trace.h")
    #inplace_change(filename, "plugin_cr_tr.h", "plugin.h")
    #inplace_change(filename, "pfe_mexpr_cr_tr.h", "pfe_mexpr.h")
    #inplace_change(filename, "ZH_BRINGUP_FIXME", "ZH_DRIVER_READY")
    #inplace_change(filename, "if_port_qfx.c", "if_port_mexpr.c")
    #inplace_change(filename, "if_port_qfx.h", "if_port_mexpr.h")
    #inplace_change(filename, "pedlu", "zephyrdlu")
    #inplace_change(filename, "PEDLU", "ZEPHYRDLU")

    #inplace_change(filename, "global_fpc_slot_id_t", "mexpr_global_fpc_slot_id_t")
    #inplace_change(filename, "pic_slot_t", "mexpr_pic_slot_t")

    #inplace_change(filename, "ppfe_id_t", "mexpr_ppfe_id_t")
    #inplace_change(filename, "vpfe12_id_t", "mexpr_vpfe12_id_t")
    #inplace_change(filename, "vpfe14_id_t", "mexpr_vpfe14_id_t")
    #inplace_change(filename, "voq_id_t", "mexpr_voq_id_t")

    inplace_change(filename, "mexpr_ppfe_id_t", "ppfe_id_t")
    inplace_change(filename, "mexpr_vpfe12_id_t", "vpfe12_id_t")
    inplace_change(filename, "mexpr_vpfe14_id_t", "vpfe14_id_t")
    inplace_change(filename, "mexpr_voq_id_t", "voq_id_t")

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
