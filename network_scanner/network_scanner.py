#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
# putting all the packet information into one variable
    arp_request_broadcast = broadcast / arp_request
# timeout = 1 waits for 1 second if there is no response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
# we get index [0] since send/receive returns two coupled lists
# we are only interested in the answered packets

    for element in answered_list:
        # we only want the second element in the couple
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("--------------------------------------------------------------------------------")


scan("10.0.2.1/24")
