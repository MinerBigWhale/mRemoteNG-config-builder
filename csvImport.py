
from csv import DictReader
from xml.etree.cElementTree import Element
from mRNGcipher import encryptAES
from mRNGconfCons import createConnection

def extract(filePath, panel, separator, columns):
    with open(filePath, 'r')  as csvfile:
        
        reader = DictReader(csvfile, delimiter=separator, quotechar='"')
        children = []

        for row in reader:
            print(row)
            node = createConnection(row[columns["Name"]], panel, row[columns["Username"]], row[columns["Domain"]], encryptAES(row[columns["Password"]],""), row[columns["Hostname"]], row[columns["Protocol"]], row[columns["Port"]])
            children.append(node)

        return children