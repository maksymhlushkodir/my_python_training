
user_name = input("name")

print(f"Hello, {user_name} \nHow are you?")


user_choice = input("1 - good / 2 - not good")

if user_choice == "1":
    print("very good")

elif user_choice == "2":
    print("i am sorry")

else:
    print("ERROR")

input("")
