# write your code here
with open("users.json", "r") as f:
    users_dict = json.load(f)

print(len(users_dict["users"]))