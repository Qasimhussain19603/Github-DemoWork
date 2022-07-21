import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
<<<<<<< HEAD
        """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare Information!')
    #Initializing an empty city variable to store city choice from user
    #You will see this repeat throughout the program
=======
    print('Hello! Let\'s explore some US bikeshare Information!')
    print('\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
>>>>>>> refactoring
    city = ''
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Enter the Name of the City (chicago, new york city, washington): ').lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month=''
    while month not in ['all', 'january', 'february','march', 'april', 'may' , 'june']:
        month = input('Enter the Month Name from the First Six Months or Enter all: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']:
        day = input('Enter the Day of the Week or Enter all: ').lower()

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
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['Day'] = df['Start Time'].dt.strftime('%A').str.lower()
    df['Hour'] = df['Start Time'].dt.strftime('%H')
    if day != 'all':
        df = df[df['Day'] == day]
        
    if month != 'all':
        df = df[df['Month'] == month]
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df.groupby('Month').size().idxmax())

    # TO DO: display the most common day of week
    print(df.groupby('Day').size().idxmax())

    # TO DO: display the most common start hour
    print(df.groupby('Hour').size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df.groupby('Start Station').size().idxmax())

    # TO DO: display most commonly used end station
    print(df.groupby('End Station').size().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print(df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df.groupby('Trip Duration').size().idxmax())

    # TO DO: display mean travel time
    print(df.groupby('Trip Duration').mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print ('Information on Gender Not Available')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth year' in df:
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())
        print(df['Birth Year'].mode())
    else: 
        print('Information on Birth Year Not Available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to Restart the program? Enter yes or no: ')
        if restart.lower() != 'yes':
            break
        print('-'*40)
        print("\n")


if __name__ == "__main__":
	main()