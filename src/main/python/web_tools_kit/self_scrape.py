import instaloader


L = instaloader.Instaloader()
username = r"ansonother"
password = r"0ther1n$ta!"
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, username)
follow_list = []
for followee in profile.get_followees():
    follow_list.append(followee.username)
L.close()
print(follow_list)
stay = True
while stay:
    proceed = input("Enter an alphabetic character to end the program: ")
    stay = proceed.isalnum()
print("Program terminated ...")
