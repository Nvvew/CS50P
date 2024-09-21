from validator_collection import validators, errors

def main():
    # Prompt user for an email address
    email = input("What's your email address? ")

    try:
        # Validate the email address
        validators.email(email)
        print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()