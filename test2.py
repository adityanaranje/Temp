def add_user(users, name, age):
    if name not in users:
        users[name] = age
    return users


users = {}
add_user(users, "Alice", 30)
add_user(users, "Bob", "25")  # inconsistent type

for user in users:
    print(user, users[user])
