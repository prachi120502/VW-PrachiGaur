# Telephone bill calculation program

calls = int(input("Enter number of calls: "))
bill = 200

if calls > 100:
    extra = calls - 100
    if extra <= 50:
        bill += extra * 0.60
    elif extra <= 100:
        bill += 50 * 0.60 + (extra - 50) * 0.50
    else:
        bill += 50 * 0.60 + 50 * 0.50 + (extra - 100) * 0.40

print("Total telephone bill = Rs.", bill)