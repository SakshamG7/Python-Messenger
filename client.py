import random
import server

class client():
    # Constructor
    def __init__(self, user):
        self.user = user
        self.key = None

    # Get User
    def getUser(self):
        return self.user
    
    # Set User
    def setUser(self, user):
        self.user = user

    # Get Key
    def getKey(self):
        return self.key
    
    # Set Key
    def setKey(self, key):
        self.key = key
    
    # Generate Key
    def genKey(self):
        self.key = random.randint(1, 100)
        return self.key
    
    # Send message to server for requested user
    def send(self, msg, user):
        print("Message sent: " + msg + " to " + user)
        server.receive(msg, user)

    # Message listener from server
    def receive(self, msg):
        print("Message received: " + msg)

    # basic encryption using the key TODO: improve encryption method, this is temporary
    def encrypt(self, msg):
        for i in range(len(msg)):
            msg[i] = chr(ord(msg[i]) + self.key)
    
    # decrypts message using the key
    def decrypt(self, msg):
        for i in range(len(msg)):
            msg[i] = chr(ord(msg[i]) - self.key)
