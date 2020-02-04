# Get's recipe name and checks it is not blank

# Not blank function goes here:
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response



# Main routine goes here:

recipe_name = not_blank("What is the recipe name? ")

print("You are making {}".format(recipe_name))