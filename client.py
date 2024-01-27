# Imports
from server import Server

# Client class
class Client:
    def __init__(self, user):
        self.user = user
        self.key = None

    # Get Key
    def getKey(self):
        return self.key
    
    # Set Key
    def setKey(self, key):
        self.key = key
    
    # Generate Key, basic way to get a random number TODO: improve key generation method, this is temporary
    def genKey(self):
        seed = self.user
        for i in range(len(seed)):
            self.key += ord(seed[i])
        self.key = self.key % 26
    
    # Send message to server for requested user
    def send(self, msg, user):
        print("Message sent: " + msg + " to " + user)
        Server.receive(msg, user)

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
