import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():

    try:
        length = int(input("Enter the Length for Password: "))
        if length <= 0:
            print("Your length not mets or greater than zero.")
        else:
            # Here Password can be generated
            password = generate_password(length)

            # Print or Displayed Password
            print("The Generated Password: " + password)
    except ValueError:
        print("Enter lenght of Pass Again.")

if __name__ == "__main__":
    main()
