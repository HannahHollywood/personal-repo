"""
Name: weather.py
Date: 12/12/21
Version: 1.0
Author: Hannah-Beth Hannah-Becker

Purpose:
This is a library that allows the caller to supply weather related data
in the form of Python Lists and Strings. The called function will then
export a return value that represents transformed data.

Issues:
- Opportunities to write more functions to remove duplicate code
- Variable naming could be more consistent
- Functions should have pseudo code to assist with usage

Reflection on Assignment:
> I overcomplicated a lot of questions through a lack of understanding
  and then revisited work as the assignment went on.
> Felt a bit time poor, particularly with Q8 & Q9.
> I learnt about Pseudo Code which I found helped me solve Q6-Q8,
  as my frustrations became less about the problem and more about my lack
  of experience with Python.
> My Google-Fu has improved a lot!

"""

import csv
from datetime import datetime

# Constants
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


# Question 1


def format_temperature(temp):

    # output a string that contains the temperature and degrees symbol
    return f"{temp}{DEGREE_SYBMOL}"


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 2


def convert_date(iso_string):

    # Split the ISO string so we have the Date & Time separated
    date_time_list = iso_string.split("T")

    # Split the date up into year, month, and day using '-'
    # Essentially, create a list for each part of the ISO string
    date_list = date_time_list[0].split("-")
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])

    # Couldn't find any other way to do this, so used Object creation:
    # Construct a DateTime object using year, month, and day vars
    date_time = datetime(year, month, day)

    # Format the output using dark magic (a format string found called .strftime that works with datetime objects)
    the_date = date_time.strftime('%A %d %B %Y')

    return the_date


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 3


def convert_f_to_c(temp_in_farenheit):
    # convert to float, then complete the equation
    temperature = (float(temp_in_farenheit) - 32.0) * (5.0 / 9.0)
    # output the rounded temperature
    return (round(temperature, 1))


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 4


def calculate_mean(weather_data):

    # start by creating a sumoflist variable to totals 0
    sum_of_list = 0

    # for the total in the weaterdata list += the (floated) total
    for total in weather_data:
        sum_of_list += float(total)

    # divide the total sumoflist by the length of the weatherdata to find mean
    # use (len(weatherdata)) to avoid issues with strings
    total_mean = sum_of_list / (len(weather_data))
    return total_mean


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 5


def load_data_from_csv(csv_file):

    # open 'a' csv_file
    with open(csv_file) as csv_file:
        # create variable called csv_reader
        # ask the csv to read 'to the csv file'
        csv_reader = csv.reader(csv_file)

        # skip the first line in CSV file that contains headings
        csv_reader.__next__()

        # create a variable to immitate the contents of the list
        csv_contents = []

        # for each line in the file being read
        for line in csv_reader:

            # Enclose everything in an IF statement because one of the files has empty lines between data
            # Skip over empty lines (see: example_two.csv) [if the length of the line is NOT equal to 0 then...]
            if(len(line) != 0):

                # Firstly need to separate each index in the CSV file's current line because of differing data types
                temperature_date = line[0]

                # Convert temperature readings from String => Int
                min_temp = int(line[1])
                max_temp = int(line[2])

                # This is "sanitised" because data is in the test's expected format
                sanitised_line = [temperature_date, min_temp, max_temp]

                # Build out the "clean" csv_contents list using sanitised line for output purposes
                csv_contents.append(sanitised_line)

        # Export the assembled "clean" list to the caller
        return csv_contents


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 6


def find_min(weather_data):

    # create variables for the following:
    index_position = 0
    lowest_index = None
    lowest_value = None

    # Specify != 0 because we know length is positive when the list has stuff in it
    if(len(weather_data) != 0):

        for current_value_q1 in weather_data:

            # Avoid issues where we have mixed ints, strings, and floats
            current_value_q1 = float(current_value_q1)

            # Do this for the first index because we do not have anything to compare to
            if(lowest_value is None):
                lowest_value = current_value_q1
                lowest_index = 0

            elif(current_value_q1 <= lowest_value):
                lowest_value = current_value_q1
                lowest_index = index_position

            # Increment by one to keep track of where we are in the list
            index_position += 1

        # Create a tuple
        min_value = (lowest_value, lowest_index)

    else:

        # Caller expects an empty tuple if an empty list was supplied
        min_value = ()

    return min_value


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 7


