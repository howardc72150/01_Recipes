# Iterates through string...

# Asks the user for a string:
recipe_name = input("What is the recipe name? ")

error = "Your recipe name has numbers in it."
has_errors = ""

# Looks at each character in string and if it's a number, complain:
for letter in recipe_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

# Gives user feedback...
if has_errors != "yes":
    print("There are no errors.")
