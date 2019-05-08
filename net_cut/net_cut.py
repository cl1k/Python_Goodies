#!/usr/bin/env python
import netfilterqueue
# sudo apt install libnetfilter-queue-dev
# pip install netfilterqueue


def process_packet(packet):
    print(packet)
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run
