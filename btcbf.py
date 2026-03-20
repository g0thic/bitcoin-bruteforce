from typing import Any, Callable, Iterable, Mapping
import requests
from time import sleep
import address_factory
import multiprocessing as Multi_processing
import threading
import sys
import os
from fp.fp import FreeProxy
import random

import signal
#import win32api
import ntplib
import datetime
from time import ctime, strftime,localtime
import secrets
                    
import freeProxyProxies

class StaticMethods():
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_some_proxies():
        proxy: list = list()
        try:
            for i in range(100):
                try:
                    proxy_server = FreeProxy(timeout=1).get()
                    proxy.append(str(proxy_server))
                except BaseException as ex:
                    continue
        except BaseException as ex:
            return proxy
            
        return proxy

    @staticmethod
    def connect(address):
        try:
            
            url = "https://blockchain.info/q/getreceivedbyaddress/"+str(address)
            c = requests.get(url,timeout=1)
            return int(c.text)
        except BaseException as bx:
            return -1
    
    @staticmethod
    def connect_P(address, proxies: list):
        try:
            p_={}
            url = "https://blockchain.info/q/getreceivedbyaddress/"+str(address)
            result_ = requests.Response()
            if len(proxies) > 0:
                p_ = proxies[random.randint(0,len(proxies)-1)]
                p_ = {1: proxies[random.randrange(len(proxies))]}
            else:
                p=0
            result_ = requests.get(url, proxies=p_,timeout=1)
            return int(result_.text)
        except BaseException as ex:
            return -1
    
    @staticmethod
    def prnt_scr(txt):
        print(txt)


class Proxy_thread(threading.Thread):
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.data: list
        self.is_running : bool
        try:
            t1 = freeProxyProxies.ssl_Proxy()
            for item in t1:
                self.data.append("https://"+item)
        except:
            pass
        try:
            t2 = freeProxyProxies.free_Proxy()
            for item in t2:
                self.data.append("https://"+item)
        except:
            pass

    
    @property
    def PROXY_LIST(self):
        return self.data
    @property
    def IS_RUNNING(self):
        return self.is_running
    @IS_RUNNING.setter
    def IS_RUNNING(self,value:bool):
        self.is_running = value
        
    def get_some_proxies(self):
        proxy: list = list()
        try:
            for i in range(100):
                try:
                    proxy_server = FreeProxy().get()
                    if proxy_server not in proxy:
                        proxy.append(str(proxy_server))
                except BaseException as ex:
                    continue
        except BaseException as ex:
            return proxy
            
        return proxy
    def update_proxies(self):
        
        while self.is_running:
            try:
                p_ = self.get_some_proxies()
                if len(p_) >0:
                    for item in p_:
                        self.data.append(item)
                sleep(1)
            except BaseException as ex:
                sleep(10)
                continue

    def run(self):
        self.is_running = True
        self.data = list()
        self.update_proxies()


