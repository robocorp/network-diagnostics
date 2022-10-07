:: Run the "TLS Debug Robocorp Vault" to get the values for the following
SET SECRETS_API_GET="https://api.us1.robocorp.com/secrets-v1/workspaces/b90da0be-cb72-48a2-9ffe-7665810cbd7a/secrets/ever?encryptionScheme=robocloud-vault-transit-v2&publicKey=MIICI..."
SET AUTH_HEADER="Authorization: Bearer eyJhbGciOi..."

curl --ssl-no-revoke --tlsv1.2 -v --noproxy '*' ^
 %SECRETS_API_GET% ^
 --header %AUTH_HEADER% ^
 --header "User-Agent: python-requests/2.28.1" ^
 --header "HTTP/1.1" ^
 --header "Host: api.us1.robocorp.com" ^
 --header "Accept-Encoding: gzip, deflate" ^
 --header "Accept: */*" ^
 --header "Connection: keep-alive" ^