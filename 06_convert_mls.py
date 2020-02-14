# Ask user for amount
# Ask user for unit
# Check that unit is in dictionary

# If unit in dictionary, convert to mL

# If no unit given/unit is unknown, leave as is.

unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

keep_going = ""
while keep_going == "":

    amount = eval(input("How much? "))
    amount = float(amount)

    unit = input("Unit? ")

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in mL {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q")