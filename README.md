# tls-logging

Bots to log and hunt down network traffic TLS level problems.


## Bot `TLS Debug Robocorp Vault` 

This bot connects to the Robocorp Vault by executing `Get Secret` using `rpaframework` library `RPA.Robocorp.Vault`.
Target Robocorp Vault name is by default **ever**, but this can be changed in the `task_robocorp_vault.py` file or by
setting environment variable `TARGET_ROBOCORP_VAULT`.

## Bot `TLS Debug Request` 

This bot can be customized to make any kind of request using Python's `requests` package.

## Bot `TLS OpenSSL`

Will run `openssl` command and outputs information.