while True:   
    while True:    
        # Prompt the user to enter hours
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

    # Ask User if they would like to have taxes adjusted for

    try:
        ut = input('Would you like to have taxes taken out of your calculated pay? y/n ').lower()
        if ut == 'y':
            tax_rate = float(input('Enter your desired tax percentage now. Whole numbers only.'))
        else:
            print('You have committed tax fraud.')
    except:
        
        tax_rate = 1

            
                
    # Calculate overtime
    if sh > 40:
        reg = 40 * sr  # Regular pay for the first 40 hours
        otp = (sh - 40) * (sr * 1.5)  # Overtime pay for hours over 40
        xp = reg + otp  # Total pay including overtime
    else:
        reg = sh * sr
        otp = 0
        xp = reg

    # Calculate the pay before tax
    print('Regular pay:', reg)
    print('Overtime pay:', otp)
    print(' ')
    print('Total pay before tax:', xp)

    # Calculate the pay after tax
    if tax_rate != 0:
        st = xp * (1 - tax_rate / 100)  # Subtracting the tax amount from total pay
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
