weight = float(input("Enter your weight: "))
measurement = input("Kg or Lbs ?: ")

Kg = 'KG'
Lbs = 'LBS'

measurement = measurement.upper()

if Kg in measurement:
    print("Your weight in Lbs is about: " + str(round(weight*2.20462)))

if Lbs in measurement:
    print("Your weight in Kg is about: " + str(round(weight * 1/2.20462)))