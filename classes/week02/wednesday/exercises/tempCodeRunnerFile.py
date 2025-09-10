def greet(name):
    # Capitalize the name before greeting
    name = input("Please enter your name: ")
    name = name.capitalize()
    """
    The function prints a greeting.
    By taking the user's name,
    capitalizing it, then
    including it in the message.
    """
    print(f"Hello, {name}!")
greet(" ")