# helpme plz
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s



def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

mph = input("Input speed in mph: ")
mph = float(mph)

print("please choose between these three options:")
print("1. Kilometers per Hour")
print("2. Meters per Second")
print("3. Feet per Second")
menuInput = input()
menuInput = float(menuInput)

if menuInput < 1 or menuInput > 3 :
    print("please try again")

if menuInput == 1 :
    print("Speed in kph is", mph_to_kph(mph))

if menuInput == 2 :
    print("Speed in m/s is", mph_to_ms(mph))

if menuInput == 3 :
    print("Speed in ft/s is", mph_to_fts(mph))

