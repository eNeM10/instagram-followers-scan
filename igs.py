import os
from dotenv import load_dotenv
import instaloader

load_dotenv()

username = os.environ.get('userid')
password = os.environ.get('password')

L = instaloader.Instaloader()


L.login(username, password)

profile = instaloader.Profile.from_username(L.context, r'ntx23')

followersList = []

for follower in profile.get_followers():
    followersList.append(follower.username)

print("Followers list obtained")
print("Followers: " + str(len(followersList)))

followersFile = open("my_followers.txt", "a+")
followersFile.truncate(0)

for follower in followersList:
    followersFile.write(follower + "\n")

followersFile.close()

followeesList = []

for followee in profile.get_followees():
    followeesList.append(followee.username)

print("Followees list obtained")

followeesFile = open("my_followees.txt", "a+")
followeesFile.truncate(0)

for follower in followeesList:
    followeesFile.write(follower + "\n")

followeesFile.close()
