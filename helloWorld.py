try:
    user_input = input("Please input something: ").strip()
    if user_input:
        print(user_input)
    else:
        print(1 / 0)
except ZeroDivisionError:
    print("Sorry, but you entered nothing!")
