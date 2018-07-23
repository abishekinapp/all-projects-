import time
import socket
i=1
while i>0:
    print("Day/month/date : ",time.ctime())
    print("IP address : ",socket.gethostbyname(socket.gethostname()), "\n")
    time.sleep(2)
    