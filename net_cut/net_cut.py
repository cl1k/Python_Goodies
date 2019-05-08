#!/usr/bin/env python
import netfilterqueue
# sudo apt install libnetfilter-queue-dev
# pip install netfilterqueue
# iptables -I FORWARD -j NFQUEUE --queue -num 0
# iptables --flush


def process_packet(packet):
    print(packet)
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run
