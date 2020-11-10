#!/usr/bin/env python3

from mRNGconfCons import createContainer, createConnection
import requests
from requests.auth import HTTPBasicAuth
import unidecode
import json
import re


def extract(host, port, user, password, panel):

    uri = f"https://{host}:{port}/SolarWinds/InformationService/v3/Json/Query?query=SELECT c.ContainerID as customerid, c.CustomProperties.CustomerCode as customercode, c.Name as customername, s.ContainerID as siteid, s.Name as sitecode, s.Description as sitename, n.NodeID as nodeid, n.Caption as nodename, n.IP as nodeip, n.CustomProperties.DeviceType as nodetype, n.MachineType as nodemodel FROM Orion.Container as c inner join Orion.Container as s on s.ContainerId = c.Members.MemberPrimaryID inner join Orion.Container as m on m.ContainerId = s.Members.MemberPrimaryID inner join Orion.Nodes as n on n.NodeId = m.Members.MemberPrimaryID where (m.Members.MemberEntityType = 'Orion.Nodes' or m.Members.MemberEntityType = null) and c.CustomProperties.Type = 'Customer'"
    response = requests.get(uri, auth=HTTPBasicAuth(user, password), verify=False)
    content = response.content.decode("utf-8")
    content = re.sub("&", "", content)
    content = unidecode.unidecode(content)
    table = json.loads(content)
    
