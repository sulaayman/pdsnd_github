# PROGRAMMER: Sulaiman Owodunni
# DATE CREATED: 22/05/2020
# REVISED DATE:
# PURPOSE:
#
#
# Edit for refactoring branch



import time
import pandas as pd
import numpy as np
from datetime import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new-york': 'new_york_city.csv',
              'washington': 'washington.csv' }

today = datetime.now()

def get_filters(city, month, day, fullname):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello '+ fullname +'! Let\'s explore some US bikeshare data! ' + today.strftime("%d of %b,%Y ") + '\n')

    print('To start kindly input your details below. ')
    

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("please select city for data required.(Cities are chicago, new-york, washington)?\n").split(": ")[0].lower()
        #Loop to check if selected city is a value in CITY_DATA
        try:
            #if city does not exist         
            if city not in CITY_DATA:
                print("{} is an invalid location. Kindly pick from the list provided above again".format(city))
                continue
            # it exist continue
            else:
                break
        except ValueError as e:
            print("Exception occurred: {}".format(e))
                     
                
    # TO DO: get user input for month (all, january, february, ... , june)
    '''
        FOR THE MONTH,
        This TO DO is used to check is data exist based on a month filter.
        
        If the month selected exist, user should be able to proceed to the next 
        and get data for the specified month.
        
        If no month selected, all data for the city should be gotten.
        
        If month selection is wrong there should be a validation and warning of the 
        expected outcome and user should be taken to the previous step again.
        
        FOR A DAY,
        
        If the month selected exist, user should be able to proceed to the next 
        and get data for the specified month.
        
        If no month selected, all data for the city should be gotten.
        
        If month selection is wrong there should be a validation and warning of the 
        expected outcome and user should be taken to the previous step again.
    '''
    #custom filter created.
    filters = {
                'month',
                'day',
                'all'
               }

    while True:
        option = input("Month, day, or all?\n").lower()
        try:
            #if city does not exist         
            if option not in filters:
                print("{} is an invalid location. Kindly pick from the list provided above again".format(option))              
            elif option == 'month':
                month = input("Which month?\n January, February, March, April or June?\n").lower()
                months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
                day = 'all'
                while True:
                    # condition to check if input month exist
                    if month not in months:
                        print("{} is an invalid month selection. Kindly pick from the list provided above again".format(month))  
                        month = input("Which month?\n January, February, March, April or June?\n").lower()
                    # it exist continue
                    else:
                        break
                break
            elif option == 'day':
                day = input("Select a day from sunday to saturday and all: \n").lower()
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
                month = 'all'
            
                while True:
                    # condition to check if input day exist
                    if day not in days:
                        print("{} is an invalid day selection. Kindly pick from the list provided above again\n".format(day))
                        day = input("Select a day from sunday to saturday and all: \n").lower()
                    # it exist continue
                    else:
                        break
                break
            elif option == "all":
                month = input("Which month?\n January, February, March, April or June?\n").lower()
                months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
                
                while True:
                    if month not in months:
                        print("\n{} is an invalid day selection. Kindly pick from the list provided above again\n".format(day))
                        month = input("Which month?\n January, February, March, April or June?\n").lower()
                    else:
                        break
                   
                print("Now which day do you want to explore?\n")
                day = input("Select a day from sunday to saturday and all: \n").lower()
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
                
                while True:
                    if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                        print("{} is an invalid day selection. Kindly pick from the list provided above again\n".format(day))
                        day = input("Select a day from sunday to saturday and all: \n").lower()
                    else:
                        break
                break    
            
        except ValueError as e:
            print("Exception occurred: {}".format(e))

    print('')                     
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # condition to check month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
 
    # condition to check month if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('\nMost Popular Start Hour:', popular_month)
    print('')
    # TO DO: display the most common day of week
    
    df['month'] = df['Start Time'].dt.weekday_name
    popular_dow = df['day_of_week'].mode()[0]
    print('\nMost Popular Start Hour:', popular_dow)
    print('')
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('\nMost Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
 
    print('Most Common Start Station:', popular_start)
    print('')
 
    # TO DO: display most commonly used end station

    popular_end = df['End Station'].mode()[0]
 
    print('Most Common End Station:', popular_end)
    print('')
 
    # TO DO: display most frequent combination of start station and end station trip

    df['combo'] = df['Start Station'] + ' to ' + df['End Station']
    popular_station = df['combo'].mode()[0]
 
    print('Popular Combination:', popular_station)
    print('')
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()
 
    print('Total Travel Time:', total_trip_time)
    print('')

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
 
    print('Mean/Average Travel Time:', mean)
    print('')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, fullname ):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # count the number of rows on the user column
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Counts of gender:', gender)
        print('')
    else:
        print("There is no Gender information in {} city!".format(city))
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_birth_year = df['Birth_Year'].min()
        print('Earliest Birth Year:', earliest_birth_year)
        print('')
        recent_birth_year = df['Birth Year'].max()
 
        print('Recent Birth Year:', recent_birth_year)
        print('')
 
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Popular Birth Year:', common_birth_year)
        print('')
    else:
        print("Birth year information is not available for this city!")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)
    print("\n This data was requested by: " +fullname+ " on the "+ today.strftime("%d of %b,%Y ") )


def raw_data(df):
    """ Displays 5 rows of raw data at a time """
    data_row = 0
    print("\n Will you like to see raw data?\n")
    response = input("Yes or no?\n").lower()
    option  = ['yes', 'no']
    if response not in option:
        print("\nInvalid / unknown response\n")
        response = input("Yes or no?\n").lower()
    elif response == 'yes':
        while True:
            data_row += 5
            print(df.iloc[data_row : data_row + 5])
            print("\n Will you like to more raw data?\n")
            continues = input("Yes or no?\n").strip().lower()
            if continues == 'no':
                break
    elif response == 'no':
        return
  


def requesters_information(fullname):
    firstname = input("Please enter firstname?\n").split(": ")[0].lower()
    print("")
    lastname = input("Please enter lastname?\n").split(": ")[0].lower()
    print("")

    fullname = firstname.capitalize() +" "+ lastname.capitalize()
    print(fullname+"\n")
    print("")
    print('-'*40)
    return fullname
    
    
def main():
    city = ""
    month = 0
    day = 0
    fullname= ""


    while True:
        fullname = requesters_information(fullname)
        
        city, month, day = get_filters(city, month, day, fullname)
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city, fullname)
        raw_data(df)
        
#         with open('output.txt', 'w') as f:
#             print('Filename:', filename, file=f) 
#         file = open("sample.txt","w")
#         file.write(ri)
#         file.close()
        #customer satisfaction.
        satisfaction = input('\n {} are you satisfied with the data processed? Enter yes or no.\n'.format(fullname))
        if satisfaction.lower() != 'yes':
            complaint = input('\n Kindly tell us your complaint.\n')
            print('complaint has been noted. Thank you ')
            break
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                print('Thank you for using out services')
                break


if __name__ == "__main__":
	main()
