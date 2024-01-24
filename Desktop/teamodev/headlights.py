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
        