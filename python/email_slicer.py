# This function slices the character after @
Gmail = input("Enter Your Gmail: ").strip()

username = Gmail[:Gmail.index('@')]
domain = Gmail[Gmail.index('@') + 1:]

print(f"Your username is : {username} & domain is : {domain}")