def find_max(weather_data):

    # create variables for the following:
    index_position = 0
    maximum_index = None
    maximum_value = None

    if(len(weather_data) != 0):
        for current_value in weather_data:

            # convert to float to avoid issues with str, int, floats
            current_value = float(current_value)

            if(maximum_value is None):
                maximum_value = current_value
                maximum_index = 0

            elif current_value >= maximum_value:
                maximum_value = current_value
                # this then means it's the index_position of the max number in the list
                maximum_index = index_position

            index_position += 1

        max_value = (maximum_value, maximum_index)

    # Return an empty tuple if weather_data contained nothing
    else:
        max_value = ()

    return max_value


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 8
# I ran out of time to write functions here for duplicate code
# E.g.: could use a function that finds a temperature value if specified as low or high


def generate_summary(weather_data):

    number_of_days = len(weather_data)

    # Find the average lowest/highest temperature and format
    lowest_temp_list = []
    highest_temp_list = []

    # Avoid loss of precision by retaining temp in Fahrenheit until conversion necessary
    for day in weather_data:
        lowest_temp_list.append(int(day[1]))
        highest_temp_list.append(int(day[2]))

    # Find the lowest temperature value and its date
    # Temperature is a tuple of format: (temp_value, index (where we found the value in weather_data))
    # Where "index" represents where the lowest_temp is within weather_data
    #  -> weather_data[index] = a day of the week
    #  -> weather_data[index][n] = the day's value (n=0: date string; n=1: min_value; n=2: max_value)
    temperature = find_min(lowest_temp_list)
    lowest_temp = temperature[0]
    date_index = temperature[1]
    lowest_temp = convert_f_to_c(str(lowest_temp))
    lowest_temp = format_temperature(lowest_temp)
    # Get the actual date of the lowest temp from weather_data and assign it to lowest_temp_date
    lowest_temp_date = weather_data[date_index][0]
    # Take the ISO string and convert it into required format
    lowest_temp_date = convert_date(lowest_temp_date)
    # Delete temporary values so we can re-use safely later
    del temperature, date_index

    # Find the highest temperature value and its date, refer previous comment for info.
    temperature = find_max(highest_temp_list)
    highest_temp = temperature[0]
    date_index = temperature[1]
    highest_temp = convert_f_to_c(str(highest_temp))
    highest_temp = format_temperature(highest_temp)
    highest_temp_date = weather_data[date_index][0]
    highest_temp_date = convert_date(highest_temp_date)
    del temperature, date_index

    # Find the average lowest temp; this could probably be a function too
    avg_lowest_temp = calculate_mean(lowest_temp_list)
    avg_lowest_temp = convert_f_to_c(avg_lowest_temp)
    avg_lowest_temp = format_temperature(avg_lowest_temp)
    del lowest_temp_list

    # Find the average highest temp
    avg_highest_temp = calculate_mean(highest_temp_list)
    avg_highest_temp = convert_f_to_c(avg_highest_temp)
    avg_highest_temp = format_temperature(avg_highest_temp)
    del highest_temp_list

    # Create the output string; could write an "output" function to construct strings?
    weather_summary = f"{number_of_days} Day Overview\n"
    weather_summary += f"  The lowest temperature will be {lowest_temp}, and will occur on {lowest_temp_date}.\n"
    weather_summary += f"  The highest temperature will be {highest_temp}, and will occur on {highest_temp_date}.\n"
    weather_summary += f"  The average low this week is {avg_lowest_temp}.\n"
    weather_summary += f"  The average high this week is {avg_highest_temp}.\n"

    return weather_summary


"""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
"""

# Question 9


def generate_daily_summary(weather_data):

    daily_report = ""

    # Append the result of each "day" to daily_report
    for day in weather_data:
        # assign day[0] to current_day because it's the first item in the list (the ISO string)
        current_day = day[0]
        # convert the date to the readable format
        current_day = convert_date(current_day)
        # assign the formatted date to current_day
        current_day = f"---- {current_day} ----\n"
        # add this to the daily report (use += to keep adding days on to the daily summary until loop complete)
        daily_report += current_day

        lowest_temp = day[1]
        lowest_temp = convert_f_to_c(lowest_temp)
        lowest_temp = format_temperature(lowest_temp)
        lowest_temp = f"  Minimum Temperature: {lowest_temp}\n"
        daily_report += lowest_temp

        highest_temp = day[2]
        highest_temp = convert_f_to_c(highest_temp)
        highest_temp = format_temperature(highest_temp)
        highest_temp = f"  Maximum Temperature: {highest_temp}\n\n"
        daily_report += highest_temp

    return daily_report
