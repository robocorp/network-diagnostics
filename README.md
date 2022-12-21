# Network Diagnostics Robot

Robot logs some common diagnostics to help hunt down network traffic level problems:
- RCC diagnostics to get the machine generic state
- Check proxy settings via: `netsh winhttp show proxy`
  - (Note: not 100% reliable as some proxies do not show up here)
- Requests -library help printout
- Test TLS communications:
  - Directly using OpenSSL
  - Using Requests -library agains Robocorp EU instance
  - Using Requests -library agains Robocorp US instance

The outputs are logged into `/output/log.html`

> Verify the content of this file before sharing

## To run this robot

Simplest way is to get rcc and just use it to run:
```
curl -o rcc.exe https://downloads.robocorp.com/rcc/releases/latest/windows64/rcc.exe
rcc pull github.com/robocorp/network-diagnostics
cd network-diagnostics-master
rcc run
```