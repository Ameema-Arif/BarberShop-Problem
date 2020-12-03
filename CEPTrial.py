from threading import *
import time

class BarberShop:
    chairs = 3                                        # total chairs in the waiting room
    barber_chair = Semaphore(1)                       # lock
    customer = Semaphore(0)                           
    waiting_customers = 0                             # waiting customers
    barberOnJob = Semaphore(0)                        # barbers
    selected_customer = 0                             # total customers selected to be seated on the barber chair

    def cutHair(self):
        time.sleep(1)
        print("Barber starts cutting hair.")
        time.sleep(3)
        print("Barber finished his job.")
        time.sleep(1)
    
    def getHairCut(self):
        time.sleep(0.01)

        if self.selected_customer == 1:
            print("first Customer wakes up the barber")
        print("Customer %d wants a hair cut." % self.selected_customer)

    def balk(self):
        time.sleep(5)
        print("Customer has gone.")

    def barber(self):
        time.sleep(0.1)
        self.customer.acquire()
        
        time.sleep(0.01)
        self.barber_chair.acquire()
        
        time.sleep(0.01)
        self.waiting_customers = self.waiting_customers - 1
        self.selected_customer = self.selected_customer + 1
        self.chairs = self.chairs + 1
        
        time.sleep(1)
        self.barberOnJob.release()
        
        time.sleep(0.01)
        self.cutHair()
        
        time.sleep(0.01)
        self.barber_chair.release()
        
        time.sleep(0.01)
        
    def customers(self):
        time.sleep(0.01)
        self.barber_chair.acquire()
        
        if self.waiting_customers <= self.chairs:
            self.chairs = self.chairs - 1            
            time.sleep(0.01)
            
            self.customer.release()
            time.sleep(0.01)
            
            self.barber_chair.release()
            time.sleep(0.01)
            
            self.barberOnJob.acquire()
            time.sleep(0.01)
            
            self.getHairCut()
            time.sleep(0.01)
            

        else:                                         
            self.barber_chair.release()
            time.sleep(0.01)
            self.balk()
            time.sleep(0.01)

    

            

xyzBarberShop = BarberShop()
print("Barber is going to sleep.")

for i in range(0, 7):

    BarberThread = Thread(target=xyzBarberShop.barber)
    CustomerThread = Thread(target=xyzBarberShop.customers)

    BarberThread.start()
    time.sleep(0.01)
    CustomerThread.start()
    time.sleep(0.01)


