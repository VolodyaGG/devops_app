SCRIPT_DIR=$(dirname "$0")
WORKER_IP=${WORKER_IP:-10.184.0.117}
HOST=${HOST:-"cbr-app.local"}

echo "Add host"
echo "$WORKER_IP  $HOST" | sudo tee -a /etc/hosts

echo "Add CA cert"

if [[ "$OSTYPE" == "darwin"* ]]; then
    sudo security add-trusted-cert -d -r trustRoot \
        -k /Library/Keychains/System.keychain "$SCRIPT_DIR/rootCA.pem"
else
    sudo cp ./rootCA.pem /usr/local/share/ca-certificates/mkcert-cbr.crt
    sudo update-ca-certificates
fi

echo "Success. Open https://cbr-app.local/info"