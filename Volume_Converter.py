print('what would you like to convert gallons or liters')
convert = input()
if convert == "gallons":
    print('how many gallons would you like to convert into liters')
    gallons = int(input())
    liters = gallons * 3.8
    print(liters)
elif convert == "liters":
    print('how many would you like to convert liters to gallons?')
    liters = float(int(input()))
    gallons = liters / 3.8
    print(gallons)
else:
    print('thats not what i asked')
