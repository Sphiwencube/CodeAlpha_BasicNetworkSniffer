from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        print("================================")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")

        if TCP in packet:
            print("Protocol Type: TCP")
            print(f"Payload: {bytes(packet[TCP].payload)}")

        elif UDP in packet:
            print("Protocol Type: UDP")
            print(f"Payload: {bytes(packet[UDP].payload)}")

print("Starting network sniffer...")
sniff(prn=packet_callback, count=10)
