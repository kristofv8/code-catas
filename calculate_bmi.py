def bmi(weight, height):
    bmi_amount = weight / height ** 2
    return bmi_amount

a = bmi(50, 1.80)
print(a)