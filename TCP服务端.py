#coding:utf-8
#注意端口占用问题

import socket
import threading

#设置需要监听的ip与及端口
bind_ip='127.0.0.1'
bind_port=23000

#建立一个socket对象、
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定端口
server.bind((bind_ip,bind_port))

#设置最大连接数量
server.listen(5)

print "[*] Listening on %s:%d"% (bind_ip,bind_port)

#客户端处理线程
def handle_client(client_socket):
    #打印客户端发送得到的内容
    request=client_socket.recv(1024)

    print "[*] Received: %s"% request

    #返回一个数据包
    client_socket.send("ack")

    client_socket.close()


while True:
    #接收客户端
    client,addr=server.accept();

    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    #挂起客户端，处理传入的数据

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
