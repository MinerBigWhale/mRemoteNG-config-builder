import xml.etree.cElementTree as ET
from xml.etree.cElementTree import ElementTree, SubElement, XML, register_namespace, XMLParser
from xml.dom import minidom
import uuid 
import re

class confBuilder:

    def __init__(self, filePath):
        self.filePath = filePath
        self.open()

    def open(self):
        register_namespace("mrng", "http://mremoteng.org")
        xmlp = XMLParser(encoding="utf-8")
        with open(self.filePath, 'r') as xml_file:
            tree = ET.parse(xml_file, parser=xmlp)
            self.root = tree.getroot()

    def close(self):
        xmlraw = ET.tostring(self.root, "utf-8").decode("utf-8")
        xmlclean = re.sub('\s+(?=<)', '', xmlraw)
        xmlpretty = minidom.parseString(xmlclean).toprettyxml(encoding="utf-8", indent="    ").decode("utf-8")
        with open(self.filePath, "w+") as f:
            f.write(xmlpretty)

    def addBranch(self, branch, xml): 
        if branch != "root":
            for child in reversed(self.root):
                try:
                    if child.attrib['Name'] == branch:
                        self.root.remove(child)
                except(KeyError):
                    continue
            
            sub = [createContainer(branch)]
            sub[-1].extend(xml)
            self.root.extend(sub)
            return
        self.root.extend(xml)
        return 

