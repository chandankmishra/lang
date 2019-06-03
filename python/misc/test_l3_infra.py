"""Contains routines for L2 vlan-tagging test cases."""
# pragma pylint: disable=line-too-long, bad-continuation, unused-variable, missing-docstring, pointless-string-statement, unnecessary-semicolon, bare-except, bad-whitespace, catching-non-exception, superfluous-parens, too-many-statements, too-many-locals, import-error, invalid-name
import time
import warnings
import sys
import pdb
import threading
import yaml
import inspect
import re

from lxml import etree
import xmltodict

from lib.devtest.feature.l2.vlan import Vlan
from lib.devtest.feature.lag.lag import Lag
from infra.traffic import Traffic
from infra.interface import Interface
from infra.utils import Utils
from infra.device import Device
from infra.debug import Debug
from infra.base import Base
from infra.db import Db
from infra.hlt import HLT
from lib.infra.traffic_utils import TrafficUtils
from lib.devtest.feature.l3.l3_infra import L3Infra

class TestL3Infra(Base):
    ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'

    def __init__(self, **kvargs):
        Base.__init__(self, **kvargs)
        self._port_info = {}
        self._port_map = {}
        self._device_handle = {}
        self._port_handle = []
        self.interface_list_1 = []
        self.interface_list_2 = []
        self._default_log_level = kvargs.get('log', 'INFO')
        self.R0 = None
        self.R1 = None

        # intialize global variables
        self._MAX_PORTS     = 3
        self._MAX_PORTS_R0   = 2
        self._MAX_PORTS_R1   = 1
        # initialize objects
        self._intf      = Interface()
        self._vlan      = Vlan()
        self._traffic_utils = TrafficUtils()
        self._l3_infra = L3Infra()
        #set log level
        Debug.set_log_level(self._default_log_level)

    def configure_l3_interface (self, **kwargs):
        debug = kwargs.get('debug', False)
        set_method = inspect.stack()[0][3]
        port_info = kwargs.get('port_info', {})
        device = kwargs.get('device', None)
        misc_config     = kwargs.get('misc_config', [])

        if not device:
            raise AssertionError("Please give the device for which you need to configure the vlan \n")

        # If port_info has been passed configure based on it.
        # else, just config and commit the config lines passed by the caller.
        for port in port_info.keys():
            logical1   = str(port_info[port]['port_config']['logical1'])
            ip_src_addr = str(port_info[port]['traffic_config']['ip_src_addr'])
            ip_src_subnet_mask = str(port_info[port]['traffic_config']['ip_src_subnet_mask'])
            Device.config(cmd='set interfaces ' + logical1 + ' family inet address ' + ip_src_addr + '/' + ip_src_subnet_mask, handle=device)

        for conf_lines in misc_config:
            Device.config(cmd=conf_lines, handle=device)

        # commit the configuration
        Device.commit(handle=device)

    def configure_misc_config (self, **kwargs):
        debug       = kwargs.get('debug', False)
        device      = kwargs.get('device', None)
        Debug.set_debug(debug)
        set_method  = inspect.stack()[0][3]
        port_info   = kwargs.get('port_info', {})
        misc_config = kwargs.get('misc_config', [])
        if not device:
            raise AssertionError("Please give the device for which you need to configure the vlan \n")

        for conf_lines in misc_config:
            Device.config(cmd=conf_lines, handle=device)

        # commit the configuration
        Device.commit(handle=device)

    def start_traffic (self, **kvargs):
        # fix me : Spirent/port infor should come from params info
        Debug.log(('start traffic tests'), self._default_log_level)
        port_handle     = kvargs.get('port_handle', False)
        #port_handle    = ['port1', 'port2']
        port_info       = kvargs.get('port_info', False)
        set_method      = inspect.stack()[0][3]
        is_ipv6         = bool(kvargs.get('is_ipv6', False))
        for port in port_handle:
            p_info                        = port_info[port]
            config                        = p_info['traffic_config']
            # We don't need to populate these variables as of now.
            # IPv6 transit traffic specific not needed by current tests.
            '''
            stream_var                    = Db.traffic_dict[port]['streamblock_variables'].copy()
            is_tagged                     = p_info['port_config']['is_tagged']
            if stream_var['l3_protocol'] == 'ipv6':
                if 'ip_id' in stream_var:
                    del stream_var['ip_id']
                if 'ip_src_addr' in stream_var:
                    del stream_var['ip_src_addr']
                if 'ip_dst_addr' in stream_var:
                    del stream_var['ip_dst_addr']
                if 'ip_ttl' in stream_var:
                    del stream_var['ip_ttl']
                if 'ip_hdr_length' in stream_var:
                    del stream_var['ip_hdr_length']
                if 'ip_protocol' in stream_var:
                    del stream_var['ip_protocol']
                if 'ip_fragment_offset' in stream_var:
                    del stream_var['ip_fragment_offset']
                if 'ip_mbz' in stream_var:
                    del stream_var['ip_mbz']
                if 'ip_tos_field' in stream_var:
                    del stream_var['ip_tos_field']
                if 'ip_precedence' in stream_var:
                    del stream_var['ip_precedence']
                if 'mac_discovery_gw' in stream_var:
                    del stream_var['mac_discovery_gw']

                stream_var['ether_type']            = '86DD'
                stream_var['ipv6_dst_addr']         = str(config['ipv6_dst_addr'])
                stream_var['ipv6_src_addr']         = str(config['ipv6_src_addr'])
                stream_var['ipv6_traffic_class']    = '0'
                stream_var['ipv6_next_header']      = '59'
                stream_var['ipv6_length']           = '0'
                stream_var['ipv6_hop_limit']        = '255'
                stream_var['mac_discovery_gw']      = '00::1'
            else:
                if 'ipv6_dst_addr' in stream_var:
                    del stream_var['ipv6_dst_addr']
                if 'ipv6_src_addr' in stream_var:
                    del stream_var['ipv6_src_addr']
                stream_var['ip_src_addr']       = str(config['ip_src_addr'])
                stream_var['mac_discovery_gw']  = str(config['mac_discovery_gw'])
                stream_var['ip_dst_addr']       = str(config['ip_dst_addr'])

            #update src/dst map/ip
            stream_var['mac_src']   = str(config['mac_src'])
            stream_var['mac_dst']   = str(config['mac_dst'])
            # update vlan-id
            if is_tagged:
                stream_var['vlan_id']       = int(config['vlan_id'])
            if 'tpid' in config:
                #stream_var['vlan_tpid']    = int(config['tpid'], 16)
                stream_var['vlan_tpid']    = int(config['tpid'])
            else:
                if 'vlan_id' in stream_var:
                    del stream_var['vlan_id']
                if 'vlan_tpid' in stream_var:
                    del stream_var['vlan_tpid']
            Debug.log(("[{0}] stream_block {1}".format(set_method,
                        stream_var)), self._default_log_level)
            '''
            # configure stream properties
            Traffic.config_interface(port=port)
            # create traffic streams
            Traffic.create_streamblock(port_info=p_info, port=port)
        result = Traffic.traffic_check(port_list=port_handle, port_info=port_info)
        Debug.log(("[{0}] traffic result {1}".format(set_method,result)), self._default_log_level)
        return result

    def intialize_ports (self, **kwargs):
        """
        Load config from yml data files, robot files and traffic setup
        and build testcase global dictionary. There are two ways to build
        this dictionary. Either specify the ports 'r0-rt0-N' etc explictly
        or in a loop assign these varaibles.
        """
        Debug.log("Intializing Dictionaries")

        # clear the test port dictionary
        self._port_info.clear()

        port_config_dict    = Db.get_port_config_dict()

        # We hardcode that this suite will need 3 ports.
        # port1 and port2 will belong to R0 and port3 wil
        # belong to R1.
        index = 1
        for index in range(1, self._MAX_PORTS + 1):
            ''' Different test cases may need different ports
                First two ports would be on R0 and the rest on
                R1.
            '''
            if (index <= self._MAX_PORTS_R0):
                port = 'r0-rt0-' + str(index)
            else:
                port = 'r1-rt0-' + str(index - self._MAX_PORTS_R0)

            # port = 'r[0-N]-[rt|r][0-N]' and port handle = 'port[0-N]'
            # copy the config from port config dict in the config
            # block of test port dict. This port config is coming from
            # port_config.yml data file.
            network_port = Db.get_network_port(port)
            traffic_port = Db.get_traffic_port(port)

            # port_handle is just port1, port2 string. This can be derived from
            # a suite specific [port=>port_handle] map table instead of taking
            # from HTL class
            #port_handle  = HLT.get_port_handle(port)

            ''' copy the config block from port config dict to test dict '''
            port_info = {}
            port_info['port_config']    = {}
            port_info['traffic_config'] = {}
            port_config_key = 'port' + str(index)

            # copy stream config from traffic_config.yml file
            port_info['traffic_config'] = port_config_dict[port_config_key].copy()

            port_info['port_config']['port']    = network_port
            port_info['port_config']['is_lag']  = False
            unit = 0

            logical_port = str(port_info['port_config']['port']) +'.'+ str(unit)
            port_info['port_config']['logical1'] = logical_port
            Debug.log("port map {0} <=> {1} <=> {2} <=> {3}".format(
                      port, traffic_port, network_port, port_config_key))
            self._port_info[port] = port_info
            index = index + 1

        return self._port_info

    def update_testcase_config (self, **kwargs):
        """
        Load config from yml data files, robot files and traffic setup
        and build testcase global dictionary. There are two ways to build
        this dictionary. Either specify the ports 'r0-rt0-N' etc explictly
        or in a loop assign these varaibles.
        """
        Debug.log("update Test Case Configuration")
        cfg_list = kwargs.get('args', None)
        if not cfg_list:
            raise AssertionError("Please give the cfg_list for which you need to configure the vlan \n")

        # clear the test port dictionary
        #self._port_info.clear()

        # create a test port dictionary network port dict based on the max
        # number of ports required for this testcase. Assign the config to the
        # ports explictly. The test dictionary value will change from test
        # to test but we should not modify network_dict and port_config_dict
        index = 1
        for cfg in cfg_list:
            ''' Different test cases may need different ports
                First two ports would be on R0 and the rest on
                R1.
            '''
            if (index <= 2):
                port = 'r0-rt0-' + str(index)
            else:
                port = 'r1-rt0-' + str(index-2)

            # port = 'r[0-N]-[rt|r][0-N]' and port handle = 'port[0-N]'
            # copy the config from port config dict in the config
            # block of test port dict. This port config is coming from
            # port_config.yml data file.
            network_port = Db.get_network_port(port)
            traffic_port = Db.get_traffic_port(port)

            # Update parameter that are specifically passed by the testcase.
            #
            if ('is_lag' in cfg) and (cfg['is_lag'] == True):
                self._port_info[port]['port_config']['port'] = 'ae0'
                self._port_info[port]['port_config']['child1']  = network_port
                self._port_info[port]['port_config']['is_lag']  = True
            else:
                self._port_info[port]['port_config']['port']    = network_port
                self._port_info[port]['port_config']['is_lag']  = False

            if 'vlan' in cfg:
                self._port_info[port]['port_config']['vlan']    = cfg['vlan']
            else:
                self._port_info[port]['port_config']['vlan']    = 'vtest'

            if 'vlan_id' in cfg:
                self._port_info[port]['port_config']['vlan_id'] = cfg['vlan_id']
            else:
                self._port_info[port]['port_config']['vlan_id'] = 100

            if 'mode' in cfg:
                self._port_info[port]['port_config']['mode']    = cfg['mode']
            else:
                self._port_info[port]['port_config']['mode']    = 'access'

            if 'is_nvid' in cfg:
                self._port_info[port]['port_config']['is_nvid'] = bool(cfg['is_nvid'])
            else:
                self._port_info[port]['port_config']['is_nvid'] = False

            if ('is_tagged' in cfg) and (str(cfg['is_tagged']) == 'True'):
                self._port_info[port]['port_config']['is_tagged']	= True
            else:
                self._port_info[port]['port_config']['is_tagged']   = False

            if 'is_sp' in cfg:
                if cfg[is_sp] == False:
                    unit = 0
                else:
                    unit = self._port_info[port]['port_config']['vlan_id']
            unit = 0

            logical_port = str(self._port_info[port]['port_config']['port']) +'.'+ str(unit)
            self._port_info[port]['port_config']['logical1'] = logical_port
            index = index + 1

        return self._port_info


    def start_test (self, **kwargs):

        port_info   = kwargs.get('port_info', False)
        port_handle = kwargs.get('port_handle', False)
        test        = str(kwargs.get('test'))

        if test == 'flood_untagged':
            is_flood    = True
            is_tagged   = False
        elif test == 'flood_tagged':
            is_flood    = True
            is_tagged   = True
        elif test == 'forward_untagged':
            is_flood    = False
            is_tagged   = False
        elif test == 'forward_tagged':
            is_flood    = False
            is_tagged   = True
        else:
            Debug.log(("invalid test"), 'WARN')

        port1 = Db.gl('r0','rt0',1)
        port2 = Db.gl('r0','rt0',2)
        port3 = Db.gl('r1','rt0',1)
        port_info[port3]['port_config']['is_tagged']    = is_tagged
        port_info[port2]['port_config']['is_tagged']    = is_tagged
        port_info[port1]['port_config']['is_tagged']    = is_tagged
        port_info[port3]['port_config']['is_flood']     = is_flood
        port_info[port2]['port_config']['is_flood']     = is_flood
        port_info[port1]['port_config']['is_flood']     = is_flood

        port_list = [port1, port2, port3]

        result = self.start_traffic(port_info=port_info, port_handle=port_handle)

        self._traffic_utils.l2_verify_packet_count(test=test, traffic_result=result, port_list=port_handle)


    def configure_bgp_protocol (self, **kwargs):
        debug           = kwargs.get('debug', False)
        device = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        port_info       = kwargs.get('port_info', {})
        misc_config     = kwargs.get('misc_config', [])
        if not device:
            raise AssertionError("Please give the device for which you need to configure the vlan \n")

        for conf_lines in misc_config:
            Device.config(cmd=conf_lines, handle=device)

    # commit the configuration
        Device.commit(handle=device)

    def config_ospf(self, **kwargs):
        """
        This Function Configures OSPF between two devices R0 and R1
        in this case
        """
        port_info = self.update_testcase_config(**kwargs)
        port1 = Db.gl('r0','rt0',1)
        port3 = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        misc_config = []
        Debug.log('[step #2] !!!!!!!!!!!  OSPF CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring OSPF on Device 1')
        del misc_config[:]
        misc_config.append('delete protocols')
        misc_config.append('set protocols ospf area 0.0.0.0 interface ' + self.interface_list_1[0] )
        misc_config.append('set protocols ospf area 0.0.0.0 interface lo0 passive')
        misc_config.append('set protocols ospf export adv-route')
        misc_config.append('set protocols ospf area 0.0.0.0 interface ' + r0_spt_port['port_config']['port'] + ' passive')
        misc_config.append('set protocols ospf3 export adv-route')
        misc_config.append('set protocols ospf3 import reject-route')
        misc_config.append('set protocols ospf3 area 0 interface ' + self.interface_list_1[0])
        self.configure_misc_config (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring OSPF on Device 2')
        del misc_config[:]
        misc_config.append('set protocols ospf3 export adv-route')
        misc_config.append('set protocols ospf3 import reject-route')
        misc_config.append('set protocols ospf3 area 0 interface ' + self.interface_list_2[0] )
        misc_config.append('set protocols ospf area 0.0.0.0 interface ' + self.interface_list_2[0] )
        misc_config.append('set protocols ospf export adv-route')
        misc_config.append('set protocols ospf import reject-route')
        misc_config.append('set protocols ospf area 0.0.0.0 interface lo0 passive')
        misc_config.append('set protocols ospf area 0.0.0.0 interface ' + r1_spt_port['port_config']['port'] + ' passive')
        self.configure_misc_config (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  OSFP CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')

        time.sleep(60)


    ######## First routine to be called in irb over ae segment ######################
    # Will also call routine to setup Base irb over ae config.
    #################################################################################
    def test_ae_l3_dual_stack (self, **kwargs):
        misc_config = []
        test            = kwargs.get('test', None)

        # Call to setup base irb over ae config
        Debug.log(('[step #1] Setp Base irb over ae config'), 'INFO')
        self.setup_irb_over_ae_config(**kwargs)

        Debug.log(('[step #2] Populate port config'), 'INFO')
        port_info = self.update_testcase_config(**kwargs)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1 = Db.gl('r0','rt0',1)
        port3 = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]

        Debug.log('[step #3] !!!!!!!!! Testing L3 dual Stack on ae  !!!!!!!!!')
        Debug.log('Configuring Device 1')
        del misc_config[:]
        misc_config.append('set protocols ospf export adv-route')
        misc_config.append('set protocols ospf import reject-route')
        misc_config.append('set protocols ospf area 0 interface irb.200')
        '''
            misc_config.append('set routing-options rib inet6.0 static route ::/0 next-hop ::50.50.50.1')
        '''
        misc_config.append('set protocols ospf3 export adv-route')
        misc_config.append('set protocols ospf3 import reject-route')
        misc_config.append('set protocols ospf3 area 0 interface irb.200')
        self.configure_l3_interface (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring Device 2')
        del misc_config[:]
        '''
        misc_config.append('set routing-options rib inet6.0 static route ::/0 next-hop ::50.50.50.2')
        '''
        misc_config.append('set protocols ospf3 export adv-route')
        misc_config.append('set protocols ospf3 import reject-route')
        misc_config.append('set protocols ospf3 area 0 interface ae1')
        misc_config.append('set protocols ospf export adv-route')
        misc_config.append('set protocols ospf import reject-route')
        misc_config.append('set protocols ospf area 0 interface ae1')
        self.configure_l3_interface (device=self.R1, misc_config=misc_config)
        time.sleep(60)
        # Verify if the ae is UP or not before proceeding. Sending is_static to skip lacp check.
        Debug.log(('Verify ae status'), 'INFO')
        Lag.check_lag_is_up(device=self.R0 , ae_name='ae1', is_static=True);

        Debug.log(('Verify ae status'), 'INFO')
        Lag.check_lag_is_up(device=self.R1 , ae_name='ae1', is_static=True);

        #Verify if OSPF is UP or not
        Debug.log(('Verify OSPF status'), 'INFO')
        self._l3_infra.verify_ospf_protocol(device=self.R0,                \
                                verif_nbr_addr    = '50.50.50.1',         \
                                verif_dest_nh_ip  = '50.50.50.1',         \
                                verif_intf        = 'irb.200',    \
                                verif_protocol    = 'ospf',     \
                                verif_route_addr  = '100.100.100.2/32')
        # Test IPv4 traffic
        #
        mac = Utils.get_dut_mac_address(device=self.R0, port=str(r0_spt_port['port_config']['port']))
        #Update port specific parameters on both ports based on current config
        r0_spt_port['traffic_config']['ip_src_addr']      = '90.90.90.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '90.90.90.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '80.80.80.2'
        r0_spt_port['traffic_config']['mac_dst']          =  mac
        r0_spt_port['traffic_config']['l3_protocol']	  =  'ipv4'
        mac = Utils.get_dut_mac_address(device=self.R1, port=str(r1_spt_port['port_config']['port']))
        r1_spt_port['traffic_config']['ip_src_addr']      = '80.80.80.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '80.80.80.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '90.90.90.2'
        r1_spt_port['traffic_config']['mac_dst']          = mac
        r1_spt_port['traffic_config']['l3_protocol']      =  'ipv4'
        port_handle     = [port1, port3]
       #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        # start l2 traffic test
        #Debug.set_debug('True')
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

        # Test IPv6 traffic
        #
        Debug.log('[step #3] !!!!!!!!! Testing ipv6 dual Stack on ae  !!!!!!!!!')
        '''
        r0_spt_port['traffic_config']['ipv6_src_addr']      = '00::90:90:90:2'
        r0_spt_port['traffic_config']['ipv6_dst_addr']      = '00::80:80:80:2'
        r0_spt_port['traffic_config']['mac_dst']          =  mac
        r0_spt_port['traffic_config']['l3_protocol']      =  'ipv6'

        r1_spt_port['traffic_config']['ipv6_src_addr']      = '00::80:80:80:2'
        r1_spt_port['traffic_config']['ipv6_dst_addr']      = '00::90:90:90:2'
        r1_spt_port['traffic_config']['mac_dst']          =  mac
        r1_spt_port['traffic_config']['l3_protocol']      =  'ipv6'
        '''

        Debug.log('Checking ping to peer ip ::50.50.50.1')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='::50.50.50.1'))
        if ping_successful:
            Debug.log('Execute ping to  ::50.50.50.1/112  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('Checking ping to peer lo0 abcd::128:102:185:236')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='abcd::128:102:185:236'))
        if ping_successful:
            Debug.log('Execute ping to  abcd::128:102:185:236/128 successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('\n*********************************')
        Debug.log('         IPV6 TEST PASSED')
        Debug.log('*********************************')
        #self.start_test(port_info=port_info, port_handle=port_handle)

    def test_rip_protocol_irb_over_ae (self, **kwargs):
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = kwargs.get('test', None)
        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port_info = self.update_testcase_config(**kwargs)
        port1 = Db.gl('r0','rt0',1)
        port3 = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        port_handle     = [port1, port3]
        misc_config = [];
        Debug.log('[step #1] Populate port config')

        Debug.log('[step #2] !!!!!!!!!!!  RIP CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring RIP on Device 1')
        del misc_config[:]
        misc_config.append('delete protocols')
        misc_config.append('set protocols rip group group1 neighbor irb.200')
        misc_config.append('set protocols rip group group1 export adv-route')
        misc_config.append('set protocols rip group group1 import reject-route')
        self.configure_misc_config (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring RIP on Device 2')
        del misc_config[:]
        misc_config.append('set protocols rip group group1 neighbor ae1.0')
        misc_config.append('set protocols rip group group1 export adv-route')
        misc_config.append('set protocols rip group group1 import reject-route')
        self.configure_misc_config (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  RIP CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')

        time.sleep(30)
        Debug.log('[step #3] !!!!!!!!!!!  VERIFY RIP PROTOCOL  !!!!!!!!!!!!!!!!!')
        self._l3_infra.verify_rip_protocol(device=self.R0, \
                                verif_interface = 'irb.200', \
                                verif_local_addr = '50.50.50.2', \
                                verif_nh_ip = '50.50.50.1', \
                                verif_route_addr = '100.100.100.2/32')
        mac = Utils.get_dut_mac_address(device=self.R0, port=str(r0_spt_port['port_config']['port']))
        #Update port specific parameters on both ports based on current config
        r0_spt_port['traffic_config']['ip_src_addr']      = '90.90.90.2'
        r0_spt_port['traffic_config']['mac_discovery_gw'] = '90.90.90.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '80.80.80.2'
        r0_spt_port['traffic_config']['mac_dst']          =  mac

        mac = Utils.get_dut_mac_address(device=self.R1, port=str(r1_spt_port['port_config']['port']))
        r1_spt_port['traffic_config']['ip_src_addr']      = '80.80.80.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '80.80.80.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '90.90.90.2'
        r1_spt_port['traffic_config']['mac_dst']          = mac
        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

    def test_bgp_protocol_irb_over_ae (self, **kwargs):
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = str(kwargs.get('test', False))
        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port_info = self.update_testcase_config(**kwargs)
        port1 = Db.gl('r0','rt0',1)
        port3 = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        port_handle     = [port1, port3]
        misc_config = [];
        Debug.set_debug(debug);
        Debug.log(('[step #1] Populate port config'), 'INFO')


        Debug.log(('[step #2] !!!!!!!!!!!  BGP CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!'), 'INFO')
        Debug.log(('Configuring Device 1'), 'INFO')
        '''
        BGP set commands for R0
        '''
        del misc_config[:]
        misc_config.append('delete protocols')
        misc_config.append('set protocols bgp group ibgp neighbor 50.50.50.1 peer-as 100')
        misc_config.append('set protocols bgp local-address 50.50.50.2')
        misc_config.append('set protocols bgp group ibgp export adv-route')
        misc_config.append('set protocols bgp group ibgp import reject-route')
        self.configure_bgp_protocol (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring Device 2')
        '''
        BGP set commands for R1
        '''
        del misc_config[:]
        misc_config.append('delete protocols')
        misc_config.append('set protocols bgp group ibgp neighbor 50.50.50.2 peer-as 100')
        misc_config.append('set protocols bgp local-address 50.50.50.1')
        misc_config.append('set protocols bgp group ibgp export adv-route')
        misc_config.append('set protocols bgp group ibgp import reject-route')
        self.configure_bgp_protocol (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  BGP CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')

        time.sleep(30)
        Debug.log('[step #3] !!!!!!!!!!!  VERIFY BGP PROTOCOL  !!!!!!!!!!!!!!!!!')
        self._l3_infra.verify_bgp_protocol(device=self.R0, \
                                verif_peerid    = '50.50.50.1', \
                                verif_local_id  = '50.50.50.2', \
                                verif_peer_as   = '100', \
                                verif_local_as  = '100', \
                                verif_dest_nh_ip = '50.50.50.1', \
                                verif_intf       = 'irb.200', \
                                verif_route_addr = '100.100.100.2/32')

        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=port_info[port1]['port_config']['port'])
        r0_spt_port['traffic_config']['ip_src_addr']      = '90.90.90.2'
        r0_spt_port['traffic_config']['mac_discovery_gw'] = '90.90.90.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '80.80.80.2'
        r0_spt_port['traffic_config']['mac_dst']          =  mac

        mac = Utils.get_dut_mac_address(device=self.R1, port=str(r1_spt_port['port_config']['port']))
        r1_spt_port['traffic_config']['ip_src_addr']      = '80.80.80.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '80.80.80.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '90.90.90.2'
        r1_spt_port['traffic_config']['mac_dst']          = mac

        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

    def test_ospf_protocol_irb_over_ae (self, **kwargs):
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = str(kwargs.get('test', False))

        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port_info = self.update_testcase_config(**kwargs)

        port1       = Db.gl('r0','rt0',1)
        port3       = Db.gl('r1','rt0',1)
        r0_spt_port = port_info[port1]
        r1_spt_port = port_info[port3]
        port_handle = [port1, port3]

        misc_config = [];
        Debug.set_debug(debug);
        Debug.log(('[step #1] Populate port config'), 'INFO')

        Debug.log('[step #2] !!!!!!!!!!!  OSPF CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring OSPF on Device 1')
        del misc_config[:]
        misc_config.append('delete protocols')
        misc_config.append('set protocols ospf area 0.0.0.0 interface irb.200')
        misc_config.append('set protocols ospf area 0.0.0.0 interface lo0 passive')
        misc_config.append('set protocols ospf area 0.0.0.0 interface ' + r0_spt_port['port_config']['port'] + ' passive')
        misc_config.append('set protocols ospf3 export adv-route')
        misc_config.append('set protocols ospf3 import  reject-route')
        misc_config.append('set protocols ospf3 area 0 interface irb.200')
        self.configure_misc_config (device=self.R0, misc_config=misc_config)
        Debug.log('Configuring OSPF on Device 2')
        del misc_config[:]
        misc_config.append('set protocols ospf3 export adv-route')
        misc_config.append('set protocols ospf3 import reject-route')
        misc_config.append('set protocols ospf3 area 0 interface ae1.0')
        misc_config.append('set protocols ospf area 0.0.0.0 interface ae1.0')
        misc_config.append('set protocols ospf area 0.0.0.0 interface lo0 passive')
        misc_config.append('set protocols ospf area 0.0.0.0 interface ' + r1_spt_port['port_config']['port'] + ' passive')
        self.configure_misc_config (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  OSFP CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')
        time.sleep(60)
        Debug.log('[step #3] !!!!!!!!!!!  VERIFY OSPF PROTOCOL  !!!!!!!!!!!!!!!!!')
        verif_nbr_addr          = str(kwargs.get('verif_nbr_addr', None))
        verif_intf              = str(kwargs.get('verif_intf', None))
        verif_dest_nh_ip        = str(kwargs.get('verif_dest_nh_ip', None))
        verif_route_addr        = str(kwargs.get('verif_route_addr', None))
        self._l3_infra.verify_ospf_protocol(device=self.R0,                \
                                verif_nbr_addr    = '50.50.50.1',         \
                                verif_dest_nh_ip  = '50.50.50.1',         \
                                verif_intf        = 'irb.200',    \
                                verif_protocol    = 'ospf',	\
                                verif_route_addr  = '100.100.100.2/32')

        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=str(r0_spt_port['port_config']['port']))
        r0_spt_port['traffic_config']['ip_src_addr']      = '90.90.90.2'
        r0_spt_port['traffic_config']['mac_discovery_gw'] = '90.90.90.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '80.80.80.2'
        r0_spt_port['traffic_config']['mac_dst']          =  mac

        mac = Utils.get_dut_mac_address(device=self.R1, port=str(r1_spt_port['port_config']['port']))
        r1_spt_port['traffic_config']['ip_src_addr']      = '80.80.80.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '80.80.80.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '90.90.90.2'
        r1_spt_port['traffic_config']['mac_dst']          = mac

       #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

        # Test IPv6 traffic
        Debug.log('[step #3] !!!!!!!!! Testing ipv6 traffic  !!!!!!!!!')

        Debug.log('Checking ping to peer ip ::50.50.50.1')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='::50.50.50.1'))
        if ping_successful:
            Debug.log('Execute ping to  ::50.50.50.1/112  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('Checking ping to peer lo0 abcd::128:102:185:236')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='abcd::128:102:185:236'))
        if ping_successful:
            Debug.log('Execute ping to  abcd::128:102:185:236/128 successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('\n*********************************')
        Debug.log('         IPV6 TEST PASSED')
        Debug.log('*********************************')

    def test_isis_protocol_irb_over_ae (self, **kwargs):
        #remove this after testing
        #self.setup_irb_over_ae_config(**kwargs)
        #
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = str(kwargs.get('test', False))

        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)

        port_info = self.update_testcase_config(**kwargs)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1       = Db.gl('r0','rt0',1)
        port3       = Db.gl('r1','rt0',1)
        r0_spt_port = port_info[port1]
        r1_spt_port = port_info[port3]
        port_handle = [port1, port3]

        misc_config = [];
        Debug.set_debug(debug);
        Debug.log(('[step #1] Populate port config'), 'INFO')


        Debug.log('[step #2] !!!!!!!!!!!  ISIS CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring ISIS on Device 1')
        del misc_config[:]
        misc_config.append('delete protocols')
        misc_config.append('set interfaces lo0 unit 0 family iso address 47.0005.80ff.f800.0000.0108.0001.1280.9204.0116.00')
        misc_config.append('set interfaces irb.200 family iso')
        misc_config.append('set interfaces ' + r0_spt_port['port_config']['port'] + '  unit 0 family iso')
        misc_config.append('set protocols isis interface lo0')
        misc_config.append('set protocols isis interface irb.200')
        misc_config.append('set protocols isis interface ' + r0_spt_port['port_config']['port'])
        self.configure_misc_config (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring ISIS on Device 2')
        del misc_config[:]
        misc_config.append('delete protocols')
        misc_config.append('set interfaces lo0 unit 0 family iso address 47.0005.80ff.f800.0000.0108.0001.1280.9204.0118.00')
        misc_config.append('set interfaces ae1 unit 0 family iso')
        misc_config.append('set interfaces ' + r1_spt_port['port_config']['port'] + '  unit 0 family iso')
        misc_config.append('set protocols isis interface ae1.0')
        misc_config.append('set protocols isis interface lo0')
        misc_config.append('set protocols isis interface ' + r1_spt_port['port_config']['port'])

        self.configure_misc_config (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  ISIS CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')

        #Adding additional delay for vQFX
        if (Utils.get_product_model == 'vqfx-10000'):
           time.sleep(45)
        else:
            time.sleep(30)

        # For local-area network (LAN) connection SNPA is the MAC address of the interface
        # on the peer device. We will validate it as a part of IS-IS adjacency
        snpa = Utils.get_dut_mac_address(device=self.R1, port='ae1')

        self._l3_infra.verify_isis_protocol(device=self.R0,                \
                                verif_dest_nh_ip  = '50.50.50.1',         \
                                verif_intf        = 'irb.200',    \
                                verif_protocol    = 'isis',     \
                                verif_snpa	  = snpa,	\
                                verif_route_addr  = '100.100.100.2/32')
        # Test IPv4 traffic
        #
        Debug.log('Checking ping to peer lo0 ip 100.100.100.2')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='100.100.100.2'))
        if ping_successful:
            Debug.log('Execute ping to  100.100.100.2/32  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('Checking ping to peer ip 80.80.80.1')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='80.80.80.1'))
        if ping_successful:
            Debug.log('Execute ping to  80.80.80.1  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=str(r0_spt_port['port_config']['port']))
        r0_spt_port['traffic_config']['ip_src_addr']      = '90.90.90.2'
        r0_spt_port['traffic_config']['mac_discovery_gw'] = '90.90.90.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '80.80.80.2'
        r0_spt_port['traffic_config']['mac_dst']          =  mac

        mac = Utils.get_dut_mac_address(device=self.R1, port=str(r1_spt_port['port_config']['port']))
        r1_spt_port['traffic_config']['ip_src_addr']      = '80.80.80.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '80.80.80.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '90.90.90.2'
        r1_spt_port['traffic_config']['mac_dst']          = mac

       #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                              port_list=port_list,
                                              chk_port_list=chk_port_list,
                                              verify_rewrite=False)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                      test=test,
                                                      port_info=port_info,
                                                      port_list=port_list,
                                                      chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

        # Test IPv6 traffic
        Debug.log('[step #3] !!!!!!!!! Testing ipv6 traffic  !!!!!!!!!')

        Debug.log('Checking ping to peer ip ::50.50.50.1')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='::50.50.50.1'))
        if ping_successful:
            Debug.log('Execute ping to  ::50.50.50.1/112  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('Checking ping to peer lo0 abcd::128:102:185:236')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='abcd::128:102:185:236'))
        if ping_successful:
            Debug.log('Execute ping to  abcd::128:102:185:236/128 successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('\n*********************************')
        Debug.log('         IPV6 TEST PASSED')
        Debug.log('*********************************')

    def test_irb_traffic_sanity (self, **kwargs):
        misc_config = []
        test            = kwargs.get('test', None)
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)

        Debug.log('[step #1] Populate port config')
        port_info = self.update_testcase_config(**kwargs);
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1     = Db.gl('r0','rt0',1)
        port2     = Db.gl('r0','rt0',2)
        r0_spt_port_1     = port_info[port1]
        r0_spt_port_2     = port_info[port2]

        Debug.log('[step #2] !!!!!!!!! Testing IRB traffic Across Access Ports  !!!!!!!!!')
        Debug.log('Configuring Device 1')
        del misc_config[:]
        misc_config.append('delete interfaces '+ r0_spt_port_1['port_config']['port'])
        misc_config.append('set interfaces ' + r0_spt_port_1['port_config']['port'] + '  unit 0 family ethernet-switching interface-mode access vlan members VLAN300')
        misc_config.append('set interfaces irb unit 300 family inet address 80.80.80.1/24 ')

        misc_config.append('set interfaces irb.300 family inet address 80.80.80.1/24 arp 80.80.80.2 l2-interface ' + \
                                str(r0_spt_port_1['port_config']['port']) + ' mac ' + \
                                str(r0_spt_port_1['traffic_config']['mac_src']))
        misc_config.append('set vlans VLAN300 l3-interface irb.300')
        misc_config.append('set vlans VLAN300 vlan-id 300')
        misc_config.append('delete interfaces ' + r0_spt_port_2['port_config']['port'])
        misc_config.append('set interfaces ' + r0_spt_port_2['port_config']['port'] + '  unit 0 family ethernet-switching interface-mode access vlan members VLAN400')
        misc_config.append('set interfaces irb unit 400 family inet address 200.200.200.1/24')
        misc_config.append('set interfaces irb.400 family inet address 200.200.200.1/24 arp 200.200.200.2 l2-interface ' + \
                                str(r0_spt_port_2['port_config']['port']) + ' mac ' + \
                                str(r0_spt_port_2['traffic_config']['mac_src']))
        misc_config.append('set vlans VLAN400 l3-interface irb.400')
        misc_config.append('set vlans VLAN400 vlan-id 400')
        self.configure_l3_interface (device=self.R0, misc_config=misc_config)
        mac = Utils.get_dut_mac_address(device=self.R0, port='irb')
        #Update port specific parameters on both ports based on current config
        r0_spt_port_1['traffic_config']['ip_src_addr']      = '80.80.80.2'
        r0_spt_port_1['traffic_config']['mac_discovery_gw'] = '80.80.80.1'
        r0_spt_port_1['traffic_config']['ip_dst_addr']      = '200.200.200.2'
        r0_spt_port_1['traffic_config']['mac_dst']          =  mac

        mac = Utils.get_dut_mac_address(device=self.R0, port='irb')
        r0_spt_port_2['traffic_config']['ip_src_addr']          = '200.200.200.2'
        r0_spt_port_2['traffic_config']['mac_discovery_gw']     = '200.200.200.1'
        r0_spt_port_2['traffic_config']['ip_dst_addr']          = '80.80.80.2'
        r0_spt_port_2['traffic_config']['mac_dst']              = mac

        port_handle	= [port1, port2]
        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port2]
        chk_port_list = [port1, port2]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

        Debug.log('[step #2] !!!!!!!!! IRB traffic Across Access Ports Successful !!!!!!!!!')
        Debug.log('[step #3] !!!!!!!!! Testing IRB traffic Across Trunk Ports  !!!!!!!!!')
        del misc_config[:]
        #Update port to be trunk
        misc_config.append('delete interfaces ' + r0_spt_port_1['port_config']['port'])
        misc_config.append('set interfaces ' + r0_spt_port_1['port_config']['port'] + ' unit 0 family ethernet-switching interface-mode trunk vlan members VLAN300')
        misc_config.append('delete interfaces ' + r0_spt_port_2['port_config']['port'])
        misc_config.append('set interfaces ' + r0_spt_port_2['port_config']['port'] + ' unit 0 family ethernet-switching interface-mode trunk vlan members VLAN400')

        self.configure_l3_interface (device=self.R0, misc_config=misc_config)
        #Update port_info to indicate that ports are now trunk
        test = 'forward_tagged'
        r0_spt_port_1['port_config']['vlan_id']	= 300
        r0_spt_port_2['port_config']['vlan_id']	= 400
        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list,
                                         verify_rewrite=False)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise



    '''
        Rotine to configure base irb over ae interface
    '''
    def setup_irb_over_ae_config (self, **kwargs):
        Debug.log(('[step #1] Cleanup config from non irb testcases'), self._default_log_level)
        Device.clean_config(handle=self.R0)
        Device.clean_config(handle=self.R1)

        misc_config = []
        Debug.log('[step #2] Populate port config')
        port_info = self.update_testcase_config(**kwargs)
        num_child = 2

        port1       = Db.gl('r0','rt0',1)
        port3       = Db.gl('r1','rt0',1)
        r0_spt_port = port_info[port1]
        r1_spt_port = port_info[port3]

        Debug.log(('[step #3] !!!!!!!!! Configuring irb over ae  !!!!!!!!!'), self._default_log_level)
        Debug.log(('Configuring Device 1'), self._default_log_level)

        # set ports to be part of ae
        for x in range(0, num_child):
            if Utils.is_junos_cli(handle=self.R0):
                misc_config.append('set interfaces ' + self.interface_list_1[x] + ' gigether-options 802.3ad ae1')
            else:
                misc_config.append('set interfaces ' + self.interface_list_1[x] + ' ether-options 802.3ad ae1')

        misc_config.append('set interfaces lo0 unit 0 family inet address 100.100.100.1/32')
        misc_config.append('set interfaces lo0 unit 0 family inet6 address abcd::128:102:185:235/128')
        misc_config.append('set chassis aggregated-devices ethernet  device-count 2')
        misc_config.append('set interfaces ' + str(r0_spt_port['port_config']['port']) + ' unit 0 family inet address ' + '90.90.90.1/24')
        misc_config.append('set interfaces ' + str(r0_spt_port['port_config']['port']) + ' unit 0 family inet6 address ' + '::90.90.90.1/112')
        misc_config.append('set interfaces ' + str(r0_spt_port['port_config']['port']) + ' unit 0 family inet address ' + '90.90.90.1/24 ' \
                                'arp 90.90.90.2 mac ' + str(r0_spt_port['traffic_config']['mac_src']))
        misc_config.append('set interfaces ' + str(r0_spt_port['port_config']['port']) + ' unit 0 family inet6 address \
                                ::90.90.90.1/112 arp ::90.90.90.2 l2-interface ' + \
                                str(r0_spt_port['port_config']['port']) + ' mac ' + \
                                str(r0_spt_port['traffic_config']['mac_src']))
        misc_config.append('set interfaces ae1 unit 0 family ethernet-switching  interface-mode access vlan members VLAN200')
        misc_config.append('set interfaces irb unit 200  family inet address 50.50.50.2/24')
        misc_config.append('set vlans VLAN200 l3-interface irb.200')
        misc_config.append('set vlans  VLAN200 vlan-id 200')

        misc_config.append('set interfaces irb unit 200  family inet6 address ::50.50.50.2/112')
        misc_config.append('set policy-options policy-statement adv-route term 1 from protocol direct')
        misc_config.append('set policy-options policy-statement adv-route term 1 then accept')
        misc_config.append('set policy-options policy-statement reject-route term 1 from route-filter 10.0.0.0/8 orlonger')
        misc_config.append('set policy-options policy-statement reject-route term 1 then reject')
        misc_config.append('set routing-options router-id 50.50.50.2')
        misc_config.append('set routing-options autonomous-system 100')
        self.configure_l3_interface (device=self.R0, misc_config=misc_config)

        del misc_config[:]
        misc_config.append('set interfaces lo0 unit 0 family inet address 100.100.100.2/32')
        misc_config.append('set interfaces lo0 unit 0 family inet6 address abcd::128:102:185:236/128')
        # set ports to be part of ae
        for x in range(0, num_child):
            if Utils.is_junos_cli(handle=self.R1):
                misc_config.append('set interfaces ' + self.interface_list_2[x] + ' gigether-options 802.3ad ae1')
            else:
                misc_config.append('set interfaces ' + self.interface_list_2[x] + ' ether-options 802.3ad ae1')

        misc_config.append('set chassis aggregated-devices ethernet device-count 2')
        misc_config.append('set interfaces ' + r1_spt_port['port_config']['port'] + ' unit 0 family inet address ' + '80.80.80.1/24')
        misc_config.append('set interfaces ' + r1_spt_port['port_config']['port'] + ' unit 0 family inet6 address ' + '::80.80.80.1/112')
        misc_config.append('set interfaces ' + r1_spt_port['port_config']['port'] + ' unit 0 family inet address ' + '80.80.80.1/24 ' \
                                'arp 80.80.80.2 mac ' + str(r1_spt_port['traffic_config']['mac_src']))
        misc_config.append('set interfaces ' + str(r1_spt_port['port_config']['port']) + ' unit 0 family inet6 address \
                                ::80.80.80.1/112 arp ::80.80.80.2 l2-interface ' + \
                                str(r1_spt_port['port_config']['port']) + ' mac ' + \
                                str(r1_spt_port['traffic_config']['mac_src']))
        misc_config.append('set interfaces ae1 unit 0 family inet address 50.50.50.1/24')
        misc_config.append('set interfaces ae1 unit 0 family inet6 address ::50.50.50.1/112')
        misc_config.append('set policy-options policy-statement adv-route term 1 from protocol direct')
        misc_config.append('set policy-options policy-statement adv-route term 1 then accept')
        misc_config.append('set policy-options policy-statement reject-route term 1 from route-filter 10.0.0.0/8 orlonger')
        misc_config.append('set policy-options policy-statement reject-route term 1 then reject')

        misc_config.append('set routing-options router-id 50.50.50.1')
        misc_config.append('set routing-options autonomous-system 100')
        self.configure_l3_interface (device=self.R1, misc_config=misc_config)
        time.sleep(20)

    #######################################################################################
    #                               BASIC L3 TESTCASES
    #######################################################################################
    def setup_l3_ports(self, **kwargs):
        misc_config = [];
        port_info   = kwargs.get('port_info', None)
        Debug.log('Configuring Device 1')
        port1       = Db.gl('r0','rt0',1)
        port3       = Db.gl('r1','rt0',1)
        r0_spt_port = port_info[port1]
        r1_spt_port = port_info[port3]

        del misc_config[:]
        misc_config.append('set interfaces lo0 unit 0 family inet address 100.100.100.1/32')
        misc_config.append('set interfaces lo0 unit 0 family inet6 address abcd::128:102:185:235/128')
        misc_config.append('set interfaces ' + self.interface_list_1[0] + ' unit 0 family inet address 50.0.0.1/24')
        misc_config.append('set interfaces ' + self.interface_list_1[0] + ' unit 0 family inet6 address ::50.50.50.2/112')
        misc_config.append('set interfaces ' + r0_spt_port['port_config']['port'] + ' unit 0 family inet address 192.85.1.1/24')
        misc_config.append('set interfaces ' + r0_spt_port['port_config']['port'] + ' unit 0 family inet address 192.85.1.1/24 arp 192.85.1.2 mac 00:10:94:00:00:01')
        misc_config.append('set routing-options static route 100.100.100.2/32 next-hop 50.0.0.2')
        misc_config.append('set routing-options static route 192.85.2.0/24 next-hop 50.0.0.2')
        misc_config.append('set routing-options router-id 50.0.0.1')
        misc_config.append('set routing-options autonomous-system 100')
        misc_config.append('set policy-options policy-statement adv-route term 1 from protocol direct')
        misc_config.append('set policy-options policy-statement adv-route term 1 then accept')
        misc_config.append('set policy-options policy-statement reject-route term 1 from route-filter 10.0.0.0/8 orlonger')
        misc_config.append('set policy-options policy-statement reject-route term 1 then reject')

        # over PTX we have to add this config explicitly
        misc_config.append('set policy-options policy-statement override-ptx-series-default term 1 from protocol bgp')
        misc_config.append('set policy-options policy-statement override-ptx-series-default term 1 then install-to-fib')
        misc_config.append('set routing-options forwarding-table export override-ptx-series-default')

        self.configure_l3_interface (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring Device 2')
        del misc_config[:]
        misc_config.append('set interfaces lo0 unit 0 family inet address 100.100.100.2/32')
        misc_config.append('set interfaces lo0 unit 0 family inet6 address abcd::128:102:185:236/128')
        misc_config.append('set interfaces ' + self.interface_list_2[0] + ' unit 0 family inet address 50.0.0.2/24')
        misc_config.append('set interfaces ' + self.interface_list_2[0] + ' unit 0 family inet6 address ::50.50.50.1/112')
        misc_config.append('set interfaces ' + r1_spt_port['port_config']['port'] + ' unit 0 family inet address 192.85.2.1/24')
        misc_config.append('set interfaces ' + r1_spt_port['port_config']['port'] + ' unit 0 family inet address 192.85.2.1/24 arp 192.85.2.2 mac 00:10:94:00:00:02')
        misc_config.append('set routing-options static route 100.100.100.1/32 next-hop 50.0.0.1')
        misc_config.append('set routing-options static route 192.85.1.0/24 next-hop 50.0.0.1')
        misc_config.append('set routing-options router-id 50.0.0.2')
        misc_config.append('set routing-options autonomous-system 100')
        misc_config.append('set policy-options policy-statement adv-route term 1 from protocol direct')
        misc_config.append('set policy-options policy-statement adv-route term 1 then accept')
        misc_config.append('set policy-options policy-statement reject-route term 1 from route-filter 10.0.0.0/8 orlonger')
        misc_config.append('set policy-options policy-statement reject-route term 1 then reject')

        # over PTX we have to add this config explicitly
        misc_config.append('set policy-options policy-statement override-ptx-series-default term 1 from protocol bgp')
        misc_config.append('set policy-options policy-statement override-ptx-series-default term 1 then install-to-fib')
        misc_config.append('set routing-options forwarding-table export override-ptx-series-default')

        self.configure_l3_interface (device=self.R1, misc_config=misc_config)

    ######## First routine to be called ######################
    # Will also call routine to setup Base L3 config.
    ##########################################################
    def test_basic_l3 (self, **kwargs):
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)

        port_info   = self.update_testcase_config(**kwargs)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        test        = kwargs.get('test', None)
        port1       = Db.gl('r0','rt0',1)
        port3       = Db.gl('r1','rt0',1)
        r0_spt_port = port_info[port1]
        r1_spt_port = port_info[port3]
        port_handle = [port1, port3]

        Debug.log('[step #2] Populate port config')

        Debug.log(' [step #3] VERIFY Default Route')
        Debug.log(' ******************************\n')
        cmd = "show route protocol static"
        Debug.log(("[{0}] show command : {1}".format(set_method, cmd)), self._default_log_level)
        try:
            result_dict = Device.cli_show_cmd_dict(handle=self.R0, cmd=cmd)
        except warnings.warn:
            pass
        verif_intf = str(self.interface_list_1[0]) + '.0'
        self._l3_infra.verify_routing_table(protocol_name='Static', dest_nh_ip='50.0.0.2', egr_intf = verif_intf, \
                        verif_table = 'inet.0', verif_route = '100.100.100.2/32', result_dict=result_dict)
        mac = Utils.get_dut_mac_address(device=self.R0, port=r0_spt_port['port_config']['port'])
        port_info[port1]['traffic_config']['mac_dst']          = mac
        port_info[port1]['traffic_config']['ip_src_addr']      = '192.85.1.2'
        port_info[port1]['traffic_config']['mac_discovery_gw'] = '192.85.1.1'
        port_info[port1]['traffic_config']['ip_dst_addr']      = '192.85.2.2'

        mac = Utils.get_dut_mac_address(device=self.R1, port=r1_spt_port['port_config']['port'])
        port_info[port3]['traffic_config']['mac_dst']          = mac
        port_info[port3]['traffic_config']['ip_src_addr']      = '192.85.2.2'
        port_info[port3]['traffic_config']['mac_discovery_gw'] = '192.85.2.1'
        port_info[port3]['traffic_config']['ip_dst_addr']      = '192.85.1.2'

        #self.start_test(port_info=port_info, port_handle=port_handle, test = test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

    def test_ospf_protocol (self, **kwargs):
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = kwargs.get('test', None)
        port_info = self.update_testcase_config(**kwargs)
        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)

        Debug.log('[step #1] Populate port config')
        self.config_ospf(**kwargs)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1           = Db.gl('r0','rt0',1)
        port3           = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        port_handle     = [port1, port3]

        #Verify if OSPF is UP or not
        Debug.log(('[step #2] Verify OSPF status'), 'INFO')
        self._l3_infra.verify_ospf_protocol(device=self.R0,                \
                                verif_nbr_addr    = '50.0.0.2',         \
                                verif_dest_nh_ip  = '50.0.0.2',         \
                                verif_intf        = str(self.interface_list_1[0])+'.0',    \
                                verif_protocol    = 'ospf',     \
                                verif_route_addr  = '100.100.100.2/32')

        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=r0_spt_port['port_config']['port'])
        r0_spt_port['traffic_config']['mac_dst']          =  mac
        r0_spt_port['traffic_config']['ip_src_addr']      = '192.85.1.2'
        r0_spt_port['traffic_config']['mac_discovery_gw'] = '192.85.1.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '192.85.2.2'

        mac = Utils.get_dut_mac_address(device=self.R1, port=r1_spt_port['port_config']['port'])
        r1_spt_port['traffic_config']['mac_dst']          = mac
        r1_spt_port['traffic_config']['ip_src_addr']      = '192.85.2.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '192.85.2.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '192.85.1.2'

        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise
        # Test IPv6 traffic
        #
        Debug.log('[step #3] Verify OSPFv3 status')

        Debug.log('Checking ping to peer ip ::50.50.50.1')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='::50.50.50.1'))
        if ping_successful:
            Debug.log('Execute ping to  ::50.50.50.1/112  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('Checking ping to peer lo0 abcd::128:102:185:236')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='abcd::128:102:185:236'))
        if ping_successful:
            Debug.log('Execute ping to  abcd::128:102:185:236/128 successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('\n*********************************')
        Debug.log('         IPV6 TEST PASSED')
        Debug.log('*********************************')

    def test_isis_protocol (self, **kwargs):
        Debug.log('[step #1] Set Up base L3 config')
        misc_config = [];
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = kwargs.get('test', None)
        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)

        port_info = self.update_testcase_config(**kwargs)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1           = Db.gl('r0','rt0',1)
        port3           = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        port_handle     = [port1, port3]

        Debug.log('[step #1] Populate port config')

        Debug.log('[step #2] !!!!!!!!!!!  IS-IS CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring Device 1')
        '''
        IS-IS set commands for R0
        '''
        del misc_config[:]
        misc_config.append('set interfaces lo0 unit 0 family iso address 47.0005.80ff.f800.0000.0108.0001.1280.9204.0116.00')
        misc_config.append('set interfaces ' + str(self.interface_list_1[0]) + '.0 family iso')
        misc_config.append('set interfaces ' + r0_spt_port['port_config']['port'] + '  unit 0 family iso')

        misc_config.append('set protocols isis interface lo0 family iso address 47.0005.80ff.f800.0000.0108.0001.1280.9204.0116.00')
        misc_config.append('set protocols isis interface ' + str(self.interface_list_1[0]) + '.0')
        misc_config.append('set protocols isis interface ' + r0_spt_port['port_config']['port'])
        self.configure_misc_config (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring Device 2')
        '''
        IS-IS set commands for R1
        '''
        del misc_config[:]
        misc_config.append('set interfaces lo0 unit 0 family iso address 47.0005.80ff.f800.0000.0108.0001.1280.9204.0118.00')
        misc_config.append('set interfaces ' + str(self.interface_list_2[0]) + '.0 family iso')
        misc_config.append('set interfaces ' + r1_spt_port['port_config']['port'] + '  unit 0 family iso')

        misc_config.append('set protocols isis interface lo0 family iso address 47.0005.80ff.f800.0000.0108.0001.1280.9204.0118.00')
        misc_config.append('set protocols isis interface ' + str(self.interface_list_2[0]) + '.0')
        misc_config.append('set protocols isis interface ' + r1_spt_port['port_config']['port'])
        self.configure_misc_config (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  IS-IS CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')

        #Adding additional delay for vQFX
        if (Utils.get_product_model == 'vqfx-10000'):
            time.sleep(45)
        else:
            time.sleep(30)

        #Verify if IS-IS is UP or not
        Debug.log(('[step #3] Verify IS-IS status'), 'INFO')
        # For local-area network (LAN) connection SNPA is the MAC address of the interface
        # on the peer device. We will validate it as a part of IS-IS adjacency
        snpa = Utils.get_dut_mac_address(device=self.R1, port=str(self.interface_list_2[0]))
        self._l3_infra.verify_isis_protocol(device=self.R0,                \
                                verif_dest_nh_ip  = '50.0.0.2',         \
                                verif_intf        = str(self.interface_list_1[0])+'.0',    \
                                verif_protocol    = 'isis',     \
                                verif_snpa        = snpa,       \
                                verif_route_addr  = '100.100.100.2/32')
        # Test IPv4 traffic
        #
        Debug.log('Checking ping to peer lo0 ip 100.100.100.2')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='100.100.100.2'))
        if ping_successful:
            Debug.log('Execute ping to  100.100.100.2/32  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('Checking ping to peer ip 192.85.2.1')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='192.85.2.1'))
        if ping_successful:
            Debug.log('Execute ping to  192.85.2.1  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        # Test IPv6 traffic
        #
        Debug.log('[step #3] Verify IPv6 traffic')

        Debug.log('Checking ping to peer ip ::50.50.50.1')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='::50.50.50.1'))
        if ping_successful:
            Debug.log('Execute ping to  ::50.50.50.1/112  successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        Debug.log('Checking ping to peer lo0 abcd::128:102:185:236')
        ping_successful = (Utils.check_ping(self.R0, dst_ip='abcd::128:102:185:236'))
        if ping_successful:
            Debug.log('Execute ping to  abcd::128:102:185:236/128 successful')
        else:
            raise AssertionError(" *** Ping Test Failed *** \n")

        # Test end to end IPv4 traffic
        #
        Debug.log('[step #3] Verify End to End IPv4 traffic')
        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=r0_spt_port['port_config']['port'])
        r0_spt_port['traffic_config']['mac_dst']          =  mac
        r0_spt_port['traffic_config']['ip_src_addr']      = '192.85.1.2'
        r0_spt_port['traffic_config']['mac_discovery_gw'] = '192.85.1.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '192.85.2.2'

        mac = Utils.get_dut_mac_address(device=self.R1, port=r1_spt_port['port_config']['port'])
        r1_spt_port['traffic_config']['mac_dst']          = mac
        r1_spt_port['traffic_config']['ip_src_addr']      = '192.85.2.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '192.85.2.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '192.85.1.2'

        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list,
                                         verify_rewrite=False)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise
    def test_rip_protocol (self, **kwargs):
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = kwargs.get('test', None)
        input_packet    = " "
        output_packet   = " "
        misc_config = [];
        Debug.set_debug(debug);

        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)

        Debug.log('[step #1] Populate port config')
        port_info = self.update_testcase_config(**kwargs)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1           = Db.gl('r0','rt0',1)
        port3           = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        port_handle     = [port1, port3]

        Debug.log('[step #2] !!!!!!!!!!!  RIP CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring RIP on Device 1')
        del misc_config[:]
        misc_config.append('set protocols rip group group1 neighbor ' + str(self.interface_list_1[0]) + '.0')
        misc_config.append('set protocols rip group group1 export adv-route')
        misc_config.append('set protocols rip group group1 import reject-route')
        self.configure_misc_config (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring RIP on Device 2')
        del misc_config[:]
        misc_config.append('set protocols rip group group1 neighbor ' + str(self.interface_list_2[0])+ '.0')
        misc_config.append('set protocols rip group group1 export adv-route')
        misc_config.append('set protocols rip group group1 import reject-route')
        self.configure_misc_config (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  RIP CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')

        time.sleep(30)
        Debug.log('[step #3] !!!!!!!!!!!  VERIFY RIP PROTOCOL  !!!!!!!!!!!!!!!!!')
        self._l3_infra.verify_rip_protocol(device=self.R0, \
                                verif_interface = str(self.interface_list_1[0])+'.0', \
                                verif_local_addr = '50.0.0.1', \
                                verif_nh_ip = '50.0.0.2', \
                                verif_route_addr = '100.100.100.2/32')

        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=r0_spt_port['port_config']['port'])
        r0_spt_port['traffic_config']['mac_dst']          = mac
        r0_spt_port['traffic_config']['ip_src_addr']      = '192.85.1.2'
        r0_spt_port['traffic_config']['mac_discovery_gw'] = '192.85.1.1'
        r0_spt_port['traffic_config']['ip_dst_addr']      = '192.85.2.2'

        mac = Utils.get_dut_mac_address(device=self.R1, port=r1_spt_port['port_config']['port'])
        r1_spt_port['traffic_config']['mac_dst']          = mac
        r1_spt_port['traffic_config']['ip_src_addr']      = '192.85.2.2'
        r1_spt_port['traffic_config']['mac_discovery_gw'] = '192.85.2.1'
        r1_spt_port['traffic_config']['ip_dst_addr']      = '192.85.1.2'
        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise
    '''
    Routine to Test BGP protocol
    '''
    def test_bgp_protocol (self, **kwargs):
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        test            = str(kwargs.get('test', False))
        '''
        Delete previous protocol config if any
        '''
        self.cleanup_l3_config(device=self.R0)
        self.cleanup_l3_config(device=self.R1)

        port_info = self.update_testcase_config(**kwargs)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1           = Db.gl('r0','rt0',1)
        port3           = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        port_handle     = [port1, port3]

        misc_config = [];

        Debug.set_debug(debug);
        Debug.log('[step #1] Populate port config')
        Debug.log('[step #2] !!!!!!!!!!!  BGP CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring Device 1')

        '''
        BGP set commands for R0
        '''
        del misc_config[:]
        misc_config.append('set routing-options router-id 50.0.0.1')
        misc_config.append('set routing-options autonomous-system 100')
        misc_config.append('set protocols bgp group ibgp neighbor 50.0.0.2 peer-as 100')
        misc_config.append('set protocols bgp local-address 50.0.0.1')
        misc_config.append('set protocols bgp group ibgp export adv-route')
        misc_config.append('set protocols bgp group ibgp import reject-route')
        self.configure_bgp_protocol (device=self.R0, misc_config=misc_config)

        Debug.log('Configuring Device 2')
        '''
        BGP set commands for R1
        '''
        del misc_config[:]
        misc_config.append('set routing-options router-id 50.0.0.2')
        misc_config.append('set routing-options autonomous-system 100')
        misc_config.append('set protocols bgp group ibgp neighbor 50.0.0.1 peer-as 100')
        misc_config.append('set protocols bgp local-address 50.0.0.2')
        misc_config.append('set protocols bgp group ibgp export adv-route')
        misc_config.append('set protocols bgp group ibgp import reject-route')
        self.configure_bgp_protocol (device=self.R1, misc_config=misc_config)
        Debug.log('            !!!!!!!!!!!  BGP CONFIGURATION ENDS  !!!!!!!!!!!!!!!!!')

        time.sleep(30)
        Debug.log('[step #3] !!!!!!!!!!!  VERIFY BGP PROTOCOL  !!!!!!!!!!!!!!!!!')
        self._l3_infra.verify_bgp_protocol(device=self.R0,                \
                                verif_peerid    = '50.0.0.2',         \
                                verif_local_id  = '50.0.0.1',         \
                                verif_peer_as   = '100',        \
                                verif_local_as  = '100',        \
                                verif_dest_nh_ip = '50.0.0.2', \
                                verif_intf      = str(self.interface_list_1[0])+'.0',    \
                                verif_route_addr = '100.100.100.2/32')

        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=r0_spt_port['port_config']['port'])
        port_info[port1]['traffic_config']['mac_dst']          = mac
        port_info[port1]['traffic_config']['ip_src_addr']      = '192.85.1.2'
        port_info[port1]['traffic_config']['mac_discovery_gw'] = '192.85.1.1'
        port_info[port1]['traffic_config']['ip_dst_addr']      = '192.85.2.2'

        mac = Utils.get_dut_mac_address(device=self.R1, port=r1_spt_port['port_config']['port'])
        port_info[port3]['traffic_config']['mac_dst']          = mac
        port_info[port3]['traffic_config']['ip_src_addr']      = '192.85.2.2'
        port_info[port3]['traffic_config']['mac_discovery_gw'] = '192.85.2.1'
        port_info[port3]['traffic_config']['ip_dst_addr']      = '192.85.1.2'

        #self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        port_list = [port1, port3]
        chk_port_list = [port1, port3]
        try:
            self._traffic_utils.l2_start_test(test=test, port_info=port_info,
                                         port_list=port_list,
                                         chk_port_list=chk_port_list)
        except:
            self._traffic_utils.debug_traffic_failure(handle=handle,
                                                 test=test,
                                                 port_info=port_info,
                                                 port_list=port_list,
                                                 chk_port_list=chk_port_list)
            #Device.clean_config(handle=handle)
            raise

    def test_l3_traffic_vlan_tagged (self, **kwargs):
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        debug           = kwargs.get('debug', False)
        is_flood        = kwargs.get('is_flood', False)
        port_info       = self.update_testcase_config(**kwargs)
        test            = kwargs.get('test', None)
        handle = Db.get_handle('r0')
        handle = Db.get_handle('r1')
        port1           = Db.gl('r0','rt0',1)
        port3           = Db.gl('r1','rt0',1)
        r0_spt_port     = port_info[port1]
        r1_spt_port     = port_info[port3]
        port_handle     = [port1, port3]

        misc_config = [];
        Debug.set_debug(debug);

        Debug.log('[step #1] Populate port config')

        Debug.log('[step #2] !!!!!!!!!!!  VLAN TAGGING CONFIGURATION STARTS  !!!!!!!!!!!!!!!!!')
        Debug.log('Configuring Vlan Tagging on Device 1')
        Device.config(cmd='set interfaces ' + str(self.interface_list_1[0]) + ' vlan-tagging unit 0 vlan-id 110', handle=self.R0)
        Device.config(cmd='set interfaces ' + r0_spt_port['port_config']['port'] + ' vlan-tagging unit 0 vlan-id 100', handle=self.R0)
        Device.commit(handle=self.R0)

        Debug.log('Configuring Vlan Tagging on Device 2')
        Device.config(cmd='set interfaces ' + str(self.interface_list_2[0]) + '  vlan-tagging unit 0 vlan-id 110', handle=self.R1)
        Device.config(cmd='set interfaces ' + r1_spt_port['port_config']['port'] + ' vlan-tagging unit 0 vlan-id 100', handle=self.R1)
        Device.commit(handle=self.R1)

        Debug.log(' VERIFY Default Route')
        Debug.log(' ********************\n')
        cmd = "show route protocol static"
        Debug.log(("[{0}] show command : {1}".format(set_method, cmd)), self._default_log_level)
        try:
            result_dict = Device.cli_show_cmd_dict(handle=self.R0, cmd=cmd)
        except warnings.warn:
            pass
        verif_intf = str(self.interface_list_1[0]) + '.0'

        try:
            self._l3_infra.verify_routing_table(protocol_name='Static', dest_nh_ip='50.0.0.2', egr_intf = verif_intf, \
                        verif_table = 'inet.0', verif_route = '100.100.100.2/32', result_dict=result_dict)
        except:
            self.cleanup_basic_l3_config (r0_spt_port = port_info[port1],
                                        r1_spt_port = port_info[port3]);
            raise AssertionError("Routes verification Failed  !! \n")

        #Update parameters for spirent traffic
        mac = Utils.get_dut_mac_address(device=self.R0, port=port_info[port1]['port_config']['port'])
        port_info[port1]['traffic_config']['mac_dst']          = mac
        port_info[port1]['traffic_config']['ip_src_addr']      = '192.85.1.2'
        port_info[port1]['traffic_config']['mac_discovery_gw'] = '192.85.1.1'
        port_info[port1]['traffic_config']['ip_dst_addr']      = '192.85.2.2'

        mac = Utils.get_dut_mac_address(device=self.R1, port=port_info[port3]['port_config']['port'])
        port_info[port3]['traffic_config']['mac_dst']          = mac
        port_info[port3]['traffic_config']['ip_src_addr']      = '192.85.2.2'
        port_info[port3]['traffic_config']['mac_discovery_gw'] = '192.85.2.1'
        port_info[port3]['traffic_config']['ip_dst_addr']      = '192.85.1.2'

        try:
            self.start_test(port_info=port_info, port_handle=port_handle, test=test)
        except:
            self.cleanup_basic_l3_config (r0_spt_port = port_info[port1],
                                        r1_spt_port = port_info[port3]);
            raise AssertionError("Traffic Verfication failed  !! \n")

        self.cleanup_basic_l3_config(r0_spt_port = port_info[port1],
                                    r1_spt_port = port_info[port3]);

    def cleanup_basic_l3_config (self, **kwargs):
        debug           = kwargs.get('debug', False)
        device          = kwargs.get('device', None)
        set_method      = inspect.stack()[0][3]
        r0_spt_port = kwargs.get('r0_spt_port', False)
        r1_spt_port = kwargs.get('r1_spt_port', False)
        try:
            Device.config(cmd='delete interfaces ' + self.interface_list_1[0] + ' vlan-tagging ', handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd='delete interfaces ' + self.interface_list_1[0] + ' unit 0 vlan-id ', handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd='delete interfaces ' + r0_spt_port['port_config']['port'] + ' vlan-tagging ', handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd='delete interfaces ' + r0_spt_port['port_config']['port'] + ' unit 0 vlan-id ', handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 100.100.100.2/32 next-hop 50.0.0.2'), handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 192.85.2.0/24 next-hop 50.0.0.2'), handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)

        Device.commit(handle=self.R0)

        try:
            Device.config(cmd='delete interfaces ' + self.interface_list_2[0] + ' vlan-tagging ', handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd='delete interfaces ' + self.interface_list_2[0] + ' unit 0 vlan-id ', handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd='delete interfaces ' + r1_spt_port['port_config']['port'] + ' vlan-tagging ', handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd='delete interfaces ' + r1_spt_port['port_config']['port'] + ' unit 0 vlan-id ', handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 100.100.100.1/32 next-hop 50.0.0.1'), handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 100.100.100.1/32 next-hop 50.0.0.1'), handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 192.85.2.0/24 next-hop 50.0.0.2'), handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 192.85.1.0/24 next-hop 50.0.0.1'), handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        Device.commit(handle=self.R1)

    def cleanup_l3_config (self, **kwargs):
        set_method = inspect.stack()[0][3]
        #Debug.log(("[{0}] checking vlan membership of the interface {1}".format(set_method, kwargs)), self._default_log_level)
        device         = kwargs.get('device', None)
        try:
            Device.config(cmd='delete protocols ', handle=device)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 100.100.100.2/32 next-hop 50.0.0.2'), handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 100.100.100.1/32 next-hop 50.0.0.1'), handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 192.85.2.0/24 next-hop 50.0.0.2'), handle=self.R0)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)
        try:
            Device.config(cmd=('delete routing-options static route 192.85.1.0/24 next-hop 50.0.0.1'), handle=self.R1)
        except:
            Debug.log(("{0} Statement not found".format(set_method)), self._default_log_level)

        # commit the configuration
        Device.commit(handle=device)

    # suite setup and teardown apis
    def l3_sanity_suite_init (self, **kwargs):
        set_method = inspect.stack()[0][3]
        # call setup to clean the config
        Debug.log('[step #0] [%s] setup traffic for ports' % set_method)
        Debug.log('--------------------------------------------------------')
        try:
            Debug.log('setup traffic session')
            super(TestL3Infra, self).base_suite_init()
        except:
            Debug.log('setup L3 Sanity suit init failed')
        self.R0=Db.get_handle('r0')
        self.R1=Db.get_handle('r1')

        self.interface_list_1.append(Db.get_network_port_from_key('r0','r1',1))
        self.interface_list_1.append(Db.get_network_port_from_key('r0','r1',2))
        self.interface_list_2.append(Db.get_network_port_from_key('r1','r0',1))
        self.interface_list_2.append(Db.get_network_port_from_key('r1','r0',2))

        # cleanup the configuration
        try:
            Device.clean_config(handle=self.R0)
        except:
            Debug.log('clean config failed for R0')
            raise

        try:
            Device.clean_config(handle=self.R1)
        except:
            Debug.log('clean config failed for R1')
            raise

        Debug.log('[step #0] [%s] setup traffic for ports' % set_method)
        # Initialize port_info dictionary
        Debug.log(('Setup port and traffic dictionaries'), self._default_log_level)
        port_info = self.intialize_ports()

        Debug.log(('Setup l3 ports'), self._default_log_level)
        self.setup_l3_ports(port_info = port_info)

        # check for the core dumps
        Debug.log('check for core dumps')
        try:
            Utils.check_system_core_dumps(device=self.R0)
        except:
            Debug.log('core dump check failed for r0')
            raise

        try:
            Utils.check_system_core_dumps(device=self.R1)
        except:
            Debug.log('core dump check failed for r1')
            raise


    def l3_sanity_suite_cleanup (self, **kwargs):
        """L3 sanity suite cleanup.

        Cleanup the traffic port reservation and cleanup
        the configuration.
        """
        self.R0=Db.get_handle('r0')
        self.R1=Db.get_handle('r1')
        Debug.log('cleanup the config')

        # cleanup the configuration
        try:
            Device.clean_config(handle=self.R0)
        except:
            Debug.log('clean config failed for R0')
            raise

        try:
            Device.clean_config(handle=self.R1)
        except:
            Debug.log('clean config failed for R1')
            raise

        # check for the core dumps
        Debug.log('check for core dumps')
        try:
            Utils.check_system_core_dumps(device=self.R0)
        except:
            Debug.log('core dump check failed for r0')
            raise

        try:
            Utils.check_system_core_dumps(device=self.R1)
        except:
            Debug.log('core dump check failed for r1')
            raise

        # cleanup the spirent session
        try:
            super(TestL3Infra, self).base_suite_cleanup(**kwargs)
        except:
            Debug.log('setup L3 Sanity suit cleanup failed')
            raise

#end of file
