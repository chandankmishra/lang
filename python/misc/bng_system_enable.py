#!/usr/bin/python

import xmlrpclib, sys, os

cobbler_server = 'bng-olive1-dcbg.englab.juniper.net'

server = xmlrpclib.Server("http://%s/cobbler_api" %(cobbler_server))
token = server.login("cobbler","Embe1mpls")

def set_netbootable(system_name, state):
    "Enable or disable system for netbooting"

    handle = server.get_system_handle(system_name, token)
    server.modify_system(handle, 'netboot_enabled', state, token)
    server.save_system(handle, token)

def set_profile(sname):
    "Set a profile if provided else keep the default profile"
    try:
        known_systems = [ system1['name'] for system1 in server.get_systems() ]
        if sname not in known_systems:
            sys.exit('System "%s" not defined in cobbler server "%s".\nPlease register the system and retry' 
                    %(sname, cobbler_server))
        MY_HASH = server.get_system_as_rendered(sname)
        if len(sys.argv) < 4: 
            pname = MY_HASH['profile_name']
            print "No profile specified keeping default :", pname
        else:
            pname = (sys.argv[3])
            known_profiles = [ profile1['name'] for profile1 in server.get_profiles() ]
            if pname not in known_profiles:
                sys.exit('Profile "%s" not defined in cobbler server "%s".' 
                        % (pname, cobbler_server))
            handle = server.get_system_handle(sname, token)
            server.modify_system(handle, 'profile', pname, token)
            server.save_system(handle, token)
    except Exception, e:
        print "ERROR: %s" % e
        sys.exit('System name or profile is not defined')

def check_state(sname):
    "Check the state of a machine"

    MY_HASH = server.get_system_as_rendered(sname)
    print sname, "netboot-enabled = ", MY_HASH['netboot_enabled']
    print sname, "profile = ", MY_HASH['profile_name']

def check_cmdline():
    "Check the command line passed"

    if len(sys.argv) == 2:
        return True
    else:
        state = sys.argv[2]
        if state in [ 'en', 'enable' ]:
            return True
        elif [ 'dis', 'disable' ]:
            return False
        else:
            print 'second arg must be enable or disable'
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("""Must provide system name and enable or disable
                  e.g.: testbed_enable.py dc-rod-test-pp-a enable DC-SW01""")
    
    system_name = sys.argv[1]
    endis = check_cmdline()
    set_profile(system_name)
    set_netbootable(system_name, endis)
    check_state(system_name)
