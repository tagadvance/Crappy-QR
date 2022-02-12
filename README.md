# Crappy-QR

## Ubuntu 20.04
```shell
sudo apt-get install -y python3-dev python3-pip python3-venv python3-wheel
```

## Testing
```shell
python3 -m venv virt
source ./virt/bin/activate
pip3 install wheel
pip3 install .
python3 qr/test.py && xdg-open /tmp/qr-test.jpeg
deactivate
```

## Example Images
![Crappy QR](/images/qr-test.png?raw=true "QR to this repository")
