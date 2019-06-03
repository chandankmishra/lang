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
    #inplace_change(filename, "zephyr_epp_gen.h", "priv_zephyr_epp_gen.h")
    #inplace_change(filename, "zephyr_dlu_gen.h", "priv_zephyr_dlu_gen.h")
    #inplace_change(filename, "zephyr_filter_gen.h", "priv_zephyr_filter_gen.h")
    #inplace_change(filename, "zephyr_clist_gen.h", "priv_zephyr_clist_gen.h")
    #inplace_change(filename, "zephyr_irp_gen.h", "priv_zephyr_irp_gen.h")
    #inplace_change(filename, "zephyr_hostif_gen.h", "priv_zephyr_hostif_gen.h")
    #inplace_change(filename, "zephyr_viqm_gen.h", "priv_zephyr_viqm_gen.h")
    #inplace_change(filename, "zephyr_voqm_gen.h", "priv_zephyr_voqm_gen.h")
    #inplace_change(filename, "zephyr_ps_gen.h", "priv_zephyr_ps_gen.h")
    #inplace_change(filename, "zephyr_rs_gen.h", "priv_zephyr_rs_gen.h")
    #inplace_change(filename, "zephyr_zeg_gen.h", "priv_zephyr_zeg_gen.h")
    #inplace_change(filename, "zephyr_oqm_gen.h", "priv_zephyr_oqm_gen.h")
    #inplace_change(filename, "zephyr_cm_gen.h", "priv_zephyr_cm_gen.h")
    #inplace_change(filename, "zephyr_gs_gen.h", "priv_zephyr_gs_gen.h")
    #inplace_change(filename, "zephyr_gt_gen.h", "priv_zephyr_gt_gen.h")
    #inplace_change(filename, "zephyr_ccl0_gen.h", "priv_zephyr_ccl0_gen.h")
    #inplace_change(filename, "zephyr_ccl_gen.h", "priv_zephyr_ccl_gen.h")
    #inplace_change(filename, "zephyr_plct_gen.h", "priv_zephyr_plct_gen.h")
    #inplace_change(filename, "zephyr_slu_gen.h", "priv_zephyr_slu_gen.h")
    #inplace_change(filename, "zephyr_mce_gen.h", "priv_zephyr_mce_gen.h")
    #inplace_change(filename, "zephyr_pg_gen.h", "priv_zephyr_pg_gen.h")
    #inplace_change(filename, "zephyr_igp_misc_gen.h", "priv_zephyr_igp_misc_gen.h")
    #inplace_change(filename, "zephyr_cbuf_gen.h", "priv_zephyr_cbuf_gen.h")
    inplace_change(filename, "epp_test_junos_struct.h", "priv_epp_test_junos_struct.h")
    inplace_change(filename, "dlu_test_junos_struct.h", "priv_dlu_test_junos_struct.h")
    inplace_change(filename, "filter_test_junos_struct.h", "priv_filter_test_junos_struct.h")
    inplace_change(filename, "zfi_test_junos_struct.h", "priv_zfi_test_junos_struct.h")
    inplace_change(filename, "clist_test_junos_struct.h", "priv_clist_test_junos_struct.h")
    inplace_change(filename, "zfo_test_junos_struct.h", "priv_zfo_test_junos_struct.h")
    inplace_change(filename, "irp_test_junos_struct.h", "priv_irp_test_junos_struct.h")
    inplace_change(filename, "hsb5_junos_struct.h", "priv_hsb5_junos_struct.h")
    inplace_change(filename, "hif_junos_struct.h", "priv_hif_junos_struct.h")
    inplace_change(filename, "viqm_test_junos_struct.h", "priv_viqm_test_junos_struct.h")
    inplace_change(filename, "voqm_test_junos_struct.h", "priv_voqm_test_junos_struct.h")
    inplace_change(filename, "rs_test_junos_struct.h", "priv_rs_test_junos_struct.h")
    inplace_change(filename, "cm_test_junos_struct.h", "priv_cm_test_junos_struct.h")
    inplace_change(filename, "gs_test_junos_struct.h", "priv_gs_test_junos_struct.h")
    inplace_change(filename, "gt_test_junos_struct.h", "priv_gt_test_junos_struct.h")
    inplace_change(filename, "zeg_test_junos_struct.h", "priv_zeg_test_junos_struct.h")
    inplace_change(filename, "zig_test_junos_struct.h", "priv_zig_test_junos_struct.h")
    inplace_change(filename, "oqm_test_junos_struct.h", "priv_oqm_test_junos_struct.h")
    inplace_change(filename, "ps_test_junos_struct.h", "priv_ps_test_junos_struct.h")
    inplace_change(filename, "ccl_local_junos_struct.h", "priv_ccl_local_junos_struct.h")
    inplace_change(filename, "ccl_test_junos_struct.h", "priv_ccl_test_junos_struct.h")
    inplace_change(filename, "plct_test_junos_struct.h", "priv_plct_test_junos_struct.h")
    inplace_change(filename, "slu_test_junos_struct.h", "priv_slu_test_junos_struct.h")
    inplace_change(filename, "mce_test_junos_struct.h", "priv_mce_test_junos_struct.h")
    inplace_change(filename, "pg_test_junos_struct.h", "priv_pg_test_junos_struct.h")
    inplace_change(filename, "igp_misc_test_junos_struct.h", "priv_igp_misc_test_junos_struct.h")
    inplace_change(filename, "igp_test_junos_struct.h", "priv_igp_test_junos_struct.h")
    inplace_change(filename, "cbuf_test_junos_struct.h", "priv_cbuf_test_junos_struct.h")

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
