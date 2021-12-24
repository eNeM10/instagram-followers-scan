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
foundUserName = profile.full_name
if foundUserName is None or foundUserName == "":
    foundUserName = "@" + profile.username
print("Account found (%s)!" % foundUserName)


followersList = []
followeesList = []

print("\nFetching followers...")

for follower in profile.get_followers():
    followersList.append(follower.username)

print("Followers list obtained!")

print("\nFetching followees...")

for followee in profile.get_followees():
    followeesList.append(followee.username)

print("Followees list obtained!")

saveToFile = input("\nSave followers and followings to file? (y/n): ")
if saveToFile == "y" or saveToFile == "Y":
    followersFile = open("op-%s-followers.txt" % targetUsername, "w")
    followersFile.truncate(0)

    for follower in followersList:
        followersFile.write(follower + "\n")

    followersFile.close()

    print("Followers list saved!")

    followeesFile = open("op-%s-followings.txt" % targetUsername, "w")
    followeesFile.truncate(0)

    for follower in followeesList:
        followeesFile.write(follower + "\n")

    followeesFile.close()

    print("Followees list saved!")

while True:
    print("\n\nMENU:")
    print("1. Get friends (followers that you follow back)")
    print("2. Get fans (followers that you don't follow back)")
    print("3. Get stars ;) (followees that don't follow you back)")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '0':
        print("\nExiting...")
        exit()
    elif choice == '1':
        mutual = list(set(followersList).intersection(followeesList))
        print("\nNumber of followers that you follow back: " + str(len(mutual)))
        print("Mutual followers: " + str((', '.join(mutual))))
        # print(mutual)
        saveToFile = input("\nSave fans to file? (y/n): ")
        if saveToFile == "y" or saveToFile == "Y":
            mutualFile = open("op-%s-mutual.txt" % targetUsername, "w")
            mutualFile.truncate(0)

            for follower in mutual:
                mutualFile.write(follower + "\n")

            mutualFile.close()

            print("Fans list saved!")
    elif choice == '2':
        fans = list(set(followersList).difference(set(followeesList)))
        print("\nNumber of people that you don't follow back: " + str(len(fans)))
        print("Fans: " + str((', '.join(fans))))
        # print(fans)
        saveToFile = input("\nSave fans to file? (y/n): ")
        if saveToFile == "y" or saveToFile == "Y":
            fansFile = open("op-%s-fans.txt" % targetUsername, "w")
            fansFile.truncate(0)

            for follower in fans:
                fansFile.write(follower + "\n")

            fansFile.close()

            print("Fans list saved!")
    elif choice == '3':
        nonFollowers = list(set(followeesList).difference(set(followersList)))
        print("\nNumber of people that don't follow back: " +
              str(len(nonFollowers)))
        print("Non-followers: " + str((', '.join(nonFollowers))))
        # print(nonFollowers)
        saveToFile = input("\nSave non followers to file? (y/n): ")
        if saveToFile == "y" or saveToFile == "Y":
            nonFollowersFile = open("op-%s-nonfollowers.txt" %
                                    targetUsername, "w")
            nonFollowersFile.truncate(0)

            for followee in nonFollowers:
                nonFollowersFile.write(followee + "\n")

            nonFollowersFile.close()

            print("Followers list saved!")
    else:
        print("Invalid choice! Try again.")
