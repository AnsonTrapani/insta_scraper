from instagramy import InstagramUser

user = input("Input the Instagram account username: ")
user_object = InstagramUser(user)


def get_follower_count():
    print("Number of followers:", user_object.number_of_followers)


def get_followed_by():
    print(user_object.followed_by_viewer)


def get_followee_count():
    print(user_object.number_of_followings)