class Brute():
    LIB1 = "Lib1"
    LIB2 = "Lib2"
    LIB3 = "Lib3"
    LIB4 = "Lib4"
    LIB5 = "Lib5"
    LIB6 = "Lib6"
    LIB7 = "Lib7"
    def __init__(self) -> None:
        self.proxies = list()
        pass

    def connect(self, address):
        
        return StaticMethods.connect(address)

    def connect_P(self, address, proxies):
        
        return StaticMethods.connect_P(address, proxies)

    def get_adr_list(self):
        aa = list()
        bb = address_factory.AddressFact()

        cc = [self.LIB1, self.LIB2, self.LIB3,self.LIB4,self.LIB5,self.LIB6,self.LIB7]
        for dd in cc:
            try:
                ee = bb.instance(dd).getAdrs()
            except BaseException:
                    continue
            for item in ee:
                aa.append(item)
        return aa

    def append_to_file(self, wallet: list):
        fn = "key.txt"
        op = "a"
        with open(fn, op) as f:
            f.write("Address: "+str(wallet[0])+" ,WIF: "+str(wallet[1])+" ,HEX: "+str(wallet[2]))
            f.write("\n")

    def thread_func(self, wallet: list,):
        try:
            sleep(10)
            result = self.connect(wallet[0])
            
            if result > 0:
                str_ = "found: "+str(wallet[0])
                StaticMethods.prnt_scr(str_)
                self.append_to_file(wallet)
            else:
                str_ = "address: "+str(wallet[0])+" result:"+str(result)
                StaticMethods.prnt_scr(str_)
        except BaseException as ex:
            sys.tracebacklimit=0
            

    def thread_func_P(self, wallet: list, proxies: list,n,):
        try:
            sleep(10)
            result = self.connect_P(wallet[0], proxies)
            if result > 0:
                str_ = "found: "+str(wallet[0])
                StaticMethods.prnt_scr(str_)
                self.append_to_file(wallet)
            elif result == -1:
                str_ = "address: "+str(wallet[0])+" result: "+str(result)
                StaticMethods.prnt_scr(str_)
                n[1]=False
            else:
                str_ = "address: "+str(wallet[0])+" result: "+str(result)
                StaticMethods.prnt_scr(str_)
        except BaseException as ex:
            sys.tracebacklimit=0
    
    
    def con_prob(self,n):
        sleep(random.randint(1,10))
        n[1]=True
    
    def rb_P(self,size:int,n):
        proxies = list()
        st = Proxy_thread()
        st.start()
        sleep(1)
        proxies = st.PROXY_LIST
        t_list = list()
        
        
        while True:
                try:
                    if n[1] is False:
                        self.con_prob(n)
                   
                    ll = self.get_adr_list()
                    proxies = st.PROXY_LIST
                    for addr in ll:
                        if n[1] is False:
                            self.con_prob(n)
                        t_ = threading.Thread(target=self.thread_func_P, args=(
                            addr, proxies,n,))
                        t_.start()
                        t_list.append(t_)
                        sleep((random.randint(1,10)))
                    for item in t_list:
                        item.join()
                    t_list.clear() 
                    if n[1] is False:
                        self.con_prob(n)
                except BaseException as ex:
                    for item in t_list:
                        item.join()
                    st.IS_RUNNING = False
                    st.join()
                    sys.tracebacklimit = 0
                    raise ex
    def rb_(self,n):
        t_list = list()
        while True:
                try:
                    if n[1] is False:
                        self.con_prob(n)
                    ll = self.get_adr_list()
                    for addr in ll:
                        if n[1] is False:
                            break
                        t_ = threading.Thread(target=self.thread_func, args=(addr,))
                        t_.start()
                        t_list.append(t_)
                        sleep((random.randint(1,50)))
                    for item in t_list:
                        item.join()
                    t_list.clear()
                    if n[1] is False:
                        self.con_prob(n)
                except BaseException as ex:
                    sys.tracebacklimit = 0
                    raise ex
   
    def rand_brute(self, use_proxy:bool,size:int,n):
        if use_proxy:
            try:
                self.rb_P(size,n)
            except BaseException as ex:
                sys.tracebacklimit = 0
                raise ex
        elif not use_proxy:
            try:
                self.rb_(n)
            except BaseException as ex:
                raise ex

class brute_manager():
    
    def __init__(self):
        
        self.ProcessList=list()
        self.shared_= Multi_processing.Manager().list()
        
    def stop_worker(self):
        if len(self.ProcessList) > 0:
            for item in self.ProcessList:
                try:
                    os.kill(item, signal.SIGINT)
                except BaseException as eb:
                    sys.tracebacklimit = 0
                    continue
            self.ProcessList.clear()

        
    def worker_function(self,use_proxy,n,size:int):
        try:
            Brute().rand_brute(use_proxy,size,n)
        except BaseException as ex:
            n[0]=False
            
    

        
    def start_worker(self,workers:int,use_proxy:bool):
        try:
            
            for index in range(workers):
                if self.shared_[0] is False:
                    break
                tt = Multi_processing.Process(target=self.worker_function,args=(use_proxy,self.shared_,workers))
                tt.start()
                self.ProcessList.append(tt.pid)
                sleep(5)
                
            while (self.shared_[0] is True):
                try:
                    sleep(1)
                except BaseException as kex:
                    break
            self.shared_[0]=False
            self.stop_worker()
            sleep(1)
        except BaseException as ex:
            sys.tracebacklimit = 0
            self.stop_worker()


    def manage(self, total_workers:int, enable_proxy:bool):
        try:
            self.shared_.append(True)
            self.shared_.append(True)
            self.start_worker(workers=total_workers,use_proxy=enable_proxy)
        except BaseException as ex:
            self.stop_worker()


def run_app(workers:int):
    try:
        d: brute_manager = brute_manager()
        d.manage(total_workers=workers,enable_proxy=True)
    except BaseException as ex:
        sys.tracebacklimit = 0
        return

def user_input():
    u_i = "ERROR"
    c_ = 0
    while(u_i.isnumeric() is False and c_ < 3):
        u_i = input("number of threads >> ")
        c_+=1
    if c_ >= 3 or u_i.isnumeric() is False:
        print("too many wrong inputs")
        raise Exception("")
    else:
        return int(u_i)

if __name__ == "__main__":
    try:
        StaticMethods.prnt_scr("welcome")
        ww_ = user_input()
        run_app(workers=ww_)
        StaticMethods.prnt_scr("see you")
    except BaseException as e:
        sys.tracebacklimit = 0
        StaticMethods.prnt_scr("see you")
        sys.exit()
