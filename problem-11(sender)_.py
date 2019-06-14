import  socket
recv_ip="127.0.0.1"
recv_port=9999  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 >  3  :
    while True:
        msg=raw_input("plz  enter your message :   ")
        if len(msg) > 150:
            print('Letter Exceed 150 characters')
            continue
        else:
            break
#  sending  data  to target
    s.sendto(msg,(recv_ip,recv_port))
    #  recv data  from  recv
    print(s.recvfrom(150))
    den=raw_input('You want to continue the chat-->>>[y/n]')
    if den == 'n':
        break;
