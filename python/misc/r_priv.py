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
    inplace_change(filename, "priv_priv.h", "priv.h.h")

    inplace_change(filename, "jmexpr_encap_priv.h", "priv_jencap.h")
    inplace_change(filename, "jmexpr_encap_priv.h", "priv_jencap.h")
    inplace_change(filename, "jmexpr_encap_vlan_sel.h", "priv_jencap_vlan_sel.h")
    inplace_change(filename, "jmexpr_encap_vlan_sel.h", "priv_jencap_vlan_sel.h")
    inplace_change(filename, "jmexpr_encap_port_tix.h", "priv_jencap_port_tix.h")
    inplace_change(filename, "jmexpr_encap_const_mem.h", "priv_jencap_const_mem.h")
    inplace_change(filename, "jmexpr_encap_tunnel.h", "priv_jencap_tunnel.h")
    inplace_change(filename, "jmexpr_encap_parser.h", "priv_jencap_parser.h")
    inplace_change(filename, "jmexpr_encap_absent.h", "priv_jencap_absent.h")
    inplace_change(filename, "jmexpr_encap_desc.h", "priv_jencap_desc.h")
    inplace_change(filename, "jmexpr_encap_erw_tbl.h", "priv_jencap_erw_tbl.h")
    inplace_change(filename, "jmexpr_encap_flt_data_sel.h", "priv_jencap_flt_data_sel.h")
    inplace_change(filename, "jmexpr_encap_generic_tbl.h", "priv_jencap_generic_tbl.h")
    inplace_change(filename, "jmexpr_encap_packet_check.h", "priv_jencap_packet_check.h")
    inplace_change(filename, "jmexpr_encap_tmplt.h", "priv_jencap_tmplt.h")
    inplace_change(filename, "jmexpr_encap_tree.h", "priv_jencap_tree.h")
    inplace_change(filename, "jmexpr_encap_includes.h", "priv_jencap_platform_include.h")
    inplace_change(filename, "jmexpr_encap_include.h", "priv_jencap_include.h")

    inplace_change(filename, "jmexpr_chash_tree.h", "priv_jchash_tree.h")
    inplace_change(filename, "jmexpr_chash_parser.h", "priv_jchash_parser.h")
    inplace_change(filename, "jmexpr_chash.h", "priv_jchash.h")

    inplace_change(filename, "jmexpr_if_tree.h", "priv_jif_tree.h")
    inplace_change(filename, "jmexpr_if_stp.h", "priv_jif_stp.h")
    inplace_change(filename, "jmexpr_if_port.h", "priv_jif_port.h")
    inplace_change(filename, "jmexpr_if_l2d.h", "priv_jif_l2d.h")
    inplace_change(filename, "jmexpr_if_ai_etypes.h", "priv_jif_ai_etypes.h")
    inplace_change(filename, "jmexpr_if_lport.h", "priv_jif_lport.h")
    inplace_change(filename, "jmexpr_if_parser.h", "priv_jif_parser.h")
    inplace_change(filename, "priv_jmexpr_if.h", "priv_jif.h")

    #inplace_change(filename, "jmexpr_dlu_alpha.h", "priv_jfdb_dlu_alpha.h")
    #inplace_change(filename, "jmexpr_dlu_alpha_priv.h", "priv_jfdb_dlu_alpha.h")
    #inplace_change(filename, "jmexpr_fdb.h", "priv_jfdb.h")
    #inplace_change(filename, "jmexpr_fdb_fasthash_tbl.h", "priv_jfdb_fasthash_tbl.h")
    #inplace_change(filename, "jmexpr_fdb_tree.h", "priv_jfdb_tree.h")
    #inplace_change(filename, "jmexpr_misc_rm.h", "priv_jfdb_misc_rm.h")

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
    inplace_change(filename, "cbuf/zephyr_cbuf.h", "zephyr_cbuf.h")

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
