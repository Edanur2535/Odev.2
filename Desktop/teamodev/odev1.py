import socket
import struct
import time

def send_message_buffer(client_socket, message, buffer_size):
    message_bytes = message.encode('utf-8')
    message_size_bytes = struct.pack("!I", len(message_bytes))
    client_socket.sendall(message_size_bytes)

    offset = 0
    while offset < len(message_bytes):
        end = offset + buffer_size
        chunk = message_bytes[offset:end]
        client_socket.sendall(chunk)
        offset = end

def receive_message_buffer(client_socket, buffer_size):
    message_size_bytes = client_socket.recv(4)
    message_size = struct.unpack("!I", message_size_bytes)[0]

    received_message = b""
    while len(received_message) < message_size:
        chunk = client_socket.recv(buffer_size)
        received_message += chunk

    return received_message.decode('utf-8')

server_ip = "34.234.82.161"
server_port = 13571

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
    print("sunucuya bağlanıldı...")
    connection_name = "Edanur"
    topic_name = "ödev"
    message = "message"
    buffer_size = 16

    send_message_buffer(client_socket, connection_name, buffer_size)
    send_message_buffer(client_socket, topic_name, buffer_size)
    send_message_buffer(client_socket, message, buffer_size)

    print("mesaj gönderildi.")
    time.sleep(5)
    received_connection_name = receive_message_buffer(client_socket, buffer_size)
    received_topic_name = receive_message_buffer(client_socket, buffer_size)
    received_message = receive_message_buffer(client_socket, buffer_size)
    print(received_connection_name)
    print(received_topic_name)
    print(received_message)

except Exception as e:
    print("hata oluştu:", e)
finally:
    client_socket.close()
    print("bağlantı kapatıldı.")