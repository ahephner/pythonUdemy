#input()allows user to pass info  in
#Input() gives us a string which can be an issue with math

#round()- rounds down give number first then , how many places

print('how many kilometers did you cycle today?')
km = input()
miles = float(km)/1.60934
miles = round(miles, 2)
print(f"Your {km} ride was {miles} in miles")

