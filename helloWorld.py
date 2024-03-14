def validation_empty_input():
   user_input = input("Please input something: ").strip()
    if user_input:
        print(user_input)
    else:
        print("Sorry, but you entered nothing!")
        return validation_empty_input()


validation_empty_input()