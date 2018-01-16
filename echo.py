# coding:utf-8
import socket
import threading
import time
import chardet

user_list = []


def tcp_link( sock, addr):
    print('accept new connection from %s:%s...' % addr)
    sock.send(b'hello\n')
    show_list()
    while True:
        try:
            data = sock.recv(1024)
        except Exception as err:
            print(err)
            break
        time.sleep(1)
        if not data:
            break
        #bianma = chardet.detect(data)
        #print("编码 %s" % bianma)
        redv_data = str(data,encoding='ascii')
        redv_data =redv_data.strip().replace('\r\n','').replace('\n', '')
        if redv_data == 'mass':
            send_all()
        elif redv_data == 'kill1':
            kill1()

        print("msg from %s:%s: data:%s" % (addr[0],addr[1], redv_data))

    remove(sock)
    sock.close()
    print('connection from %s:%s... closed  ' % addr)
    show_list()

def kill1():
    print("*******kill1 print******")
    for a in user_list:
        a[0].close()
        user_list.remove(a)
        break
    print("*******kill1 print******")

def remove(sock):
    for a in user_list:
        if a[0] == sock:
            user_list.remove(a)
            break
    return

def send_all():
    print("*******send_all print******")
    for a in user_list:
        a[0].send(bytes('NOTICE\n','utf-8'))
    print("*******send_all print******")

def show_list():
    print("*******list print******")
    if len(user_list) ==0:
        print("NONE")
    else:
        for a in user_list:
            print(' %s:%s...\n' % a[1])
    print("*******list print******")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 20087))
s.listen(10)
print('listening port 20087')
while True:
    sock, addr = s.accept()
    user_list.append((sock,addr))
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
