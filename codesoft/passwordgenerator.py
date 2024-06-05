import random
import string


def generate_password(length, complexity):
    password = ""
    if complexity == "simple":
        chars = string.ascii_lowercase
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits
    elif complexity == "strong":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level")

    for i in range(length):
        password += random.choice(chars)

    return password


def main():
    print("Welcome to the Password Generator Tool!")

    while True:
        try:
            length = int(input("Enter the desired length of the password (min 8): "))
            if length < 8:
                print("Password length must be at least 8 characters")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        complexity = input("Enter the complexity of the password (simple, medium, strong): ")
        if complexity not in ["simple", "medium", "strong"]:
            print("Invalid complexity level. Please choose from simple, medium, or strong.")
            continue
        break

    password = generate_password(length, complexity)

    print("Generated Password: ", password)


if __name__ == "__main__":
    main()
