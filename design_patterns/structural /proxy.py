# postpone creating an obj only when its abs necessary 

# clients -> interacting with a proxy 

# proxy -> responsible for creating the resource-intensive obj

import time

class Producer:

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """check if producer is available"""
        print("Artist checking if Producer is available...")

        if self.occupied == "No":
            #if the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)

            # make the producer meet the guest
            self.producer.meet()

        else:
            #otherwise dont instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

# instantiate a proxy 
p = Proxy()

# make the proxy - artist produce until producer is available 
p.produce()

# change state to "occupied"
p.occupied = "Yes"

# make the Producer produce 
p.produce()