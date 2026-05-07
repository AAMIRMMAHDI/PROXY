# 🛡️ MHR‑CFW Windows Client – Corporate Edition

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform Windows](https://img.shields.io/badge/platform-Windows-0078D6.svg)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)

**Enterprise‑grade secure proxy client with automatic CA installation, MITM engine, domain fronting, and system‑wide traffic routing.**

> **Administrator rights required** – the client automatically elevates and hides the console window.

---

## 📋 Overview

MHR‑CFW is a powerful Windows proxy solution designed for corporate environments. It establishes a **secure tunnel** through Google infrastructure using **domain fronting** and **HTTP/2 multiplexing**, making it highly resilient against deep packet inspection. The client:

- ✅ Embeds its own Certificate Authority (CA) – no external files  
- ✅ Automatically installs the CA into Windows Trusted Root (when admin)  
- ✅ Configures system proxy **on start** and disables it **on exit**  
- ✅ Supports **HTTP/1.1** and **HTTP/2** (with automatic fallback)  
- ✅ Provides **SOCKS5** and **HTTP** proxy interfaces locally  
- ✅ Caches static assets for performance  
- ✅ Includes a modern **Qt GUI** with license validation and logging

---

## ✨ Features

| Category            | Capabilities                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| **Proxy Protocols** | HTTP/HTTPS (with MITM), SOCKS5 (RFC 1928)                                                      |
| **Transport**       | Domain fronting via Google IPs, SNI rotation, HTTP/2 multiplexing (H2), TLS 1.2+                |
| **Security**        | On‑the‑fly certificate generation, embedded CA, automatic CA trust installation               |
| **System**          | Auto‑set Windows proxy (HKCU), auto‑elevation, hidden console, graceful shutdown               |
| **Performance**     | Connection pooling, response caching (static assets), request batching, parallel fan‑out       |
| **Compression**     | Supports gzip, deflate, brotli, zstd decompression                                             |
| **User Interface**  | Corporate‑style dark/light log console, license history, one‑click start/stop                  |

---

## 🖥️ Installation

### 1. Prerequisites

- **Windows** 10 / 11 (64‑bit recommended)  
- **Python 3.7** or higher installed ([python.org](https://python.org))  
- Administrator privileges (first run will auto‑elevate)

### 2. Install Dependencies

Create a `requirements.txt` with the following content:

```txt
PySide6>=6.4.0
cryptography>=39.0.0
h2>=4.1.0
aiohttp>=3.8.0
brotli>=1.0.9
zstandard>=0.21.0
certifi>=2023.0.0