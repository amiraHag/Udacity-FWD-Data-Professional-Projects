import time
import pandas as pd
import numpy as np

#Variables Definations
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
KEYBOARD_ERROR_MESSAGE= "Keyboard Interrupted so we will end the program now."
def display_raw_data(city):
    display_data = input('Do you want to see the raw data for city {} ? Enter yes or no \n'.format(city)).lower()
    while display_data == 'yes':
        try:
            for city_data_chunk in pd.read_csv(CITY_DATA[city], chunksize =5):
                print(city_data_chunk)
                display_data = input('Would you like to see more raw data for city {} ? Enter yes or no \n'.format(city)).lower()
                if display_data == 'yes':
                    continue
                elif display_data == 'no':
                    break
                else:
                    display_data = input('Please enter valid choice which is yes or no? ')
        except KeyboardInterrupt:
            print(KEYBOARD_ERROR_MESSAGE)



def main():
    while True:
        city, month, day = 'washington','all','all'
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
