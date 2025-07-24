number_1 = int(input("num_1: "))
number_2 = int(input("num_2: "))

run_num = True
full = None  # Initialize variable

while run_num:
    user_choise_1 = input("1. - 2. + 3. * 4. / 5. // 6. ** 7. %: ")

    if user_choise_1 == "1": 
        full = number_1 - number_2

    elif user_choise_1 == "2":
        full = number_1 + number_2 

    elif user_choise_1 == "3":
        full = number_1 * number_2 

    elif user_choise_1 == "4":
        if number_2 == 0:
            print("Error: Division by zero!")
            continue
        full = number_1 / number_2

    elif user_choise_1 == "5":
        if number_2 == 0:
            print("Error: Division by zero!")
            continue
        full = number_1 // number_2

    elif user_choise_1 == "6":
        full = number_1 ** number_2

    elif user_choise_1 == "7":
        full = number_1 % number_2

    else:
        print("Error: Invalid choice, try again.")
        continue  # Restart loop

    run_num = False  # Exit loop if valid choice

print("Result:", full)
input("")
