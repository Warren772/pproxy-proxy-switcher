#!/usr/bin/python

import threading
import time
import subprocess
import logging 
import sys 

def importArray():  
    proxies = []
    file1 = open('proxy.txt', 'r')
    lines = file1.readlines()
    for line in lines:
        proxies.append(line.strip())
    
    return proxies
    

def runServers(proxies):
    startPort = 5000;
    for proxy in proxies:
        server = proxy.replace(" ", "#") 
        host = "http://0.0.0.0:" +  str(startPort)
        socks4 = "socks5://" + server + " -v"
        cmd = "python -m pproxy -l " + host + " -r " + socks4
        print(cmd);
        proc = subprocess.Popen(cmd, shell=True)
        startPort+=1;
   
def main():
    proxies = importArray()
    runServers(proxies)
    count = 0;
    while True:
        count+=1;
    
    
    
if __name__ == "__main__":
    main();
