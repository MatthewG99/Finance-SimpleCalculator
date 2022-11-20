"""
We import the 'math' library as per instructions
By doing this, we could use the functions from this library
The entire list of functions can be found here:
https://docs.python.org/3/library/math.html
"""
import math

"""
I used the print function to print the instruction for the user, then 
the program will wait for the user's input.

When we are taking the input from the user:
    The only 3 options are:
        1. Investment
        2. Bond
        3. If the user types something else, a message will appear and the
        programme will end
"""
print("Choose either 'investment' or 'bond' from the menu below to proceed: :")
print()  # Empty line so it will look clean

# We print the available options: investment & bond
print("investment - to calculate the amount of interest you'll earn on your investment\n"
      "bond       - to calculate the amount you'll have to pay on a home loan")

"""
We are taking the user's input
I've used the .casefold() method as the input is case sensitive.
The casefold method allow the user to enter the available input and 
ignore the capital letters
E.g. if the input is Bond - the program should stop because it's waiting
for 'bond' as input. However, if we use .casefold(), python will ignore
the capital letter and will still consider the input as available 
"""
user_choice = input('Please enter your choice: ').casefold()

"""
If the user's input is 'investment' then we are printing few other inputs as below
"""
if user_choice == 'investment':

    # The amount of money that are deposited by the user
    money_to_deposit = int(input('Please enter the amount of money you are depositing: '))

    # The interest rate
    # It's a float as the interest might have decimals (e.g 2.5, 3.1 etc)
    interest_rate = float(input('Please enter the interest rate as a percentage %: '))

    # We are dividing the interest rate by 100 as we need the percent
    interest_rate = interest_rate / 100

    # The amount of years the user is planning to invest:
    years_of_investing = int(input('Please enter the number of years you are planning to invest: '))

    """
    Now we are printing the 2 types of interest the user got to choose:
        simple & compound 
    """
    # We are taking the input from the user: simple or compound
    # Again, we are using the .casefold() method as the input might start with capital letter.
    interest = input('Please choose between simple or compound interest: ').casefold()

    # If the user's input is 'simple' then the program will follow the 'simple' given formula (from the instructions)
    if interest == 'simple':
        total_amount = money_to_deposit * (1 + interest_rate * years_of_investing)

    # Else if the input is 'compound' then the program will follow the compound given formula (from the instructions)
    elif interest == 'compound':
        total_amount = money_to_deposit * math.pow((1 + interest_rate), years_of_investing)
    total_interest = total_amount - money_to_deposit

    print()  # Blank line so it will be some space between the input and the output
    print('***' * 26)  # Printing some stars - not needed but it looks better

    # Printing the output based on the user's choice.
    print(
        f"You choose to deposit {money_to_deposit} based on {interest_rate * 100}% interest and {years_of_investing} "
        f"years of investment. \n"

        # We also round it and limit the decimals at 2 as it's not necessary to
        # show all the decimals
        f"The total is: ${round(total_amount, 2)}\n"

        # This wasn't requested, but I thought it's handy to include.
        # It will print the total interest (total_amount - money_to_deposit)
        # We also round it and limit the decimals at 2 as it's not necessary to
        # show all the decimals
        f"The total interest is ${round(total_interest, 2)}")

    print('***' * 26)  # Printing some stars - not needed but it looks better


# Else, if the user's input is 'bond' - we are requesting another set of inputs from the user
elif user_choice == 'bond':
    # Take the present value of the house from the user
    present_house_value = int(input('Please enter the present value of the house: '))

    # Take the interest rate from the user
    # It's a float as the interest might have decimals (e.g 2.5, 3.1 etc)
    interest_rate = float(input('Please enter the interest rate: '))
    # We are dividing the interest rate by 100 as we need the percentage
    interest_rate = interest_rate / 100

    # We are dividing the interest by 12 months to calculate the monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # We are taking the input from the user - the total months
    months_to_repay = int(input('Please enter the number of months you are planning to take to repay: '))

    # We are calculating the monthly repay by using the given formula ( from the instructions)
    money_each_month = (monthly_interest_rate * present_house_value) / (
            1 - (1 + monthly_interest_rate) ** (-months_to_repay))

    print()  # Printing a blank line so it will look clean

    # We are printing the output - total money to repay
    # We also round it and limit the decimals at 2 as it's not necessary to
    # show all the decimals
    print(f"You will have to repay ${round(money_each_month, 2)} monthly")

# I also included an else statement -
# If the user's input is not a valid option,
# the below message will be printed
else:
    print(f'"{user_choice}" is not a valid option')
