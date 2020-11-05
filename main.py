from mRNGconfCons import confBuilder
import csvImport
import argparse
import sys
from os import path


def main():
    parser = argparse.ArgumentParser(description="Decrypt mRemoteNG passwords.")
    parser.add_argument("-c", "--csv", help="path to csv file")
    parser.add_argument("-b", "--branch", help="create a branch for this import", default="root")
    parser.add_argument("-p", "--password", help="password to encrypt connection password", default="mR3m")

    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # initialize the confCons Object
    #xmlfile = new nMRGconfCons(path.expandvars(r'%APPDATA%\mRemoteNG\confCons.xml'))
    xmlfile = confBuilder(path.expandvars(r'%APPDATA%\mRemoteNG\Generated.xml'))

    # load csvfile
    filePath = path.expandvars(args.csv)
    branch = args.branch
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

    # apply configuration
    xmlfile.close()


if __name__ == "__main__":
    main()