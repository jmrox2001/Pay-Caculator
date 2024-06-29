# Define tax brackets based on annual income
def calculate_tax_single(weekly_income):
    tax_brackets = {11600: 0.1, 47150: .12, 100525: 0.22, 191950: 0.24, 243725: 0.32, 609350: 0.35,
        float('inf'): 0.37  # Upper bound for highest bracket
    }
    # Determine the tax rate based on the weekly income
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    # If the income exceeds the highest bracket, return the rate for the highest bracket
    return tax_brackets[float('inf')]

def calculate_tax_joint(weekly_income):
    tax_brackets = {23200: 0.1, 94300: 0.12, 201050: 0.22, 383900: 0.24, 487450: 0.32, 731200: 0.35,
        float('inf'): 0.37  
    }
    
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    return tax_brackets[float('inf')]

def calculate_tax_hoh(weekly_income):
    tax_brackets = {16550: 0.1, 63100: 0.12, 100500: 0.22, 191950: 0.24, 243700: 0.32, 609350: 0.35,
        float('inf'): 0.37  
    }
    
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    return tax_brackets[float('inf')]

# PAY CALCULATOR PROGRAM
while True:   
    # Prompt the user to enter hours
    while True:    
        try:
            sh = int(input("Enter Hours: "))
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter whole numbers only. (eg. '20')")
    # Prompt the user to enter rate    
    while True:    
        try:
            sr = float(input("Enter Rate: "))
            break
        except ValueError:
            print("Invalid input. Please enter whole numbers only. (eg. '20')")

    # Set default tax rate
    tax_rate = 0
        
        # Calculate overtime
    if sh > 40:
        reg = 40 * sr  # Regular pay for the first 40 hours
        otp = (sh - 40) * (sr * 1.5)  # Overtime pay for hours over 40
        xp = reg + otp  # Total pay including overtime
    else:
        reg = sh * sr
        otp = 0
        xp = reg
    
    # !!!!!!!!Ask User if they would like to have taxes adjusted for!!!!!!!
    try:
        ut = input('Would you like to have taxes taken out of your calculated pay? y/n ').lower()
        if ut == 'y':
            while True:
                filing_status = input("Enter your filing status (single/joint/hoh): ").lower()
                if filing_status == 'single':
                    tax_rate = calculate_tax_single(reg) 
                    break
                elif filing_status == 'joint':
                    tax_rate = calculate_tax_joint(reg) 
                    break
                elif filing_status == 'hoh':
                    tax_rate = calculate_tax_hoh(reg) 
                    break
                else:
                    print()
                    print("Invalid filing status. Please enter 'single', 'joint', or 'hoh'.")
                    print()
    
        else:                
            tax_rate = 0
    except:
        break


    # Calculate the pay before tax
    print('Weekly Pay:', reg)
    print('Overtime Pay:', otp)
    print(' ')
    print('Total pay before tax:', xp)

    # Calculate the pay after tax
    if tax_rate != 0:
        st = xp * (1 - tax_rate )  # Subtracting the tax amount from total pay
    else:
        st = xp


    print('Pay after tax:', st)

    # Find and display the user's Owed Tax Amount
    tax = xp - st
    print('Taxes Owed:', tax)

    # Add function to allow user to calculate again
    choice = input("Would you like to calculate again? (yes/no): ")
    if choice.lower() != 'yes':
        break