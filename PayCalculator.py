# Prompt the user to enter hours
try:
    sh = int(input("Enter Hours: "))
except:
    sh = int(input("No Letters Dummy! Enter Hours: "))
# Prompt the user to enter rate
try:
    sr = float(input("Enter Rate: "))
except:
    sr = float(input("No Letters Dummy! Enter Rate: "))

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

# Calculate the pay after tax (20% deduction)
st = xp * 0.8
print('Pay after tax:', st)

# Find and display the user's Owed Tax Amount
tax = xp - st

print('Taxes Owed:', tax)

# Keep the window open by prompting for additional input
input("Press Enter to exit...")
