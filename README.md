markdown
# MHR‑CFW Windows Client – Corporate Edition

Secure, high‑performance HTTPS proxy with MITM, domain fronting, and automatic Windows system proxy integration.  
Designed for enterprise environments where all outbound traffic must be inspected or rerouted through a controlled relay.

## ✨ Features

- **All‑in‑one embedded CA** – No external certificate files; the CA is hardcoded and automatically installed into the Windows Trusted Root store when running as administrator.
- **Powerful proxy engine** – HTTP/HTTPS and SOCKS5 support, full MITM for TLS traffic, domain fronting, connection pooling, and HTTP/2 multiplexing.
- **Smart routing** – Automatically bypasses Google IP ranges unless blocked, uses direct connections when possible, and falls back to the relay only when required.
- **Low‑latency caching** – Static assets (CSS, JS, images, fonts) are cached with intelligent TTL parsing to reduce relay load.
- **Windows system proxy** – Automatically sets the system‑wide proxy on start and clears it on exit (requires admin rights).
- **User‑friendly GUI** – Built with PySide6, featuring a clean corporate design, license validation, history storage, and a real‑time log console.
- **License management** – Licenses are validated online, and used codes are stored locally for quick reconnection.
- **No console window** – Runs silently in the background; logs are visible inside the GUI only (no extra terminal).

## 📋 System Requirements

- **Operating System** – Windows 10 / Windows 11 (x64)
- **Python** – 3.9 or higher (3.11+ recommended)
- **Privileges** – Administrator rights are **required** for automatic CA installation and system proxy configuration.  
  Without admin, the proxy will still work but you must install the CA and configure your browser manually.

## 🚀 Installation

1. **Clone or download** this repository.

2. **Install dependencies** using pip:
   ```bash
   pip install -r requirements.txt
Required packages:

PySide6 – GUI framework

cryptography – Certificate generation

aiohttp – License validation (async HTTP)

h2, hyperframe, hpack – HTTP/2 support

brotli, zstandard – Advanced compression (optional but recommended)

certifi – SSL certificate bundle

Run the application (as administrator for full functionality):

bash
python MHR_CFW.py
If not launched as admin, you will receive a warning. You can still use the proxy by manually configuring your browser (see below).

🖱️ Usage
Start the GUI – The main window appears with two sections:

License & Control: Enter your license code and click Connect & Start Proxy.

License History: Previously used codes are saved for quick reuse.

First run (admin only) – If running as administrator, the CA certificate is automatically installed into the Windows Trusted Root store, and the system proxy is enabled.
Your entire system traffic (HTTP/HTTPS/SOCKS5) will be routed through the proxy at 127.0.0.1:8085 (HTTP) and 127.0.0.1:1080 (SOCKS5).

Manual configuration (non‑admin) – If you cannot or do not want to run as administrator:

Install ca/mhr-cfw.crt (extracted from the embedded certificate) into your browser’s certificate store.

Configure your browser (or OS proxy settings) to use 127.0.0.1:8085 as an HTTP/HTTPS proxy.

Stop the proxy – Click Stop Proxy. The system proxy will be disabled immediately.

Note: The proxy engine continues to run even after closing the GUI? No – closing the main window stops the proxy engine and disables the system proxy.

⚙️ Configuration
All configuration parameters are supplied by the license server upon successful validation.
The client does not have a local configuration file; everything is received from http://185.208.175.180:5055/api/validate.

Typical server‑provided settings include:

listen_host – IP address the proxy listens on (default: 127.0.0.1)

listen_port – HTTP proxy port (default: 8085)

socks5_port – SOCKS5 port (default: 1080)

google_ip – IP address used for Google domain fronting (default: 216.239.38.120)

front_domain – SNI name for domain fronting (default: www.google.com)

relay_timeout – Timeout for relay requests (seconds)

parallel_relay – Number of parallel script‑ID channels for failover

Advanced users can modify the embedded default settings directly in the DomainFronter and ProxyServer classes, but this is not recommended.

🧰 Troubleshooting
Symptom	Likely cause	Solution
certutil error during CA installation	Not running as administrator	Restart the application as Administrator.
System proxy not changed	Not admin or registry permissions	Run as admin, or set proxy manually in Windows Settings.
License validation fails	Server unreachable or invalid code	Check your network connection; verify the license code.
TLS handshake errors in logs	CA not trusted	Install the CA certificate manually (extract from embedded or use certutil).
h2 related errors	Missing HTTP/2 library	Install h2, hyperframe, hpack.
GUI freezes on start	Missing Qt platform plugin	Ensure PySide6 is installed correctly, or run python -m pip install --force-reinstall PySide6.
🔧 Manual CA installation (if auto‑install fails)
The embedded CA certificate is printed in the source code. You can save it to a file (mhr-cfw.crt) and install it:

cmd
certutil -addstore Root mhr-cfw.crt
Or import it via the Graphical Certificate Manager (certlm.msc or certmgr.msc).

🗂️ File Structure
text
.
├── MHR_CFW.py            # Main application source
├── requirements.txt      # Python dependencies
└── README.md             # This file
⚖️ License & Disclaimer
This software is provided for authorised corporate use only.
The embedded certificate and private key are hardcoded and must not be redistributed without permission.
Use of this software may be subject to local laws regarding traffic interception.
The author assumes no liability for misuse.

🛠️ Building a Standalone Executable
You can package the application into a single .exe using PyInstaller:

bash
pip install pyinstaller
pyinstaller --onefile --windowed --name MHR-CFW --icon TASK.png MHR_CFW.py
The --windowed flag prevents a console window from appearing.

📬 Support
For technical issues, please contact your system administrator or open an issue in the internal repository.
External support is not provided for this corporate edition.

Version: 1.0 – Corporate Edition
Last updated: 2026-05-13
