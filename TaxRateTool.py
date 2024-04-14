def calculate_tax_single(weekly_income):
    # Define tax brackets based on annual income
    tax_brackets = {
        11600: 0.1,
        47150: 0.12,
        100525: 0.22,
        191950: 0.24,
        243725: 0.32,
        609350: 0.35,
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
    # Define tax brackets based on annual income
    tax_brackets = {
        23200: 0.1,
        94300: 0.12,
        201050: 0.22,
        383900: 0.24,
        487450: 0.32,
        731200: 0.35,
        float('inf'): 0.37  # Upper bound for highest bracket
    }

    # Determine the tax rate based on the weekly income
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    # If the income exceeds the highest bracket, return the rate for the highest bracket
    return tax_brackets[float('inf')]

def calculate_tax_hoh(weekly_income):
    # Define tax brackets based on annual income
    tax_brackets = {
        16550: 0.1,
        63100: 0.12,
        100500: 0.22,
        191950: 0.24,
        243700: 0.32,
        609350: 0.35,
        float('inf'): 0.37  # Upper bound for highest bracket
    }
    
    # Determine the tax rate based on the weekly income
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    # If the income exceeds the highest bracket, return the rate for the highest bracket
    return tax_brackets[float('inf')]

def main():
    while True:
        try:
            weekly_pay = float(input("Enter your weekly pay: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        filing_status = input("Enter your filing status (single/joint/hoh): ").lower()
        if filing_status in ['single', 'joint', 'hoh']:
            break
        else:
            print("Invalid filing status. Please enter 'single', 'joint', or 'hoh'.")

    if filing_status == 'single':
        tax_rate = calculate_tax_single(weekly_pay)
    elif filing_status == 'joint':
        tax_rate = calculate_tax_joint(weekly_pay)
    elif filing_status == 'hoh':
        tax_rate = calculate_tax_hoh(weekly_pay)
    
    print('')
    print('')
    print(f"Filing status: {filing_status}")
    print('')
    print('')
    print(f"Your tax rate based on ${int(weekly_pay)}/week is: {tax_rate * 100}%.")

if __name__ == "__main__":
    while True:
        main()
        print('')
        print('')
        choice = input("Would you like to calculate again? (yes/no): ").lower()
        if choice != 'yes':
            break
