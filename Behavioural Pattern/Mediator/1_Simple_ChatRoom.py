class ChatRoom:
    def __init__(self):
        self.users = []

    def add_users(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_message(message)
        print()


class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send_message(self, msg):
        print(f"{self.name} sends: {msg}\n")
        self.chatroom.send_message(msg, self)

    def receive_message(self, msg):
        print(f"{self.name} receives: {msg}")


if __name__ == "__main__":
    chatroom = ChatRoom()

    sam = User("Sam", chatroom)
    alice = User("Alice", chatroom)
    bob = User("Bob", chatroom)
    john = User("John", chatroom)

    chatroom.add_users(sam)
    chatroom.add_users(alice)
    chatroom.add_users(bob)
    chatroom.add_users(john)

    sam.send_message("Hello !")
    alice.send_message("Hey Guys!")
    bob.send_message("Whatsssup!")
    alice.send_message("Lets Plan Something!")
