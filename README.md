# mRemoteNG-config-builder
Create new branches in confCons.xml for connections details gathered from multiple sources

## install
```bash
    git clone https://github.com/MinerBigWhale/mRemoteNG-config-builder.git
    cd mRemoteNG-config-builder
    pip3 install pycryptodomex
```

## Import csv file into a new branch
```bash
    python3 main.py -c ".\examples\example.csv" -b "csv"
```
usage: main.py [-h] [-c CSV] [-b BRANCH] [-p PASSWORD]

Decrypt mRemoteNG passwords.

optional arguments:
  -c CSV, --csv CSV                     path to csv file
  -b BRANCH, --branch BRANCH            create a branch for this import (default is in root)
  -p PASSWORD, --password PASSWORD      password to encrypt connection password