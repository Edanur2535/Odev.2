import socket

def main():
    server_ip="34.234.82.161"
    server_port=13571
    
    edanur_cinar=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    edanur_cinar.bind((server_ip,server_port))
    edanur_cinar.listen(1)
    
    print("sunucu dinleniyor...")
    
    client_socket,client_address=edanur_cinar.accept()
    print("bağlantı sağlandı.")
    try:
        while(true)
    
    