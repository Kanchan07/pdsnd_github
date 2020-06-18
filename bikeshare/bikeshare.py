import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Name the city you would like to analyze? \n> ').lower()
        if city not in CITY_DATA:
            print('I am unable to find!')
        else:
            print('You looked up for: ', city)
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input ('Which month would you like to analyze? \n> '  ).lower()
        if month not in ('all','january','february', 'march', 'april', 'may', 'june'):
            print('Sorry! Please look for months from January to June or either all')
        else:
            print('You looked up for: ', month)
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    Days=('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input ('Which day would you look into for your analysis? \n> ').lower()
        if day not in Days:
            print('Sorry! I did not understand your inout. Please look for days from monday to sunday or either all')
            continue
        else:
            print('-'*40)
            return city, month, day
        city,month, day = get_filters()
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
    #load datafile into dataframe
    df = pd.read_csv(CITY_DATA[city])
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    #extract month from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    #extract day of the week fro Start time to create day of the week column
    df['day'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most popular day of the week:',popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: ', commonly_used_start_station)

    # TO DO: display most commonly used end station
    commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: ', commonly_used_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combination = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', commonly_used_start_station, " & ", commonly_used_end_station)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Display total time travel:', total_travel_time/86400, "Days")



    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Display mean travel time:', mean_travel_time/60, "Minutes")




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Total count of user types:', user_types_count)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('Display the counts of gender:', gender_types)
    except KeyError:
        print('No gender types data availabel')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        print('Display the earliest year of birth:',earliest_year_of_birth)
    except KeyError:
        print('Unable to find the earliest year of birth')

    try:
        most_recent_year = df['Birth Year'].max()
        print('Display the most year of birth:',most_recent_year)
    except KeyError:
        print('Unable to find the most year of birth')

    try:
        most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
        print('Display the most common year of birth:', most_common_year_of_birth)
    except KeyError:
        print('Unable to find the most year of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

  # Request user input for more data
    user_input = input('Would you like to see some data? Please enter yes or no: ').lower()
    if user_input in ('yes'):
        i = 0
    while True:
        print(df.iloc[i:i+5])
        i += 5
        see_more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
        if see_more_data not in ('yes'):
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
