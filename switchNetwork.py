# -*- coding: utf-8 -*-
"""
网卡切换
"""
from __future__ import print_function
import ctypes, sys
import time
import sys
#import socket
import subprocess


NET_WLAN_NAME = "WLAN"
NET_LOCAL_NAME = "内网"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
 

def operate_network_adapter(adaptername, toopen):
    processx = None
    try:
        cmd = "netsh interface set interface \"%s\" admin=%s" %(adaptername, "disabled" if toopen==False else "enabled")
        processx = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, creationflags=0x08000000)
         
        processx.wait()
        if processx.returncode == 0: 
            print('\n cmd \"%s\" success.\n' %cmd) 
        else: 
            print('\n cmd \"%s\" error.\n' %cmd) 
        processx.kill()
         
        pass
    except:
        print('\n%s\n' %(sys.exc_info()[1]))
        pass
    finally:
        if processx != None:
            processx.kill() 
        pass
    pass
     
if __name__ == "__main__":
    if is_admin():
    # 将要运行的代码加到这里
        process = None
        try:
            # myname = socket.getfqdn(socket.gethostname())
            # myaddr = socket.gethostbyname(myname)

            # if '192.168.2.157' not in myaddr:
            #     #open local network
            #     operate_network_adapter(NET_WLAN_NAME, False)
            #     time.sleep(2)
            #     operate_network_adapter(NET_LOCAL_NAME, True)
            # else:
            #     #open wlan
            #     operate_network_adapter(NET_LOCAL_NAME, False)
            #     time.sleep(2)
            #     operate_network_adapter(NET_WLAN_NAME, True)
            
            switch_command = input('1:开启内网，禁用外网；2:开启外网，禁用内网；请输入你的选择：')
            if switch_command == '1':
                #open local network
                operate_network_adapter(NET_WLAN_NAME, False)
                time.sleep(2)
                operate_network_adapter(NET_LOCAL_NAME, True)
            elif switch_command == '2':
                #open wlan
                operate_network_adapter(NET_LOCAL_NAME, False)
                time.sleep(2)
                operate_network_adapter(NET_WLAN_NAME, True)
            else:          
                raise Exception(print('your input is wrong'))
        except:
            print('\n%s\n' %(sys.exc_info()[1]))
            pass
        finally:
            pass
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
    
