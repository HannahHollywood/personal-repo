from datetime import datetime

"""
QUESTION 1: STRING TEMPERATURE READ OUT
"""

# DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


# def format_temperature(temp):
#     return f"{temp}{DEGREE_SYBMOL}"


# temp_reformatted = format_temperature(30)
# print(f"The temperature today is {temp_reformatted}.")

"""
# -------------------------------------------------------------------
"""

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):

    # determine what the symbol in "DEGREE_SYMBOL" represents
    if ("C" in DEGREE_SYBMOL) or ("c" in DEGREE_SYBMOL):
        symbol = "celcius"
    elif ("F" in DEGREE_SYBMOL) or ("f" in DEGREE_SYBMOL):
        symbol = "fahrenheit"
    elif ("K" in DEGREE_SYBMOL) or ("k" in DEGREE_SYBMOL):
        symbol = "kelvin"

    # output a string that contains the temperature and degrees symbol
    return f"The temperature today is {temp} degrees {symbol}"


# # LOCAL EXAMPLE:
temp_reformatted = format_temperature(30)
print(f"{temp_reformatted}.")

print(" ")
print(" ")
print(" ")

"""
# -------------------------------------------------------------------
"""

"""
QUESTION 2: DATE CONVERTER
"""

# Practice String Splitting
# file_path = "C:/Users/Hannah/Desktop/File1"
# file = file_path.split('/')[4]
# print(file)


def convert_date(iso_string):

    # date = "2021-10-01T07:00:00+08:00"
    # expected_result = "Friday 01 October 2021"

    # Split the ISO string so we have the Date & Time separated
    # this is the same as saying: date_time_list = "2021-10-01", "07:00:00+08:00"
    date_time_list = iso_string.split("T")

    # Use the dashes ('-') as a splitting point so we get three substrings from "2021-10-01"
    # this is the same as saying: date_list = "2021", "10", "01"
    date_list = date_time_list[0].split("-")

    # we need to use int() to convert our strings into integers so we can create a DateTime object later
    # in other words: "2021" => 2021 , "10" => 10, "01" => 1
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])

    # Construct a DateTime object by supplying three arguments
    # The first argument must be the year, so we will use the variable year
    # The second argument must be the month, so we will use the variable month
    # The third argument must be the day, so we will use the variable day
    date_time = datetime(year, month, day)

    # The strftime() function is a part of a DateTime object
    # To format the date in the way we wanted it, we specify formatters per the first table in this link:
    # https: // docs.python.org/2/library/datetime.html
    # Note that the output of strftime function is a string, so we will assign that to the variable "the_date"
    # This gives us the result of the_date being "Friday 01 October 2021"
    the_date = date_time.strftime('%A %d %B %Y')

    # OUTPUT the_date to whoever called this function
    return the_date


# LOCAL EXAMPLE:
formatted_date = convert_date("2021-10-01T07:00:00+08:00")
print(f"Today is {formatted_date}.")

# #            "YYYY-MM-DDTHH:MM:SS{GMT}"
# iso_string1 = "2021-10-01T07:00:00+08:00"


# formatted_string = convert_date(iso_string1)
# print(formatted_string)

print(" ")
print(" ")
print(" ")

##########

"""
# -------------------------------------------------------------------
"""

"""
QUESTION 3: TEMP CONVERTER
"""


# def convert_f_to_c(temp_in_farenheit):
#     return (temp_in_farenheit - 32) * (5 / 9)
# # created a function that converts fhar to cels
# # temp_in_far is the parameter (starting with a fhar temp)


# # created a variable to assign to the function
# # where i have then asked the variable to use the function to convert 100 to cels
# temperature = float(convert_f_to_c(20))
# print(round(temperature, 1))
# # ^^ used a round function to round to the nearest decimal

"""
# -------------------------------------------------------------------
"""


def convert_f_to_c(temp_in_farenheit):
    # convert to float, then complete the equation
    temperature = (float(temp_in_farenheit) - 32.0) * (5.0 / 9.0)
    # output the rounded temperature
    return (round(temperature, 1))


# LOCAL EXAMPLE:
# temperature = float(convert_f_to_c(20))
# print(temperature)

"""
# -------------------------------------------------------------------
"""


def calculate_mean(weather_data):
    sum_of_list = 0
    for total in weather_data:
        sum_of_list = sum_of_list + float(total)   # Needed: float(total)

    total_mean = sum_of_list / (len(weather_data))
    return total_mean


# LOCAL EXAMPLE: #
list = [1, 6, 5, 8, 3, 9]
print(calculate_mean(list))
