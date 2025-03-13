import json
import os

# 🔹 Update with your extracted Instagram data folder path
DATA_FOLDER = os.getenv("DATA_FOLDER")

# Load followers list
with open(DATA_FOLDER + "followers.json", "r", encoding="utf-8") as f:
    followers_data = json.load(f)

followers = {user["string_list_data"][0]["value"] for user in followers_data if "string_list_data" in user}

# 🔹 Fix: Extract "relationships_following" from following.json
with open(DATA_FOLDER + "following.json", "r", encoding="utf-8") as f:
    following_data = json.load(f)

# If "relationships_following" exists, extract it
if "relationships_following" in following_data:
    following_data = following_data["relationships_following"]
else:
    following_data = []

following = {user["string_list_data"][0]["value"] for user in following_data if "string_list_data" in user}

print(f"Total Followers: {len(followers)}")
print(f"Total Following: {len(following)}")

# Find users who you follow but don't follow you back
not_following_back = following - followers

print("\nUsers who don’t follow you back:")
for user in sorted(not_following_back):
    print(user)

# Optional: Save to file
with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for user in sorted(not_following_back):
        f.write(user + "\n")

print("List saved to 'not_following_back.txt'")

# Find people who follow you, but you don’t follow back
ghost_followers = followers - following

print("\nGhost Followers (People who follow you, but you don’t follow back):")
for user in sorted(ghost_followers):
    print(user)

# Optional: Save to file
with open("ghost_followers.txt", "w", encoding="utf-8") as f:
    for user in sorted(ghost_followers):
        f.write(user + "\n")
print("List saved to 'ghost_followers.txt'")