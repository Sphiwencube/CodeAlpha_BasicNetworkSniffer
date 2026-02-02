📘 Basic Network Sniffer — CodeAlpha Internship

🧪 Project Summary
This is a Python based network packet sniffer built as part of the CodeAlpha Internship program.
The sniffer captures network traffic and analyzes packets to show:
Source IP
Destination IP
Protocol type
Payload content

🛠️ Tools & Technologies Used:
✔️ Python 3.10+
✔️ Anaconda (for virtual environment management)
✔️ Scapy — Python library for packet manipulation
✔️ Npcap (Windows only) — required for packet capture
✔️ Git & GitHub — version control and repository hosting

CodeAlpha_BasicNetworkSniffer/
├── sniffer.py
├── requirements.txt
├── .gitignore
└── README.md

🧭 Setup & Installation
1️⃣ Created & Activatde Anaconda Environment
    -conda create -n net_sniffer python=3.10 -y
    -conda activate net_sniffer
2️⃣ Install Scapy
    -pip install scapy
3️⃣ (Windows Only) Install Npcap
    -Download and install Npcap to enable packet capturing on Windows.

🧪 Usage Instructions
    -Open Anaconda Prompt as Administrator (Windows)
    -Navigate to your project directory:
      -cd path/to/CodeAlpha_BasicNetworkSniffer
    -Run the sniffer:
      -python sniffer.py

🧠 What It Does:
The sniffer code listens for network packets and prints:
Output	                  Description
Source IP	                Origin of the packet
Destination IP	          Packet destination
Protocol number	IP        protocol field (TCP/UDP)
Protocol type	            Interpreted type like “TCP” or “UDP”
Payload	                  Raw data part of the protocol

🧑‍💻 Example Output
================================
Source IP: 192.168.1.10
Destination IP: 192.168.1.1
Protocol: 6
Protocol Type: TCP
Payload: b'GET / HTTP/1.1\r\nHost: example.com\r\n...'

📌 Notes & Recommendations:
✔️ Always run as Administrator/Root when sniffing packets.
✔️ Capture packets only in networks you own or have permission to test.
✔️ On Windows, Scapy won’t capture real packets without Npcap.
✔️ This project is for learning and ethical security research only.
