from scapy.all import TCP, IP, Ether, PcapReader
import sys

ip2syn = {}

def process_pcap(pcap_fname):
    for pkt in PcapReader(pcap_fname):
        if pkt.haslayer(TCP) and pkt.haslayer(IP) and pkt.haslayer(Ether):
            if pkt[TCP].flags == 0x002:  # SYN packet
                ip2syn[pkt[IP].src] = ip2syn.get(pkt[IP].src, [0, 0])
                ip2syn[pkt[IP].src][0] += 1
            elif pkt[TCP].flags == 0x012:  # SYN-ACK packet
                ip2syn[pkt[IP].dst] = ip2syn.get(pkt[IP].dst, [0, 0])
                ip2syn[pkt[IP].dst][1] += 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 detector.py file.pcap')
        sys.exit(-1)
    
    process_pcap(sys.argv[1])
    
    for key, value in ip2syn.items():
        if value[1] == 0 and value[0] >= value[1]:
            print(key)
        elif value[0] >= 3 * value[1]:
            print(key)
