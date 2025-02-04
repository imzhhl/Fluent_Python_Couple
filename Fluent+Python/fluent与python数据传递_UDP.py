import socket

#IPV4,TCP协议
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#ipv4,udp
#绑定ip和端口，bind接受的是一个元组
sock.bind(('127.0.0.1',54377))

while True:
    #-----------------------------------------------------------------------------------------------------------------------
    #下面进行UDF的数据操作...
    
    # 接收
    received_data,clientAddress=sock.recvfrom(40960)
    
    # 转化为数组
    received_data_str = received_data.split()
    received_data_float = list(map(float, received_data_str)) 
    print(f'{received_data_float[0]};{received_data_float[1]};{received_data_float[2]};{received_data_float[3]}')

    # 发送的数据用空格隔开，然后组合成字符串
    a = 10.2
    b = 1.1221
    c = 1002.12
    space = ' '
    send_data= str(a) + space + str(b) + space + str(c)
    
    # 发送
    sock.sendto(bytes(send_data, encoding = "utf8"),clientAddress)
    
    #UDF数据操作结束...
    # -----------------------------------------------------------------------------------------------------------------------
    # 关闭连接
    
# 关闭服务器
sock.close()
