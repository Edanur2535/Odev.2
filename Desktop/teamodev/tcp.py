import socket
import struct
import time
import threading

   
    

server_ip = "34.234.82.161"
server_port = 13571

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def listen():
    while True:
        data=client_socket.recv(1024)
        print(data)
    

# buffer_size'ın string olarak uzunluğunu kontrol et


try:
    client_socket.connect((server_ip, server_port))
    print("sunucuya bağlanıldı...")
    connection_name = "Edanur"
    connection_array=connection_name.encode('utf-8')
    #(69,64,61,110,117,114)
    if len(connection_array) < 32:
        padding_size = 32 - len(connection_array)
        padding = b'\x00' * padding_size
        connection_array += padding

    topic_name = "test_topic"
    topic_array=topic_name.encode('utf-8')
    if len(topic_array)<32:
        padding_size=32 - len(topic_array)
        padding=b'\x00' *padding_size
        topic_array +=padding
    message = "message"

    buffer_size = struct.pack('!I', 1024)
    client_socket.sendall(connection_array)
    client_socket.sendall(topic_array)
    client_socket.sendall(buffer_size)
    threading.Thread(target=listen, args=()).start()
    while True:
        kullanıcı=input("mesaj:")
        kullanıcı_array=kullanıcı.encode('utf-8')
        if len(kullanıcı)<1024:
            padding_size=1024-len(kullanıcı_array)
            padding=b'\x00' *padding_size
            kullanıcı_array +=padding
        client_socket.sendall(kullanıcı_array)
    
            

    
    print("mesaj gönderildi.")
    time.sleep(5)
    

except Exception as e:
    print("hata oluştu:", e)
finally:
    client_socket.close()
    print("bağlantı kapatıldı.")
