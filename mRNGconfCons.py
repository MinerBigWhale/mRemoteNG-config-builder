#!/usr/bin/env python3

import xml.etree.cElementTree as ET
from xml.etree.cElementTree import XML, register_namespace, XMLParser
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
        xmlpretty = minidom.parseString(xmlclean).toprettyxml(
            encoding="utf-8", indent="    ").decode("utf-8")
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


def createConnection(name, panel="", username="", domain="", password="", hostname="", protocol="", port=""):
    inheritUsername = "false"
    if username == "[inherit]":
        username = ""
        inheritUsername = "true"
    inheritDomain = "false"
    if domain == "[inherit]":
        domain = ""
        inheritDomain = "true"
    inheritPassword = "false"
    if password == "[inherit]":
        password = ""
        inheritPassword = "true"
    inheritProtocol = "false"
    if protocol == "[inherit]":
        protocol = ""
        inheritProtocol = "true"
    inheritPort = "false"
    if port == "[inherit]":
        port = ""
        inheritPort = "true"

    node = XML(f'<Node Name="{name}" VmId="" UseVmId="false" Type="Connection" Descr="" Icon="Domain Controller" Panel="{panel}" Id="{uuid.uuid4()}" Username="{username}" Domain="{domain}" Password="{password}" Hostname="{hostname}" Protocol="{protocol}" RdpVersion="rdc6" PuttySession="Default Settings" Port="{port}" ConnectToConsole="false" UseCredSsp="true" RenderingEngine="IE" ICAEncryptionStrength="EncrBasic" RDPAuthenticationLevel="NoAuth" RDPMinutesToIdleTimeout="0" RDPAlertIdleTimeout="false" LoadBalanceInfo="" Colors="Colors16Bit" Resolution="FitToWindow" AutomaticResize="true" DisplayWallpaper="false" DisplayThemes="false" EnableFontSmoothing="true" EnableDesktopComposition="false" CacheBitmaps="true" RedirectDiskDrives="true" RedirectPorts="false" RedirectPrinters="false" RedirectClipboard="true" RedirectSmartCards="false" RedirectSound="BringToThisComputer" SoundQuality="Dynamic" RedirectAudioCapture="false" RedirectKeys="true" Connected="false" PreExtApp="" PostExtApp="" MacAddress="" UserField="" Favorite="false" ExtApp="" VNCCompression="CompNone" VNCEncoding="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPassword="" VNCColors="ColNormal" VNCSmartSizeMode="SmartSAspect" VNCViewOnly="false" RDGatewayUsageMethod="Never" RDGatewayHostname="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false" InheritColors="false" InheritDescription="false" InheritDisplayThemes="false" InheritDisplayWallpaper="false" InheritEnableFontSmoothing="false" InheritEnableDesktopComposition="false" InheritDomain="{inheritDomain}" InheritIcon="false" InheritPanel="false" InheritPassword="{inheritPassword}" InheritPort="{inheritPort}" InheritProtocol="{inheritProtocol}" InheritRdpVersion="false" InheritPuttySession="false" InheritRedirectDiskDrives="false" InheritRedirectKeys="false" InheritRedirectPorts="false" InheritRedirectPrinters="false" InheritRedirectClipboard="false" InheritRedirectSmartCards="false" InheritRedirectSound="false" InheritSoundQuality="false" InheritRedirectAudioCapture="false" InheritResolution="false" InheritAutomaticResize="false" InheritUseConsoleSession="false" InheritUseCredSsp="false" InheritRenderingEngine="false" InheritUsername="{inheritUsername}" InheritICAEncryptionStrength="false" InheritRDPAuthenticationLevel="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAlertIdleTimeout="false" InheritLoadBalanceInfo="false" InheritPreExtApp="false" InheritPostExtApp="false" InheritMacAddress="false" InheritUserField="false" InheritFavorite="false" InheritExtApp="false" InheritVNCCompression="false" InheritVNCEncoding="false" InheritVNCAuthMode="false" InheritVNCProxyType="false" InheritVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNCColors="false" InheritVNCSmartSizeMode="false" InheritVNCViewOnly="false" InheritRDGatewayUsageMethod="false" InheritRDGatewayHostname="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false" InheritRDGatewayDomain="false" InheritVmId="false" InheritUseVmId="false" />')

    return node


