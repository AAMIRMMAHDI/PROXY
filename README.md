# MHR-CFW Windows Client – Corporate Edition

> **Embedded CA + Auto Install**  
> A Windows client/proxy tool with built-in certificate management for secure interception and corporate network workflows.

---

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6)
![Language](https://img.shields.io/badge/language-Python-3776AB)
![License](https://img.shields.io/badge/license-Internal%20Use%20Only-orange)

</div>

---

## ✨ Overview

**MHR-CFW Windows Client – Corporate Edition** is a Windows-oriented proxy and certificate management utility designed for controlled enterprise environments.

It includes:

- An **embedded CA certificate and private key**
- **Automatic CA installation** into the Windows Trusted Root store when running with admin privileges
- A **full proxy engine** supporting:
  - HTTP
  - SOCKS5
  - MITM inspection
  - Domain fronting

The project appears to be built for environments where secure interception, traffic routing, and corporate trust management are required.

---

## 🧩 Key Features

<div align="grid">

### 📜 Embedded Certificate Authority
The application ships with an embedded CA certificate and private key for trusted interception workflows.

### ⚙️ Auto Install on Windows
When launched as administrator, the client can automatically install the CA certificate into the Windows Trusted Root store.

### 🛡️ MITM Certificate Management
A dedicated certificate manager handles MITM-related certificate logic and trust provisioning.

### 🌐 Proxy Support
Supports multiple proxy modes and advanced routing behavior, including:
- HTTP proxying
- SOCKS5 proxying
- MITM interception
- Domain fronting

</div>

---

## 🏗️ Project Structure
```text
mhr-cfw-windows-client/
├── main.py
├── README.md
├── certs/
│   ├── embedded_ca.crt
│   └── embedded_ca.key
├── src/
│   ├── proxy/
│   ├── mitm/
│   └── utils/
└── assets/
└── screenshots/
