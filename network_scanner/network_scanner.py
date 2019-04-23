#!/usr/bin/env python

import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Enter IP, or IP range to be scanned")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an IP, or IP range. Use --help for more info.")
    return options


def scan(target):
    arp_request = scapy.ARP(pdst=target)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

# putting all the packet information into one variable
    arp_request_broadcast = broadcast / arp_request

# timeout = 1 waits for 1 second if there is no response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

# we get index [0] since send/receive returns two coupled lists (answered / unanswered)
# we are only interested in the answered packets

# creates a list of dictionaries containing client data
# iterates through answered and puts answered_list data into dictionary
# appends each dictionary to the client_list and returns
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

# use this regex to ensure a valid ip has been passed in
# ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$

# def get_target_ip(target):


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()

scan_result = scan(options.target)
print_result(scan_result)
