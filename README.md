# Crappy-QR

## Ubuntu 20.04
```shell
sudo apt-get install -y python3-dev python3-pip python3-venv python3-wheel
```

## Usage
```shell
$ crappy.py --help
usage: crappy.py [-h] [--data [DATA]] [--out [OUT]]

Generate a crappy QR code

optional arguments:
  -h, --help     show this help message and exit
  --data [DATA]  the input data
  --out [OUT]    the output file
```
e.g.
```shell
crappy.py --data 'foo' --out '/tmp/foo.png'
echo "foo" | crappy.py > /tmp/foo.png
```

## Testing
```shell
python3 -m venv virt
source ./virt/bin/activate
pip3 install wheel
pip3 install .
./qr/crappy.py
xdg-open /tmp/qr-test.jpeg
deactivate
```

## Example Images
![Crappy QR](/images/qr-test.png?raw=true "QR to this repository")
