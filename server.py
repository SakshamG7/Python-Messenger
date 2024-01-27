from client import *

class server():
    def __init__(self):
        self.users = []
        # creates users
        self.users.append(client("Bob"))
        self.users.append(client("Jim"))
    
    # returns user object from list of users
    def getUser(self, user):
        for i in range(len(self.users)):
            if self.users[i].getUser() == user:
                return self.users[i]
    
    # receives message from user and sends it to the requested user
    def receive(self, msg, user):
        print("Message received: " + msg + " from " + user)
        # sends message to user
        self.getUser(user).receive(msg)
