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
    #inplace_change(filename, "PFE_CHIPSET_ZH", "PFE_CHIPSET_ZEPHYR")
    #inplace_change(filename, "jbeta_zephyr", "jmexpr_beta")
    #inplace_change(filename, "JBETA_ZEPHYR", "JMEXPR_BETA")
    #inplace_change(filename, "jbeta_zephyr", "jmexpr_alpha")
    #inplace_change(filename, "JBETA_ZEPHYR", "JMEXPR_ALPHA")
    #inplace_change(filename, "jchash_zephyr", "jmexpr_chash")
    #inplace_change(filename, "JCHASH_ZEPHYR", "JMEXPR_CHASH")
    #inplace_change(filename, "jcv_zephyr", "jmexpr_cv")
    #inplace_change(filename, "JCV_ZEPHYR", "JMEXPR_CV")
    #inplace_change(filename, "jencap_zephyr", "jmexpr_encap")
    #inplace_change(filename, "JENCAP_ZEPHYR", "JMEXPR_ENCAP")
    #inplace_change(filename, "jfdb_zephyr", "jmexpr_fdb")
    #inplace_change(filename, "JFDB_ZEPHYR", "JMEXPR_FDB")
    #inplace_change(filename, "jfdb_zephyr", "jmexpr_fdb")
    #inplace_change(filename, "JFDB_ZEPHYR", "JMEXPR_FDB")
    #inplace_change(filename, "jfw_zephyr", "jmexpr_fw")
    #inplace_change(filename, "JFW_ZEPHYR", "JMEXPR_FW")
    #inplace_change(filename, "jif_zephyr", "jmexpr_if")
    #inplace_change(filename, "JIF_ZEPHYR", "JMEXPR_IF")
    #inplace_change(filename, "jnh_zephyr", "jmexpr_nh")
    #inplace_change(filename, "JNH_ZEPHYR", "JMEXPR_NH")
    #inplace_change(filename, "jplct_zephyr", "jmexpr_plct")
    #inplace_change(filename, "JPLCT_ZEPHYR", "JMEXPR_PLCT")
    #inplace_change(filename, "jsal_zephyr", "jmexpr_sal")
    #inplace_change(filename, "JSAL_ZEPHYR", "JMEXPR_SAL")
    #inplace_change(filename, "jsample_zephyr", "jmexpr_sample")
    #inplace_change(filename, "JSAMPLE_ZEPHYR", "JMEXPR_SAMPLE")
    #inplace_change(filename, "jtopo_zephyr", "jmexpr_topo")
    #inplace_change(filename, "JTOPO_ZEPHYR", "JMEXPR_TOPO")
    #inplace_change(filename, "jutils_mexpr", "jmexpr_utils")
    #inplace_change(filename, "JUTILS_MEXPR", "JMEXPR_UTILS")
    #inplace_change(filename, "MEXPR", "EXPR")
    inplace_change(filename, "MMEXPR", "MEXPR")
    inplace_change(filename, "mexpr", "expr")
    inplace_change(filename, "EXPR", "MEXPR")
    inplace_change(filename, "expr", "mexpr")
    inplace_change(filename, "jmmexpr", "jmexpr")
    inplace_change(filename, "jmmexpr", "jmexpr")
    inplace_change(filename, "mmexpr", "mexpr")
    inplace_change(filename, "mexpressed", "expressed")
    inplace_change(filename, "MMEXPR", "MEXPR")
    inplace_change(filename, "JMMEXPR", "JMEXPR")
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