def createContainer(name, panel="", username="", domain="", password="", hostname="", protocol="", port=""):
    inheritUsername = "false"
    if username == "[inherit]":
        username = ""
        inheritUsername = "true"
    inheritDomain = "false"
    if domain == "[inherit]":
        domain = ""
        inheritDomain = "true"
    inheritPassword = "false"
    if password == "[inherit]":
        password = ""
        inheritPassword = "true"
    inheritProtocol = "false"
    if protocol == "[inherit]":
        protocol = ""
        inheritProtocol = "true"
    inheritPort = "false"
    if port == "[inherit]":
        port = ""
        inheritPort = "true"

    node = XML(f'<Node Name="{name}" VmId="" UseVmId="false" Type="Container" Expanded="true" Descr="" Icon="Domain Controller" Panel="{panel}" Id="{uuid.uuid4()}" Username="{username}" Domain="{domain}" Password="{password}" Hostname="{hostname}" Protocol="{protocol}" RdpVersion="rdc6" PuttySession="Default Settings" Port="{port}" ConnectToConsole="false" UseCredSsp="true" RenderingEngine="IE" ICAEncryptionStrength="EncrBasic" RDPAuthenticationLevel="NoAuth" RDPMinutesToIdleTimeout="0" RDPAlertIdleTimeout="false" LoadBalanceInfo="" Colors="Colors16Bit" Resolution="FitToWindow" AutomaticResize="true" DisplayWallpaper="false" DisplayThemes="false" EnableFontSmoothing="true" EnableDesktopComposition="false" CacheBitmaps="true" RedirectDiskDrives="true" RedirectPorts="false" RedirectPrinters="false" RedirectClipboard="true" RedirectSmartCards="false" RedirectSound="BringToThisComputer" SoundQuality="Dynamic" RedirectAudioCapture="false" RedirectKeys="true" Connected="false" PreExtApp="" PostExtApp="" MacAddress="" UserField="" Favorite="false" ExtApp="" VNCCompression="CompNone" VNCEncoding="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPassword="" VNCColors="ColNormal" VNCSmartSizeMode="SmartSAspect" VNCViewOnly="false" RDGatewayUsageMethod="Never" RDGatewayHostname="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false" InheritColors="false" InheritDescription="false" InheritDisplayThemes="false" InheritDisplayWallpaper="false" InheritEnableFontSmoothing="false" InheritEnableDesktopComposition="false" InheritDomain="{inheritDomain}" InheritIcon="false" InheritPanel="false" InheritPassword="{inheritPassword}" InheritPort="{inheritPort}" InheritProtocol="{inheritProtocol}" InheritRdpVersion="false" InheritPuttySession="false" InheritRedirectDiskDrives="false" InheritRedirectKeys="false" InheritRedirectPorts="false" InheritRedirectPrinters="false" InheritRedirectClipboard="false" InheritRedirectSmartCards="false" InheritRedirectSound="false" InheritSoundQuality="false" InheritRedirectAudioCapture="false" InheritResolution="false" InheritAutomaticResize="false" InheritUseConsoleSession="false" InheritUseCredSsp="false" InheritRenderingEngine="false" InheritUsername="{inheritUsername}" InheritICAEncryptionStrength="false" InheritRDPAuthenticationLevel="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAlertIdleTimeout="false" InheritLoadBalanceInfo="false" InheritPreExtApp="false" InheritPostExtApp="false" InheritMacAddress="false" InheritUserField="false" InheritFavorite="false" InheritExtApp="false" InheritVNCCompression="false" InheritVNCEncoding="false" InheritVNCAuthMode="false" InheritVNCProxyType="false" InheritVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNCColors="false" InheritVNCSmartSizeMode="false" InheritVNCViewOnly="false" InheritRDGatewayUsageMethod="false" InheritRDGatewayHostname="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false" InheritRDGatewayDomain="false" InheritVmId="false" InheritUseVmId="false" />')

    return node
