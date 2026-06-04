from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello Threads", i+1)
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi Threads", i+1)
            sleep(1)
            
if __name__ == "__main__":
    obj1 = Hello()
    obj2 = Hi()

    obj1.start()
    obj2.start()

