# calculating the effective temperature

temperature = int(input("Enter temperature in Fahrenheit :"))
wind_speed = int(input("Enter wind speed in miles per hour :"))

if temperature > 50 and (wind_speed > 120 or wind_speed < 3):
    print("invalid inputs")
else:
    effective_temperature = 35.74 + 0.6215*temperature + (0.4275*temperature - 35.75) * wind_speed**0.16
    print("the effective temperature of national weather services is : ", effective_temperature)

