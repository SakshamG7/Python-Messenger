class Server:
    def __init__(self):
        self.users = []
    
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
    
    # adds user to list of users
    def pushUser(self, user):
        self.users.append(user)
