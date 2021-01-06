import time
import pandas as pd
import numpy as np

#Variables Definations
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

WELCOME_MESSAGE="Hello! Welcome to Bikeshare analysis program \nLet\'s explore some US bikeshare data!"
CITY_QUESTION="What city you want to analyze or filter the data by:\n\t a. Chicago \n\t b. New York City \n\t c. washington\n\n"
CITY_ERROR="Oops, please choose the city by write the city name or the coresponding char"
CITY_CONFIRMATION="You choose to show the data for {} "
TIME_FILTER_QUESTION="Do you want to filter the data by:\n\t a. Month\n\t b. Day\n\t c. Both\n\t d. None\n"
TIME_FILTER_ERROR="Oops, please choose the time filter by write the month, day, both or none or the coresponding char"
TIME_FILTER_CONFIRMATION="You choose to filter the data by {}"
MONTH_QUESTION="What Month exactly you want to filter by \n January, February, March, April, May, June?\n"
MONTH_ERROR="Oops, please choose correct month by type the month name\n"
DAY_QUESTION="What Day exactly you want to filter by Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday ? \n"
DAY_ERROR="Oops, please choose correct day by type the full day name"
KEYBOARD_ERROR_MESSAGE= "Keyboard Interrupted so we will end the program now."

CITY_CHARS =['a','b','c']
TIME_FILTER_CHARS =['a','b','c','d']
TIME_FILTER_STRINGS =['month','day','both','none']
MONTH_FILTER_STRINGS =['january', 'february', 'march', 'april', 'may', 'june']
DAY_FILTER_STRINGS =['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
CITY_CHOICE= list(CITY_DATA.keys()) + CITY_CHARS
TIME_FILTER_CHOICE= TIME_FILTER_CHARS + TIME_FILTER_STRINGS

def get_city_filter():
    """
    Asks user to specify a city.

    Returns:
        (str) city - name of the city to analyze
    """
    city=""
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input(CITY_QUESTION).lower()
            if (city not in CITY_CHOICE ):
                print(CITY_ERROR)
            else:
                city= list(CITY_DATA.keys())[(CITY_CHOICE.index(city) %3)]
                break
        except KeyboardInterrupt:
            print(KEYBOARD_ERROR_MESSAGE)
            exit()
    print(CITY_CONFIRMATION.format(city))

    return city


def get_time_filter():
    """
    Asks user to specify time filter to analyze by.

    Returns:
        (str) time filter - type of the time filter month, day or both day and month or none for no filter
    """
    time_filter=""
    # get user input for time filter by month, day, both or none
    while True:
        try:
            time_filter = input(TIME_FILTER_QUESTION).lower()
            if (time_filter not in TIME_FILTER_CHOICE ):
                print(TIME_FILTER_ERROR)
            else:
                time_filter= TIME_FILTER_STRINGS[(TIME_FILTER_CHOICE.index(time_filter) %4)]
                break
        except KeyboardInterrupt:
            print(KEYBOARD_ERROR_MESSAGE)
            exit()
    print(TIME_FILTER_CONFIRMATION.format(time_filter))

    return time_filter

def get_month_filter():
    """
    Asks user to specify a month to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input(MONTH_QUESTION).lower()
            if (month not in MONTH_FILTER_STRINGS):
                print(MONTH_ERROR)
            else:
                break
        except KeyboardInterrupt:
            print(KEYBOARD_ERROR_MESSAGE)
            exit()
    print("you choose month {}".format(month))

    return month

def get_day_filter():
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True:
        try:
            day = input(DAY_QUESTION).lower()
            if (day not in DAY_FILTER_STRINGS):
                print(DAY_ERROR)
            else:
                break
        except KeyboardInterrupt:
            print(KEYBOARD_ERROR_MESSAGE)
            exit()
    print("you choose day {}".format(day))


    return day

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print(WELCOME_MESSAGE)

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=get_city_filter()

    # get user input for time filter by month, day, both or none
    time_filter=get_time_filter()
    if time_filter == 'month':
        # get user input for month (all, january, february, ... , june)
        month=get_month_filter()
        day='all'
    elif time_filter == 'day':
        month='all'
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day=get_day_filter()
    elif time_filter == 'both':
        # get user input for month (all, january, february, ... , june)
        month=get_month_filter()
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day=get_day_filter()
    else:
           month='all'
           day='all'


    print('-'*40)
    return city, month, day




def main():
        city, month, day = get_filters()
        print("city choosed:" + city)
        print("month choosed:" + month)
        print("day choosed:" + day)




if __name__ == "__main__":
	main()
