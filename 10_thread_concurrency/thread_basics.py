from threading import Thread
from time import sleep

def hello():
    for i in range(5):
        print("Hello Threads", i+1)
        sleep(1)


def hi():
    for i in range(5):
        print("Hi Threads", i+1)
        sleep(1)
   
            
if __name__ == "__main__":
    obj1 = Thread(target=hello)
    sleep(0.5)
    obj2 = Thread(target=hi)

    obj1.start()
    obj2.start()


    obj1.join()
    obj2.join()

    print("bye")
