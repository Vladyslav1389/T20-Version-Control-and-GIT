def validation_empty_input() -> str:
    while True:
        user_input = input("Please input something: ").strip()
        if user_input:
            print(user_input)
            return user_input
        else:
            print("Sorry, but you entered nothing!")


validation_empty_input()
