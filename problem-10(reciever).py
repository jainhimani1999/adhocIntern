import  socket
recv_ip="127.0.0.1"
recv_port=4534  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  fitting    ip and port  with udp socket
s.bind((recv_ip,recv_port))
n=raw_input('Press key 1 to send the message--->>>')


if n =='1':
    msg=raw_input('Enter the message')
    s.sendto(msg[0],(recv_ip,recv_port))
    #  recv data  from  recv
    print(s.recvfrom(1500))
else:
    print(s.recvfrom(1500))

s.close()
