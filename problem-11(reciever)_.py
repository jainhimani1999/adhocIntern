
import  socket
recv_ip="127.0.0.1"
recv_port=9999  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  fitting    ip and port  with udp socket
s.bind((recv_ip,recv_port))

#   recv  data  from  sender

while  4  >  2  :
    data=s.recvfrom(100)
    print(data[0])
    while True:
        msg=raw_input("plz  enter your message :   ")
        if len(msg) > 150:
            print('Letter Exceed 150 characters')
            continue
        else:
            break
    s.sendto(msg,data[1])


s.close()
