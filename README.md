# MHR‑CFW Secure Proxy (Corporate Edition)

**MHR‑CFW** is a high‑performance Windows proxy client that uses **domain fronting** to route your internet traffic through Google’s infrastructure, bypassing censorship and network restrictions while maintaining full transparency and speed.  
It automatically configures your system’s proxy settings and, when running with administrator privileges, installs its own certificate authority to seamlessly handle HTTPS connections.

> ⚠️ **Important** – This documentation describes the **compiled application**.  
> Source code is **not included** in this package.  
> For installation files, see the `APP/Windows` and `APP/Android` folders.

---

## Features

- **One‑click proxy** – Enter a license key, hit *Connect*, and the proxy is up in seconds.
- **Automatic Windows proxy configuration** – Sets the system proxy (HTTP & SOCKS5) on start and restores original settings on exit (requires admin).
- **Built‑in CA for HTTPS** – An embedded certificate authority can be automatically installed into Windows’ Trusted Root store so that all HTTPS traffic is inspected and relayed without browser warnings.
- **Domain fronting via Google Apps Script** – Requests are disguised as legitimate Google traffic (SNI = `www.google.com`, Host = `script.google.com`), making them extremely difficult to block.
- **High‑performance relay engine**
  - HTTP/2 multiplexing and connection pooling
  - Intelligent caching of static assets
  - Request batching and parallel fan‑out for reliability
  - Multiple rotating Google IPs and SNI names to avoid detection
- **Smart routing** – Direct connections to Google services when possible, with automatic fallback to the relay if direct connections are blocked.
- **Modern, lightweight GUI** – Built with Qt, includes a real‑time log viewer and license history.
- **License‑based activation** – Configuration is provisioned automatically from the license server; no manual setup required.

---

## Requirements

- **Operating System** – Windows 10 (version 1809 or later) / Windows 11 (64‑bit)
- **Administrator privileges** – Required for automatic proxy setup and CA installation (the application will still run without admin, but those features will be disabled)
- **Internet connection** – Outbound access to `script.google.com` and the configured Google IPs (TCP port 443)

---

## Installation

1. Download the installer from the **`APP/Windows`** folder.
2. Run the installer and follow the on‑screen instructions.
3. Launch **MHR‑CFW** from the Start menu or desktop shortcut.
4. **If you intend to use automatic proxy setup, right‑click and select *Run as administrator*.**

---

## Usage

1. **Enter your license code** in the *License Code* field.  
   (Previous codes are saved and can be re‑selected from the history list.)

2. Click **Connect & Start Proxy**.
   - The proxy will start listening on `127.0.0.1:8085` (HTTP) and, if enabled, `127.0.0.1:1080` (SOCKS5).
   - If the application is running with administrator rights, Windows’ system proxy will be automatically configured to use these ports.

3. Your browser and other applications that respect the system proxy will now route traffic through MHR‑CFW.

4. To stop the proxy, click **Stop Proxy**.  
   The system proxy will be disabled, and the original network settings will be restored.

5. The **Connection Log** panel shows real‑time activity, errors, and performance metrics.

> **Note** – All proxy settings (ports, encryption, routing rules, etc.) are **provisioned by your license server**.  
> There are no configuration files to edit.

---

## How It Works (Technical Overview)

MHR‑CFW acts as a **local forward proxy** and a **man‑in‑the‑middle (MITM) proxy** for HTTPS.

1. **HTTP Requests**  
   The client sends a plain HTTP request to the proxy.  
   The proxy rewrites the request and sends it to a **Google Apps Script** endpoint using a TLS connection with the SNI set to a harmless Google domain (e.g., `www.google.com`).  
   The Apps Script fetches the actual resource and returns it – this is **domain fronting**.

2. **HTTPS Requests (MITM)**  
   - When a browser wants to connect to an HTTPS site, the proxy intercepts the `CONNECT` request.
   - It generates a **certificate for the target domain** on‑the‑fly, signed by the embedded CA.
   - The browser’s TLS session is terminated at the proxy; the proxy decrypts the traffic.
   - The decrypted HTTP request is then forwarded through the Google Apps Script relay (just like a plain HTTP request).
   - The response is re‑encrypted with the generated certificate and sent back to the browser.
   - **This works seamlessly once the embedded CA is trusted by Windows.** The installer can add the CA to the Trusted Root store when run as administrator.

3. **Performance Optimizations**  
   - **Caching** – Static files (CSS, JS, images, etc.) are cached locally to reduce latency and server load.
   - **Connection Pooling & Multiplexing** – TLS connections to Google are reused; HTTP/2 allows multiple streams over a single connection.
   - **Batching** – Multiple small requests can be combined into a single call to the Apps Script.
   - **Smart Routing** – Direct connections to Google services are attempted first; if they fail (censored), the relay is used.

4. **Bypass & Block Lists**  
   The proxy can be instructed (via the license server) to bypass certain hosts (connect directly) or completely block others.

---

## Technology Stack (Inside the Application)

The compiled client uses these components internally:

- **Google Apps Script** – Relay endpoint  
- **Multiple Google IPs & SNI domains** – For fronting and rotation  
- **HTTP/2** – Multiplexed connections (`h2` library)  
- **TLS / SSL** – `cryptography`, `ssl` module  
- **Response compression** – gzip, deflate, brotli, zstandard  
- **Windows Registry** – Automatic proxy configuration  
- **Qt / PySide6** – Graphical user interface  
- **SQLite** – Local license history

---

## Security & Privacy Considerations

- The **embedded CA** allows the proxy to decrypt your HTTPS traffic.  
  The CA certificate is provided by the software vendor; you should trust the vendor before using this feature.  
  You can choose to **not run as administrator** – then the CA will not be installed, and HTTPS sites will show certificate warnings (or the proxy may not work properly).

- All traffic passes through the **Google Apps Script relay** owned by your license provider.  
  The relay operator can see the full content of your requests and responses (after the proxy’s MITM decryption).  
  **Use MHR‑CFW only with a license provider you trust.**

- The client **does not** log your browsing activity locally beyond the on‑screen log (which is cleared when you close the application).

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| “Not running as admin” warning | Right‑click the shortcut → **Run as administrator** to enable proxy auto‑configuration. |
| Certificate errors in browser | The CA was not installed. Launch the program as administrator once, or install the CA manually (contact support for the certificate file). |
| Slow or no internet | Check your firewall – outbound TCP 443 to Google IPs must be allowed. Verify your license is still valid. |
| Proxy fails to start | Ensure no other application is using ports 8085 or 1080. Check the log for errors. |

---

## License

This software is **proprietary** and distributed under a license‑based activation model.  
Redistribution, reverse engineering, or modification is strictly prohibited unless authorised in writing.

---

## Disclaimer

MHR‑CFW is designed for **legitimate privacy and censorship circumvention** in regions where access to information is restricted.  
The developers assume no liability for any misuse or illegal activities conducted using this software.

**Always comply with your local laws and the terms of service of the networks and services you use.**

---

*For support or to obtain a license, contact your authorised reseller.*
