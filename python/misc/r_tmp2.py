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
    #inplace_change(filename,"mexpr_pkt_priv.h","priv_pkt.h")
    #inplace_change(filename,"jc_rt_priv.h","priv_jc_rt.h")
    #inplace_change(filename,"analyzer_priv.h","priv_analyzer.h")
    #inplace_change(filename,"jmexpr_slu_hash_priv.h","priv_jutils_slu_hash.h")
    #inplace_change(filename,"jmexpr_utils_priv.h","priv_jutils.h")

    #inplace_change(filename,"mexpr_pkt_dbg.h","priv_pkt_dbg.h")
    #inplace_change(filename,"mexpr_pkt_tree.h","priv_pkt_tree.h")
    #inplace_change(filename,"mexpr_pkt_ring.h","priv_pkt_ring.h")
    #inplace_change(filename,"mexpr_pkt_dma.h","priv_pkt_dma.h")
    #inplace_change(filename,"mexpr_pkt_xfer_toe.h","priv_pkt_xfer_toe.h")
    #inplace_change(filename,"mexpr_pkt_ddos_shared.h","priv_pkt_ddos_shared.h")
    #inplace_change(filename,"mexpr_pkt_queue.h","priv_pkt_queue.h")
    #inplace_change(filename,"mexpr_pkt_incl.h","priv_pkt_incl.h")
    #inplace_change(filename,"mexpr_pkt_inline_ka.h","priv_pkt_inline_ka.h")
    #inplace_change(filename,"mexpr_pkt_ddos.h","priv_pkt_ddos.h")

    #inplace_change(filename,"nh_priv_common.h","priv_nh_common.h")
    #inplace_change(filename,"nh_priv_gre.h","priv_nh_gre.h")
    #inplace_change(filename,"nh_priv_mexpr.h","priv_nh.h")
    #inplace_change(filename,"nh_priv_mcast.h","priv_nh_mcast.h")

    #inplace_change(filename,"if_vrrpmac_mexpr.h","priv_if_vrrpmac.h")
    #inplace_change(filename,"if_vlan_qfx.h","priv_if_vlan.h")
    #inplace_change(filename,"if_tree_qfx.h","priv_if_tree.h")
    #inplace_change(filename,"if_shared_qfx.h","mexpr_if_shared.h")
    #inplace_change(filename,"if_port_mexpr.h","priv_if_port.h")
    #inplace_change(filename,"if_dot1br_qfx.h","priv_if_dot1br.h")
    #inplace_change(filename,"if_mymac_mexpr.h","priv_if_mymac.h")
    #inplace_change(filename,"priv_if_parser_qfx.h","priv_if_parser.h")
    #inplace_change(filename,"if_packet_qfx.h","priv_if_packet.h")
    #inplace_change(filename,"if_mtip_mexpr.h","priv_if_mtip.h")
    #inplace_change(filename,"if_esi.h","priv_if_esi.h")
    #inplace_change(filename,"if_l2_qfx.h","priv_if_l2.h")
    #inplace_change(filename,"if_cfm_mexpr.h","priv_if_cfm_platform.h")
    #inplace_change(filename,"if_cfm.h","priv_if_cfm.h")
    #inplace_change(filename,"if_incl_qfx.h","priv_if_incl.h")

    #inplace_change(filename,"l2_scntl.h","priv_l2_scntl.h")
    #inplace_change(filename,"l2_sa.h","priv_l2_sa.h")
    #inplace_change(filename,"l2_rt.h","priv_l2_rt.h")
    #inplace_change(filename,"l2_priv.h","priv_l2.h")
    #inplace_change(filename,"l2_learning.h","priv_l2_learning.h")
    #inplace_change(filename,"l2_incl.h","priv_l2_incl.h")
    #inplace_change(filename,"l2_flex_vlan.h","priv_l2_flex_vlan.h")
    #inplace_change(filename,"l2_fdb.h","priv_l2_fdb.h")
    #inplace_change(filename,"l2_bd.h","priv_l2_bd.h")
    #inplace_change(filename,"l2_aging.h","priv_l2_aging.h")
    #inplace_change(filename,"l2_tree.h","priv_l2_tree.h")

    #inplace_change(filename,"sflow_halp.h","priv_sflow_halp.h")
    #inplace_change(filename,"mexpr_sflow_tree.h","priv_sflow_tree.h")
    #inplace_change(filename,"sflow_tree.h","priv_sflow_tree.h")
    #inplace_change(filename,"priv_priv","priv")

    #inplace_change(filename,"caem_toe.h","priv_caem_toe.h")
    #inplace_change(filename,"caem_halp_mexpr.h","priv_caem_halp.h")
    #inplace_change(filename,"caem_capability_mexpress.h","priv_caem_capability.h")

    #inplace_change(filename,"","priv_")
    #inplace_change(filename,"analyzer_tree.h","priv_analyzer_tree.h")
    #inplace_change(filename,"analyzer_incl.h","priv_analyzer_incl.h")
    #inplace_change(filename,"analyzer_parser.h","priv_analyzer_parser.h")

    #inplace_change(filename,"nh_virtual.h","priv_nh_virtual.h")
    #inplace_change(filename,"nh_includes.h","priv_nh_includes.h")
    #inplace_change(filename,"nh_unilist.h","priv_nh_unilist.h")
    #inplace_change(filename,"nh_host_mexpr_qfx_q.h","priv_nh_host_qfx_q.h")
    #inplace_change(filename,"nh_host_mexpr_qfx.h","priv_nh_host_qfx.h")
    #inplace_change(filename,"nh_host_anchor_qfx.h","priv_nh_host_anchor_qfx.h")
    #inplace_change(filename,"nh_host.h","priv_nh_host.h")
    #inplace_change(filename,"nh_encaps.h","priv_nh_encaps.h")
    #inplace_change(filename,"nh_composite_lb.h","priv_nh_composite_lb.h")

    #inplace_change(filename,"plct_tree.h","priv_plct_tree.h")
    inplace_change(filename,"jmexpr_priv_plct_tree.h","priv_jplct_tree.h")
    inplace_change(filename,"","")


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
