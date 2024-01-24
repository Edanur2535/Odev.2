import socket
import struct


def int_to_bytearray(value):
    return struct.pack('>I', value)


def string_to_bytearray(value, length=32):
    return value.encode('utf-8').ljust(length, b'\0')

class Car:
    def __init__(self):
        self.headlights_status="off"
        
class HeadlightContolDecoder:
    
    def __init__(self,car):
        self.car=car
        
    def turn_on(self):
        self.car.headlights_status="on"
        print("Headlights are now ON")
        
    def turn_of(self):
        self.car.headlights_status="off"
        print("Headlights are now OFF")
        
    def check_status(self):
        print(self.car.headlights_status)
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

        
def main():
    my_car=Car()
    decoder=HeadlightContolDecoder(my_car)
    print("Welcome to the Headlights Control System")
    
    while True:
        print("\n1. Turn On Headlights\n2. Turn Off Headlights\n3. Check Headlights\n4. Exit")
        choice=input("Enter number:")
        
        if choice=="1":
            decoder.turn_on()
             
        elif choice=="2":
            decoder.turn_off()
            
        elif choice=="3":
            decoder.check_status()
            
        elif choice=="4":
            print("Exiting Headlight Contol System")
            break
        else:
            print("Please enter a valid option")
            
if __name__ == "__main__":
    main()   
        