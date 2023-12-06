sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step1
credit_card = input("Please enter your cedit card: ")
credit_card = credit_card.replace("-", "")
credit_card = credit_card.replace(" ", "")
credit_card = credit_card[::-1]

# step2
for x in credit_card[::2]:
    sum_odd_digits +=int(x)

# step3
for x in credit_card[1::2]:
    x = int(x)*2
    if x>=10:
        sum_even_digits += int(1+(x%10))
    else:
        sum_even_digits += x

# step4
total = sum_even_digits+sum_odd_digits

# step5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")


