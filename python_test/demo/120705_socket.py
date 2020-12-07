import socket
# 1 AF_INET 网络模式  ; AF_UNIX  本地模式
# 2 SOCK_STREAM  tcp/ip    tcp模式  ;  SOCK_DGRAM  udp  udp模式
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",8125))
s.listen(8)  # 同时连接8个

while True:
    connection,address = s.accept()
    buf =connection.recv(10)
    connection.send(data=buf)
s.close()








