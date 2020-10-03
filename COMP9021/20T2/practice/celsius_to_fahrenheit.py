# Prints out a conversion table of temperatures from Celsius to
# Fahrenheit degrees, the former ranging from 0 to 100 in steps
# of 10.


# Insert your code here
min_temperature = 0
max_temperature = 100
step = 10
# \t: A tab
print('Celsius\tFahrenheit')
# We let fahrenheit take the values
# - min_temperature
# - min_temperature + step
# - min_temperature + 2 * step
# - min_temperature + 3 * step
# ...
# up to the largest value smaller than max_temperature + step
for fahrenheit in range(min_temperature, max_temperature + step, step):
    celsius = 32 + 18 * fahrenheit / 10
    # {:10d} or {:10}: fahrenheit as a decimal number in a field
    # of width 10.
    # {:7.1f}: celsius as a floating point number in a field of
    # width 7 with 1 digit after the decimal point.
    print(f'{fahrenheit:7}\t{celsius:10.0f}')

