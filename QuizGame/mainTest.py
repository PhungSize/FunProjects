class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
user_1 = User("001", "Andrew")
user_2 = User("002", "Elizabeth")

user_1.follow(user_2)

print(f"{user_1.name} has {user_1.followers} followers and is following {user_1.following}" )
