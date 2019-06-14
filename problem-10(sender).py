import  socket
recv_ip="127.0.0.1"
recv_port=4534 #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=int(raw_input('Press key 1 or 2--->>>'))

if n == 2:
    files=str(raw_input("enter the file location"))
    f=open(files,'r')
    msg=f.read()
#  sending  data  to target
    s.sendto(msg,(recv_ip,recv_port))
    #  recv data  from  recv
    print(s.recvfrom(1500))
if n==1:
    msg=raw_input("plz  enter your message :   ")
    s.sendto(msg,(recv_ip,recv_port))
    print('message sent to receiver')
