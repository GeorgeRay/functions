#Requirement calculate 10 different values, five values from
#fahrenheit to Celsius and five from Celsius to fahrenheit.
#Print out each calculated value.
test = "test" #this line is here to get the debugger to stop

# Convert Celsius to Fahrenheit (five variables)
def ConvertCtoF(fahrenheit):
    celsius = (fahrenheit * 1.8) + 32
    return celsius

#Convert Fahrenheit to Celsius only one variable
def ConvertFtoC(celsius):
    fahrenheit = (celsius - 32) / 1.8
    return fahrenheit

#Call the Celsius to Fahrenheit function and print
print("Fahrenheit Temps are:")
print(ConvertCtoF(100))
print(ConvertCtoF(0))
print(ConvertCtoF(30))
print(ConvertCtoF(20))
print(ConvertCtoF(10))

#Call the Fahrenheit to Celsius function and print
print("Celsius Temps are:")
print(ConvertFtoC(212))
print(ConvertFtoC(32))
print(ConvertFtoC(100))
print(ConvertFtoC(72))
print(ConvertFtoC(65))

