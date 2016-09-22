#coding:utf-8

import socket

target_host='127.0.0.1'
target_port=23000

#建立一个socket对象,默认是tcp协议
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务端
client.connect((target_host,target_port))
#发送一些数据
client.send('hello sock1!')
#接受一些数据
response=client.recv(4096)
#打印数据
print response