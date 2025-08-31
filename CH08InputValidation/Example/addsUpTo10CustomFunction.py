import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers)  # Return an int form of numbers

# Prompt user until digits add up to 10
response = pyip.inputCustom(addsUpToTen)  # No parentheses after addsUpToTen
print(f"You entered: {response}")