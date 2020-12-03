
# mRemoteNG-config-builder

Create new branches in confCons.xml for connections details gathered from multiple sources

## install

```bash
git clone https://github.com/MinerBigWhale/mRemoteNG-config-builder.git
cd mRemoteNG-config-builder
pip3 install -r requirements.txt
```

## Import csv file into a new branch

```bash
python3 main.py -c ".\examples\example.csv" -b "csv"
```

## Import from orion into a new branch

```bash
python3 main.py -o "username/password/server/port" -b "Orion"
```

## Usage
```bash
python3 main.py [-h] [-c CSV] [-o ORION] [-b BRANCH] [-p PASSWORD]

Decrypt mRemoteNG passwords.

optional arguments:
 -c CSV, --csv CSV                      path to csv file
 -o ORION, --orion ORION                Orion server user/password/ip/port
 -b BRANCH, --branch BRANCH             create a branch for this import (default is in root)
 -p PASSWORD, --password PASSWORD       password to encrypt connection password
```
