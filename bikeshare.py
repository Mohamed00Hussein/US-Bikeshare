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
    while True :
        city=input('please,enter the name of the city(chicago or new york city or washington)to analyze: ').lower()
        if not city in ['chicago','new york city','washington'] :
            print('invalid input,try again')
            continue
        break
        # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month=input('please,enter the name of the month(all, january, february, ... , june) to filter by, or "all" to apply no month filter: ').lower()

        if not month in ['january','february', 'march', 'april', 'may', 'june','all'] :
            print('invalid input,try again')
            continue
        break
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day=input('please,enter the name of the day of week(all, monday, tuesday, ... sunday) to filter by, or "all" to apply no day filter: ').lower()
        if not day in ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ,'sunday','all'] :
            print('invalid input,try again')
            continue
        break
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print("ps:filter affects the result..\n")
    # TO DO: display the most common month
    commonM=df['month'].mode()[0]
    months = ['january','february', 'march', 'april', 'may', 'june']
    print("the most common month is",months[commonM-1])
    # TO DO: display the most common day of week
    commonD=df['day_of_week'].mode()[0]
    print(commonD)
    # TO DO: display the most common start hour
    commonST=df['Start Time'].mode()[0]
    print(commonST)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonSS=df['Start Station'].mode()[0]
    print("most common start station is ",commonSS)
    #print(df['Start Station'].value_counts(commonSS))
    ss=len(df[df['Start Station']==commonSS])
    print(ss,'counts')

    # TO DO: display most commonly used end station
    commonES=df['End Station'].mode()[0]
    print("most common end station is ",commonES)
    es=len(df[df['End Station']==commonES])
    print(es,'counts')
    # TO DO: display most frequent combination of start station and end station trip
    #commonSES=df['Start Station'].mode()[0]
    print("most common trip is",)
    #print("under testing boy,hold on")
    print(df.groupby(['Start Station','End Station']).size().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print('the total trips duration:',total_time,'seconds')
    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('the average trip duration:',mean_time,'seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the users types: ')
    print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df :
        Gender = df['Gender'].value_counts()
        print('the users genders: ')
        print(Gender)
    else :
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth' in df :
        Birth = df['Birth Year'].value_counts()
        print('the birth years of users: ')
        print(Birth)
    else :
        print('Birth years cannot be showed because this data is not provided in the dataframe')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df) :
    """The user will  ask you to show some rows of data upon request.
    """
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while True :
        if view_data == 'yes' :
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else :
            print('thank you Sir for using our program')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
