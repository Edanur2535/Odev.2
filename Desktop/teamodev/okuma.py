import socket
import struct


def int_to_bytearray(value):
    return struct.pack('>I', value)


def string_to_bytearray(value, length=32):
    return value.encode('utf-8').ljust(length, b'\0')


class Connection:
    def __init__(self, conn_name, topic_name, buffer_size=1024):
        self.conn_name = conn_name
        self.topic_name = topic_name
        self.buffer_size = buffer_size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect(("localhost", 13571))
        self.socket.sendall(string_to_bytearray(conn_name))
        self.socket.sendall(string_to_bytearray(topic_name))
        self.socket.sendall(int_to_bytearray(buffer_size))

    def read(self):
        return self.socket.recv(self.buffer_size)

    def send(self, message_bytes):
        self.socket.sendall(message_bytes)

    def close(self):
        self.socket.close()
