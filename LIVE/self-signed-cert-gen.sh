#!/usr/bin/env bash

# Specify where we will install
# the xip.io certificate
SSL_DIR="/etc/ssl/publiccloud.co"

# Set the wildcarded domain
# we want to use
DOMAIN="*.publiccloud.co"

# A blank passphrase
PASSPHRASE=""

# Set our CSR variables
SUBJ="
C=US
ST=California
O=
localityName=SanJose
commonName=$DOMAIN
organizationalUnitName=
emailAddress=
"

# Create our SSL directory
# in case it doesn't exist
sudo mkdir -p "$SSL_DIR"

# Generate our Private Key, CSR and Certificate
sudo openssl genrsa -out "$SSL_DIR/publiccloud.co.key" 2048
sudo openssl req -new -subj "$(echo -n "$SUBJ" | tr "\n" "/")" -key "$SSL_DIR/publiccloud.co.key" -out "$SSL_DIR/publiccloud.co.csr" -passin pass:$PASSPHRASE
sudo openssl x509 -req -days 3650 -in "$SSL_DIR/publiccloud.co.csr" -signkey "$SSL_DIR/publiccloud.co.key" -out "$SSL_DIR/publiccloud.co.crt"
