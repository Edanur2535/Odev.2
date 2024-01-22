import socket
import struct
import time

    
server_ip="34.234.82.161"
server_port=13571
    
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
def send_message():
    
    connection_name="Edanur"
    topic_name="ödev"
    message="oldu mu:)"
    client_socket.sendall(connection_name.ljust(32,'\0').encode())
    client_socket.sendall(topic_name.ljust(32,'\0').encode())
    message_bytes=struct.pack("!I",len(message))
    client_socket.sendall(message_bytes)
    client_socket.sendall(message.encode())
try:
    client_socket.connect((server_ip,server_port))
    print("sunucuya bağlanıldı...") 
    while True:
        send_message()
        print("mesaj gönderilid...")
        time.sleep(5)  
        
except Exception as e:
    print( "hata oluştu...")
finally:
    client_socket.close()
    print("bağlantı kapatıldı.")
        
    