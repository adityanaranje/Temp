""
def add_user(users, name, age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if name in users:
        raise ValueError(f"User '{name}' already exists")
    users[name] = age
    return users
""


users = {}
add_user(users, "Alice", 30)
add_user(users, "Bob", "25")  # inconsistent type

for user in users:
    print(user, users[user])
