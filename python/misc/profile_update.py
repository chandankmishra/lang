#!/usr/bin/python

import xmlrpclib, sys, os.path

if len(sys.argv) < 4:
    sys.exit("Must provide profile name, distribution, and kickstart template\nex: profile_update.py DC-INFRA15 pp-distro-centos-5.4-x86_64 PPBranchInstall.ks")

#DC-INFRA15 qfd-x86_64_11.3R1_R2 QFD11.3R1-R2.ks
if len(sys.argv) == 5:
    cobbler_server = (sys.argv[4])
elif os.path.exists("/volume/dcg-sw/kickstarts"):
    cobbler_server = '10.94.184.230'
else:
    cobbler_server = 'bng-olive1-dcbg.englab.juniper.net'

pname = (sys.argv[1])
dname = (sys.argv[2])
kname = (sys.argv[3])

print "Netboot server is: ", cobbler_server
print "[", pname,dname,kname, "]"

server = xmlrpclib.Server("http://%s/cobbler_api" %(cobbler_server))
token = server.login("cobbler","Embe1mpls")

def profile(sname):
    "Set a profile if provided else keep the default profile"
    try:
        pname = (sys.argv[1])
        phandle = server.get_profile_handle(pname, token);
        MY_HASH = server.get_profile_as_rendered(pname)
        print MY_HASH['distro']
        print MY_HASH['kickstart']

        server.modify_profile(phandle, 'distro', dname, token);
        server.modify_profile(phandle, 'kickstart', kname, token);
        server.save_profile(phandle, token)

        MY_HASH = server.get_profile_as_rendered(pname)
        print MY_HASH['distro']
        print MY_HASH['kickstart']

    except Exception, e:
        print "ERROR: %s" % e
        sys.exit('System name or profile is not defined')

def check_it(sname):
    # check the state of a machine
    MY_HASH = server.get_system_as_rendered(sname)
    print sname, "netboot-enabled = ", MY_HASH['netboot_enabled']
    print sname, "profile = ", MY_HASH['profile']
    MY_MGMT = MY_HASH['mgmt_parameters']
    print "default profile is ", MY_MGMT['branch']


system_name = (sys.argv[1])
profile(system_name)
#check_it(system_name)
