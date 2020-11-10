#!/usr/bin/env python3

from mRNGconfCons import confBuilder
import csvImport
import orionImport
import argparse
import sys
from os import path


def main():
    parser = argparse.ArgumentParser(description="Decrypt mRemoteNG passwords.")
    parser.add_argument("-c", "--csv", help="path to csv file")
    parser.add_argument("-o", "--orion", help="Orion server user/password/ip/port")
    parser.add_argument("-b", "--branch", help="create a branch for this import", default="root")
    parser.add_argument("-p", "--password", help="password to encrypt connection password", default="")

    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    branch = args.branch

    # initialize the confCons Object
    # xmlfile = new nMRGconfCons(path.expandvars(r'%APPDATA%\mRemoteNG\confCons.xml'))
    xmlfile = confBuilder(path.expandvars(r'%APPDATA%\mRemoteNG\Generated.xml'), args.password)

    if args.csv != None:
        print('--importing from csv')
        # load csvfile
        filePath = path.expandvars(args.csv)
        separator = ','
        columns = {
            'Name': 'description',
            'Username': 'user',
            'Domain': 'ad',
            'Password': 'pass',
            'Hostname': 'host',
            'Protocol': 'proto',
            'Port': 'port'
        }

        csv = csvImport.extract(filePath, branch, separator, columns)

        # add csv content to confCons
        xmlfile.addBranch(branch, csv)
    
    if args.orion != None:
        print('--importing from orion')
        # parse server connection string
        user = args.orion.split('/')[0]
        password = args.orion.split('/')[1]
        host = args.orion.split('/')[2]
        port = args.orion.split('/')[3]

        orion = orionImport.extract(host, port, user, password, branch)

        # add csv content to confCons
        xmlfile.addBranch(branch, orion)

    # apply configuration
    xmlfile.close()
    print("===== Done ")


if __name__ == "__main__":
    main()
