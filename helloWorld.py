def validation_empty_input() -> str:
    """
    Validates user input for emptiness.

    :return: User input.
    :rtype: str
    """

    # Creating a while loop to ask the user continuously until the user inputs
    # something.
    while True:
        user_input = input("Please input something: ").strip()
        if user_input:
            print(user_input)
            return user_input
        else:
            print("Sorry, but you entered nothing!")


validation_empty_input()
