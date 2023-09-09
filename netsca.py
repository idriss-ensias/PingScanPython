from ping3 import ping
from scapy.layers.inet import IP
import socket
import threading

def list_sep(list_a):
    n = 10
    big_list = []
    for i in list_a:
        n = n-1
        if n >= 9:
            big_list.append([])
        elif n == 0:
            n = 10
        big_list[-1].append(str(i.dst))
    return big_list

sepp = list_sep(IP(dst="x.x.x.x/x"))

def ping_test(dst):
    if ping(dst):
        print(dst+" : "+socket.getnameinfo((dst,0),0)[0]+" is up !")

threadlist = []

for d in sepp : 
    for j in d:
        threadlist.append(threading.Thread(target=ping_test, args=(j,)))
        threadlist[-1].start()

for n in threadlist:
    n.join()


        
