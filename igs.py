import instaloader

L = instaloader.Instaloader()

userID = input("Enter your Instagram username: ")

try:
    L.load_session_from_file(userID)
except:
    try:
        L.interactive_login(userID)
    except:
        print("Error: Login Failed!")
        exit()
    else:
        saveSession = input("Save login information locally? (y/n): ")
        if saveSession == "y" or saveSession == "Y":
            L.save_session_to_file()

print("\nTarget account must be public. Data of private accounts can be fetched if you follow them.")
targetUsername = input("Enter target account username: ")

print("Searching...")
profile = instaloader.Profile.from_username(L.context, targetUsername)
print("Account (%s) found!" % targetUsername)

followersList = []
followeesList = []

print("\nFetching followers...")

for follower in profile.get_followers():
    followersList.append(follower.username)

print("Followers list obtained!")

followersFile = open("%s-followers.txt" % targetUsername, "a+")
followersFile.truncate(0)

for follower in followersList:
    followersFile.write(follower + "\n")

followersFile.close()

print("Followers list saved!")

print("\nFetching followees...")

for followee in profile.get_followees():
    followeesList.append(followee.username)

print("Followees list obtained!")

followeesFile = open("%s-followings.txt" % targetUsername, "a+")
followeesFile.truncate(0)

for follower in followeesList:
    followeesFile.write(follower + "\n")

followeesFile.close()

print("Followees list saved!")
