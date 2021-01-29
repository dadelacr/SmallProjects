import instaloader
import os
"""This is a version of the code I made to work entirely within the terminal without having to edit the code."""
#Get instance
L = instaloader.Instaloader()

#Login - Insert User @
USER = input("Enter Instagram username: ")

L.interactive_login(USER)
#This will ask for password on terminal

profile = instaloader.Profile.from_username(L.context, USER)
#Loads up Instance for the User once logged in


LastShortcode = input("Please enter the shortcode of the last post you wish to download \nIf you wish to download all saved photos, press enter: ")
#Comes after Instagram.com/p/
#https://www.instagram.com/p/SHORTCODE/etc.

if LastShortcode == False:
    LastShortcode = "a"
#Giving a dummy variable if no shortcode is given

FolderName = input("Enter Foldername (if a folder does not already exist, it will be created): ")

for post in instaloader.Profile.get_saved_posts(profile):
    if post.shortcode == LastShortcode:
        L.download_post(post, FolderName)
        break
        #Download is Inclusive of the Last Shortcode
    else:
        L.download_post(post, FolderName)

### Comments and Descriptions are also downloaded, the following code is to remove the unwanted files ###
dir_name = FolderName
Directory = os.listdir(dir_name)

for item in Directory:
    if item.endswith(".txt") or item.endswith(".json") or item.endswith(".json.xz"):
        os.remove(os.path.join(dir_name, item))

