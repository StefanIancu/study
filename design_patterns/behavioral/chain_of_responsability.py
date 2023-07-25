# 

class Handler:

    def __init__(self, succesor):
        # define who is the next handler
        self._succesor = succesor

    def handle(self, request):
        handled = self._handle(request) # if handled, stop here

        # otherwise, keep going
        if not handled:
            self._succesor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass ")

class ConcreteHandler1(Handler):

    def _handle(self, request):
        if 0 < request <= 10: # condition hor handling
            print(f"Request {request} handled in handler 1.")

class DefaultHandler(Handler):

    def _handle(self, request):
        print(f"End of chain, no handler for {request}.")
        return True # indicates the request has been handled
    
class Client:
    
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

# create a client
c = Client()

# create request 
requests = [2, 5, 30]

# send requests 
c.delegate(requests)