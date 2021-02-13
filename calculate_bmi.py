def bmi(weight, height):
    bmi_amount = weight / height ** 2
    if bmi_amount <= 18.5:
        return "Underweight"
    if bmi_amount <= 25.0:
        return "Normal"
    if bmi_amount <= 30.0:
        return "Overweight"
    if bmi_amount > 30:
        return "Obese"

a = bmi(50, 1.80)
print(a)
