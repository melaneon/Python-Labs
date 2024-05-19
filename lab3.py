#Melaniia Frolova
#A01391948

import random

#### LAB A ####
#### TASK 1 #####
def loan_qualifier():
    '''
    Qualify for loan based on number of years worked and annual income
    '''
    print("running loan qualifier")
    salary_cad = int(input("Enter your monthly salary:"))
    years_of_employment = int(input("Years of work experience:"))

    annual_income_cad = salary_cad * 12

    if annual_income_cad >= 50000 and years_of_employment >= 3:
        print("You qualify for a loan")
    elif annual_income_cad < 50000 and years_of_employment < 3:
        print("Your income must be at least 50,000 and you must be employed for 3 years or more.")
        print("You don't qualify for a loan.")
    elif annual_income_cad < 50000:
        print("Your income must be 50,000 or more. You don't qualify for a loan.")
    elif years_of_employment < 3:
        print("You must be employed for 3 years or more. You don't qualify for a loan.")





#### TASK 2 #####

def calculate_monthly_cell_phone_bill_charge_cad(air_time_minutes, text_messages_amount):
    '''
    Calculate monthly phone charges
    :param air_time_minutes: minutes in air time this month
    :type air_time_minutes: int
    :param text_messages_amount: messeges sent this month
    :type text_messages_amount: int
    '''
    tax_percentage = 0.05

    #basic plan
    base_plan_minutes = 50
    base_plan_messages = 50
    basic_plan_price_dollars_per_month = 15.0
    service_fee_911 = 0.44
    extra_minutes_total = 0
    extra_messages_total = 0

    #extra charges
    extra_minutes_charge = 0.25 #per each minute
    extra_message_charge = 0.15  #per each message


    if air_time_minutes < 0 or text_messages_amount < 0 or type(text_messages_amount) != int:
        print("Invalid minutes or messages amount.")
        return

    print("YOUR RECEIPT")
    print("Base charge is ", basic_plan_price_dollars_per_month)

    if air_time_minutes > base_plan_minutes:
        extra_minutes = air_time_minutes - base_plan_minutes
        extra_minutes_total = extra_minutes * extra_minutes_charge
        print("Additional minutes charge is ", extra_minutes_total)

    if text_messages_amount > base_plan_messages:
        extra_messages = text_messages_amount - base_plan_messages
        extra_messages_total = extra_messages * extra_message_charge
        print("Additional test messages charge is ", extra_messages_total)

    #print 911 charges
    print("911 service fees: ", service_fee_911)

    #calculate tax amount
    subtotal = basic_plan_price_dollars_per_month + extra_minutes_total + extra_messages_total + service_fee_911
    tax_amount = subtotal * tax_percentage
    print("Tax amount is ", tax_amount)
    total = subtotal + tax_amount
    print("Total chrage is ", total)



#### TASK 3 #####
def get_square_colour(row_number, column_char):
    '''
    Get chess board square colour
    :param row_number: chess board row number
    :type row_number: int
    :param column_char: chess board column character
    :type column_char: int
    '''

    #assign numbers to columns
    if column_char == "A" or column_char == 'a' or column_char == 'C' or column_char == 'c' or column_char == 'E' or column_char == 'e' or column_char == 'G' or column_char == 'g':
        column_number = 1
    else:
        column_number = 0

    #calculate the color
    if row_number % 2 == 0:
        if column_number % 2 == 0:
            color = "black"
        else:
            color = "white"
    else:
        if column_number % 2 == 0:
            color = "white"
        else:
            color = "black"

    print(color)


### LAB B ###
def play_chicago():
    '''
    Play Chicago Dice Game
    '''
    round = 1
    score = 0

    dice_min = 1
    dice_max = 6

    while round <= 12:
        # calculations for the next round
        round = round + 1

        dice1_score = random.randint(dice_min, dice_max)
        dice2_score = random.randint(dice_min, dice_max)
        dice_sum = dice1_score + dice2_score

        print(" ")
        print("Round: " + str(round))
        print("Dice 1 score: " + str(dice1_score))
        print("Dice 2 score: " + str(dice2_score))
        print("Total: " + str(dice_sum))

        # calculate score
        if round == dice_sum:
            print("Congrats! You earned a point!")
            score = score + 1

        print("Your score: " + str(score))
        print(" ")

        user_input = input("Do you want to play another round? Enter N for No or click Enter").upper()
        if user_input == "N":
            print("Thank you for playing! You earned ", score, " points")
            return

    print("Thank you for playing! You earned ", score, " point(s)")




def main():
    ### LAB A ###
    loan_qualifier()
    air_time_minutes = 50
    text_messages_amount = 50
    calculate_monthly_cell_phone_bill_charge_cad(air_time_minutes, text_messages_amount)
    get_square_colour(6, "g")

    ### LAB B ###
    play_chicago()


if __name__ == '__main__':
    main()
