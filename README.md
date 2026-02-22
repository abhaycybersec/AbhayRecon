🔥 AbhayRecon

AbhayRecon is a Python-based OSINT and reconnaissance automation tool that collects publicly available information about a target domain or IP address in a structured and efficient way.

It is designed for educational use and cybersecurity practice.

❓ What is AbhayRecon?

AbhayRecon is a Python-based OSINT and reconnaissance automation tool designed to collect publicly available information about a target domain or IP address.

It streamlines the initial information-gathering phase of cybersecurity assessments by combining multiple checks—such as WHOIS lookup, DNS records retrieval, and public data extraction—into a single, structured command-line workflow.

🚀 Features

🛰 WHOIS information lookup

📡 DNS records extraction (A, MX, NS)

🌐 Website status, server & title detection

🔎 Basic subdomain enumeration

💼 LinkedIn company search link generation

🏢 Career page detection

📧 Public email extraction

⚡ Fully automated recon workflow

🧪 This Tool Can Be Tested On

Kali Linux

Ubuntu

Parrot Security OS

macOS

Windows (PowerShell / Command Prompt)

Windows Subsystem for Linux (WSL)

Termux (Android – Limited Support)

Requires Python 3.9+ and required dependencies installed on the system.

🛠 Installing & Requirements
📌 Requirements

Python 3.9 or higher

Internet connection

Required Python libraries:

requests

python-whois

📥 Installation Steps
1️⃣ Clone the Repository
git clone https://github.com/abhaycybersec/AbhayRecon.git
cd AbhayRecon
2️⃣ (Optional but Recommended) Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux / macOS:

python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install requests python-whois
▶ Run the Tool

Windows:

python main.py

Linux / macOS:

python3 main.py

🔄 Change Log
v1.0.0

Initial release of AbhayRecon

Added WHOIS lookup

Added DNS records extraction

Added Website information module

Added Subdomain enumeration

Added LinkedIn search link generator

Added Career page detection

Added Public email scraper

👨‍💻 Author

Abhay Pratap Singh Yadav
Cyber Security Enthusiast
Focused on OSINT & Recon Automation
GitHub: https://github.com/abhaycybersec
