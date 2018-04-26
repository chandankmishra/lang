#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from collections import defaultdict
import heapq
import re

def get_ip_addr(iphash, nstr):
    pattern = re.compile("[0-2]?\d?\d[.][0-2]?\d?\d[.][0-2]?\d?\d[.][0-2]?\d?\d")
    matches = pattern.findall(nstr)
    for match in matches:
        iphash[match] += 1

def top_k_most_frequent(arr, k):
    iphash = defaultdict(int)
    res = list()

    nstr = ""
    for i in arr:
        nstr += i
        if i == '\n':
            get_ip_addr(iphash, nstr)
            nstr = ""

    # build a minheap with (freq, ip) tupple as key
    for key, ip in enumerate(iphash):
        heapq.heappush(res, (iphash[ip], ip))
        if len(res) > k:
            heapq.heappop(res)
    print (res)

    # build a list from the hash table.
    result = list()
    while res:
        var = heapq.heappop(res)
        result.append(var[1])
    result.reverse()
    return result

nstr= """0.0.0.0/8    0.0.0.0 –
    0.255.255.255   16,777,216  Software    Used for broadcast messages to the current ("this")[1]
    10.0.0.0/8  10.0.0.0 –
    10.0.0.0/8  10.0.0.0 –
    10.0.0.0/8  10.0.0.0 –
    10.255.255.255  16,777,216  Private network Used for local communications within a private network[2]
    100.64.0.0/10   100.64.0.0 –
    100.64.0.0/10   100.64.0.0 –
    100.64.0.0/10   100.64.0.0 –
    100.64.0.0/10   100.64.0.0 –
    100.127.255.255 4,194,304   Private network Used for communications between a service provider and its subscribers when using a carrier-grade NAT[3]
    127.0.0.0/8 127.0.0.0 –
    127.255.255.255 16,777,216  Host    Used for loopback addresses to the local host[4]
    127.255.255.255 16,777,216  Host    Used for loopback addresses to the local host[4]
    127.255.255.255 16,777,216  Host    Used for loopback addresses to the local host[4]
    169.254.0.0/16  169.254.0.0 –
    169.254.255.255 65,536  Subnet  Used for link-local addresses between two hosts on a single link when no IP address is otherwise specified, such as would have normally been retrieved from a DHCP server[5]
    169.254.255.255 65,536  Subnet  Used for link-local addresses between two hosts on a single link when no IP address is otherwise specified, such as would have normally been retrieved from a DHCP server[5]
    172.16.0.0/12   172.16.0.0 –
    172.31.255.255  1,048,576   Private network Used for local communications within a private network[2]
    192.0.0.0/24    192.0.0.0 –
    192.0.0.255 256 Private network Used for the IANA IPv4 Special Purpose Address Registry[6]
    192.0.0.255 256 Private network Used for the IANA IPv4 Special Purpose Address Registry[6]
    192.0.0.255 256 Private network Used for the IANA IPv4 Special Purpose Address Registry[6]
    192.0.0.255 256 Private network Used for the IANA IPv4 Special Purpose Address Registry[6]
    192.0.0.255 256 Private network Used for the IANA IPv4 Special Purpose Address Registry[6]
    192.0.0.255 256 Private network Used for the IANA IPv4 Special Purpose Address Registry[6]
    192.0.2.0/24    192.0.2.0 –
    192.0.2.255 256 Documentation   Assigned as "TEST-NET-1" for use in documentation and examples. It should not be used publicly.[7]
    192.88.99.0/24  192.88.99.0 –
    192.88.99.255   256 Internet    Used by 6to4 anycast relays (deprecated)[8]
    192.88.99.255   256 Internet    Used by 6to4 anycast relays (deprecated)[8]
    192.88.99.255   256 Internet    Used by 6to4 anycast relays (deprecated)[8]
    192.88.99.255   256 Internet    Used by 6to4 anycast relays (deprecated)[8]
    192.88.99.255   256 Internet    Used by 6to4 anycast relays (deprecated)[8]
    192.168.0.0/16  192.168.0.0 –
    192.168.255.255 65,536  Private network Used for local communications within a private network[2]
    198.18.0.0/15   198.18.0.0 –
    198.18.0.0/15   198.18.0.0 –
    198.18.0.0/15   198.18.0.0 –
    198.19.255.255  131,072 Private network Used for testing of inter-network communications between two separate subnets[9]
    198.51.100.0/24 198.51.100.0 –
    198.51.100.0/24 198.51.100.0 –
    198.51.100.255  256 Documentation   Assigned as "TEST-NET-2" for use in documentation and examples. It should not be used publicly.[7]
    203.0.113.0/24  203.0.113.0 –
    203.0.113.0/24  203.0.113.0 –
    203.0.113.0/24  203.0.113.0 –
    203.0.113.255   256 Documentation   Assigned as "TEST-NET-3" for use in documentation and examples. It should not be used publicly.[7]
    224.0.0.0/4 224.0.0.0 –
    239.255.255.255 268,435,456 Internet    Reserved for multicast[10]
    240.0.0.0/4 240.0.0.0 –
    255.255.255.254 268,435,456 Internet    Reserved for future use[11]
    255.255.255.255/32  255.255.255.255 1   Subnet  Reserved for the "limited broadcast" destination address[11]
    """
print (top_k_most_frequent(nstr, 3))
