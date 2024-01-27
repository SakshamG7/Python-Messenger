import client
import server

def main():
    s = server.Server
    
    # Create user names
    num_users = int(input("Enter the number of users: "))

    for i in range(num_users):
        username = input(f"Enter username {i+1}: ")
        c = client.Client(user=username)
        s.pushUser(user=c)

    # Access the server
    for user in s.users:
        print(f"{user.username} is accessing the server.")

    # Creates a seperate terminal for each user, each having their own ui but access the same server
    for user in s.users:
        user.run()

if __name__ == "__main__":
    main()
