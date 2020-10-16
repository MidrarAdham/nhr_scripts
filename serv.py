import socket
import os
import time

s = socket.socket()
s.settimeout(1000)
s.bind(('',9991))
s.listen(5)
print('server is up!')

print(os.getpid())
while True:
    c,a = s.accept()
    d = c.recv(1024)
    print(d)
    if (d.decode('utf-8') == 'ping'):
        os.system('python3 F-Resp-csv_MACRo.py')
    if not d:
        break
 
