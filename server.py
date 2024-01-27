from client import *

class server():
    def __init__(self):
        self.users = []
        # creates users
        self.users.append(client("Bob"))
        self.users.append(client("Jim"))
    
    def receive(self, msg, user):
        print("Message received: " + msg + " from " + user)
        # sends message to user
        user.receive(msg)
