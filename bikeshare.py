import pandas as pd
import numpy as np

def make_menu(page, choose_a):
    """Creates a menu page (i.e. 'menu_city', 'menu-time', 'menu_months') that presents users with a list of choices. This function utilizes the 'menu' dictionary to lookup values.

    INPUT:
    page: string. type of page (ie. city, month, time)
    choose_a: string. fill-in-the blank for type of choices presented to uses (ie. 'city', 'time filter', 'month filter')

    OUTPUT:
    user_input: The letter choice of the user"""

    print("\nPlease choose a {}.\n".format(choose_a).upper())
    for letter,item in menu[page]['choice'].items():
        print(("{}) {}".format(letter, item)))
    user_input= input("Enter choice: ").upper()
    if user_input not in menu[page]['choice'].keys():
         print("\nSorry! I can't seem to read this.\nCan you please type that again?\n")
         return make_menu(page,choose_a)
    return user_input


def menu_city():
    """Creates city menu and has access in sending users to another menu page depending on their choice ('Chicago', 'New York City', 'Washington').

    INPUT: none

    OUTPUT: returns a list of filters [city, time, month, dow]"""

    print("~ "*25)
    list_filters=['none', 'none', 'none', 'none']
    letter=make_menu('menu_city','city')
    choice=menu['menu_city']['choice'][letter]

    list_filters[0]=choice

    #sends users to another page depending on their choic and brings back a list of filters
    return eval(menu['menu_city']['dest'][letter]+'(list_filters)')

def menu_time(list_filters):
    """Creates time menu and has access in sending users to another menu page depending on their choice ('Month', 'Day of Week', 'Day of Week', 'No Time Filter', 'Back to City Filter').

    INPUT: list of filters

    OUTPUT: returns a list of filters [city, time, month, dow]"""

    print("~ "*25)

    #'clears' the last 3 items on the filters list and leaves only the first item which shows the city choice
    list_filters[1]="none"
    list_filters[2]="none"
    list_filters[3]="none"
    print("\nCity Choice: {}".format(list_filters[0]))
    letter=make_menu('menu_time','time filter')
    choice=menu['menu_time']['choice'][letter]

    list_filters[1]=choice

    #allows users to go back a page and reset the filter list
    if choice=='Back to City Filter':
        return eval(menu['menu_time']['dest'][letter]+'()')
    #users does not wish to have a time filter then filter list is done
    elif choice=='No Time Filter':
        return list_filters
    #sends users to next menu page depending on their filter choices
    else:
        return eval(menu['menu_time']['dest'][letter]+'(list_filters)')

def menu_month(list_filters):
    """Creates month menu and has access in sending users to another menu page depending on their choice ('January', 'February', 'March', 'April', 'May', 'June', 'Back to City Filter', 'Back to Time Filter').

    INPUT: list of filters

    OUTPUT: returns a list of filters [city, time, month, dow]"""
    print("~ "*25)

    #'clears' the last 2 items on the filters list and leaves only the first and second items which shows the city choice and time filter
    list_filters[2]="none"
    list_filters[3]="none"
    print("\nCity Choice: {}\nTime Filter: {}".format(list_filters[0], list_filters[1]))
    letter=make_menu('menu_month','month filter')
    choice=menu['menu_month']['choice'][letter]

    list_filters[2]=choice

    #allows users to go back a page and reset a section of the filter list
    if choice=='Back to City Filter':
        return eval(menu['menu_month']['dest'][letter]+'()')
    elif choice=='Back to Time Filter':
        return eval(menu['menu_month']['dest'][letter]+'(list_filters)')

    #filter list is complete and returns list
    else:
        return list_filters

def menu_dow(list_filters):
    """Creates day of week menu and has access in sending users to another menu page depending on their choice ('Sunday','Monday', 'Tuesdayy', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Back to City Filter', 'Back to Time Filter').

    INPUT: list of filters

    OUTPUT: returns a list of filters [city, time, month, dow]"""
    print("~ "*25)

    #'clears' the last 2 items on the filters list and leaves only the first and second items which shows the city choice and time filter
    list_filters[2]="none"
    list_filters[3]="none"
    print("\nCity Choice: {}\nTime Filter: {}".format(list_filters[0], list_filters[1]))
    letter=make_menu('menu_dow','day of week filter')
    choice=menu['menu_dow']['choice'][letter]

    list_filters[3]=choice

    #allows users to go back a page and reset a section of the filter list
    if choice=='Back to City Filter':
        return eval(menu['menu_dow']['dest'][letter]+'()')
    elif choice=='Back to Time Filter':
        return eval(menu['menu_dow']['dest'][letter]+'(list_filters)')
    #filter list is complete and returns list
    else:
        return list_filters


def get_filters():
    """Obtains the user's filter choices

    INPUT: none
    OUTPUT: list of filters as strings"""

    print("="*50,"\n")
    print("Greetings fellow citizens of Earth!")
    print("Welcome to our Bike Share Database where you would be about to retrieve data from various cities!")
    print("Let's begin!\n")
    return menu_city()

def find_path_most_traveled(df):
    """Finds path most traveled.

    INPUT:
    df: Data Frame

    OUTPUT: string. Statement of most popular path"""

    df_path_count=df.groupby(['Start Station', 'End Station']).size()
    max_count=df_path_count.max()
    max_path_traveled= df_path_count[df_path_count==max_count].index[0]

    start_station, end_station=max_path_traveled

    print("The most common trip from start to end: {} to {}".format(start_station,end_station))

def find_start_station_most(df):
    """Finds station most used as starting point

    INPUT:
    df: Data Frame

    OUTPUT: string. Statement of most popular starting station"""

    max_start=df['Start Station'].mode()[0]
    print("Most common start station: {}".format(max_start))

def find_end_station_most(df):
    """Finds station most used as ending point

    INPUT:
    df: Data Frame

    OUTPUT: string. Statement of most popular ending station"""

    max_end=df['End Station'].mode()[0]
    print("Most common end station: {}".format(max_end))

def pop_month(df):
    """Finds month with most counts of travels

    INPUT:
    df: Data Frame

    OUTPUT: string. Statement of most popular month"""

    pop_month=df['Month'].mode()[0]
    months=['January', 'February', 'March', 'April', 'May', 'June']
    print("The most common month is: {}".format(months[pop_month-1]))

def pop_dow(df):
    """Find most popular day of week

    INPUT:
    df: Data Frame

    OUTPUT: string. Statement of most popular day of week"""
    print("The most common day of week is: {}".format(df['Dow'].mode()[0]))

def pop_hour(df):
    """Finds most popular hour

    INPUT:
    df: Data Frame

    OUTPUT: string. Statement of most popular hour"""

    #coverts popular hour to Standard Time
    hour=df['Start Time'].dt.hour.mode()[0] %12

    #identifies if hour is AM or PM
    if hour==12:
        AMorPM="PM"
    elif hour==0:
        hour=12
        AMorPM="AM"
    elif hour/12>=1:
        hour=hour%12
        AMorPM="PM"
    else:
        AMorPM="AM"

    print("The most common hour of the day is: {}:00{}".format(hour, AMorPM))

def get_time(total_sec):
    """Converts time into days, hours, minutes, seconds

    INPUT:
    total_sec: integer. total seconds

    OUTPUT: integer. days, hours, minutes, seconds"""
    d=total_sec//(24*60*60)
    h=(total_sec//(60*60))%24
    m=(total_sec//60)%60
    s=total_sec%60
    return d,h,m,s

def get_stats(df):
    """Finds statistics under the following categories: Popuar Times of Travel, Popular Stations and Trip, Trip Duration, and User Info

    INPUT:
    df: Data Frame

    OUTPUT: string. Statements of stats"""
    print("~ "*25)
    print("\nSTATISTICS")
    #shows users their filter choices
    print("Filters: {}".format(', '.join([item for item in list_filters if item!='none'])))


    print("\nPOPULAR TIMES OF TRAVEL")
    pop_month(df)
    pop_dow(df)
    pop_hour(df)

    print("\nPOPULAR STATIONS AND TRIP")
    find_start_station_most(df)
    find_end_station_most(df)
    find_path_most_traveled(df)

    print("\nTRIP DURATION")
    total_trip=int(df['Trip Duration'].sum())

    d,h,m,s=get_time(total_trip)
    print("Total Travel Time: {} day(s) {} hour(s) {} minute(s) {} second(s)".format(d,h,m,s))

    avg_trip=int(df['Trip Duration'].mean())

    d,h,m,s=get_time(avg_trip)
    print("Average Travel Time: {} day(s) {} hour(s) {} minute(s) {} second(s)".format(d,h,m,s))

    print("\nUSER INFO")
    type_list=[]
    for type in df['User Type'].value_counts().index:
        type_list.append(" {} {} ".format(type, df['User Type'].value_counts().loc[type]))
    print("Counts For Each User Type: {}".format(",".join(type_list)))

    #if city is not NYC or Chicago then no info N/A
    if list_filters[0]!= 'Chicago' and list_filters[0]!='New York City':
        print("Gender Info: {}".format('Data Not Available'))
        print("Birth Info: {}".format('Data Not Available'))
    else:
        type_list=[]
        for type in df['Gender'].value_counts().index:
            type_list.append(" {} {} ".format(type, df['Gender'].value_counts().loc[type]))
        print("Counts For Each Gender Type: {}".format(",".join(type_list)))

        min_birth=int(df['Birth Year'].min())
        max_birth=int(df['Birth Year'].max())
        common_birth=int(df['Birth Year'].mode()[0])
        print("Earlist Year of Birth: {}".format(min_birth))
        print("Most Recent Year of Birth: {}".format(max_birth))
        print("Common Year of Birth: {}".format(common_birth))

def menu_more_data(i):
    """Asks uses if would like to see more data

    INPUT:
    i: integer. Row number of data frame last shown to users

    OUTPUT: shows next 5 lines of Data Frame and repeats function if more data would be shown"""

    print('\nWould you like you see more data?')
    letter=make_menu('menu_more_data','letter')
    choice=menu['menu_more_data']['choice'][letter]

    if choice=='Yes':
        if i+5<df.shape[0]:
            print('\n',df[i:i+5])
            return eval(menu['menu_more_data']['dest'][letter]+'(i+5)')
        else:
            print('\n',df[i:])
            print('Hmm...It looks like we have reached the end of the data!\n')

def menu_ind_data():
    """Asks uses if would like to see individual data

    INPUT: none

    OUTPUT: Data Frame showing first 5 lines and sends users to next page"""

    print('\nWould you like you see the individual data?')
    letter=make_menu('menu_ind_data','letter')
    choice=menu['menu_ind_data']['choice'][letter]

    if choice=='Yes':
        print('\n',df[0:5])
        return eval(menu['menu_ind_data']['dest'][letter]+'(5)')

#dictionary for the menu containing choices and destination pages
menu={'menu_city': {'choice': {'A':'Chicago', 'B':'New York City', 'C':'Washington'},
                     'dest': {'A':'menu_time', 'B':'menu_time', 'C':'menu_time'}},
      'menu_time': {'choice': {'A':'Month', 'B':'Day Of Week', 'C':'No Time Filter', 'D':'Back to City Filter'},
                   'dest': {'A':'menu_month', 'B':'menu_dow', 'C':'Done', 'D':'menu_city'}},
     'menu_month': {'choice': {'A':'January', 'B':'February', 'C':'March', 'D':'April', 'E': 'May', 'F':'June', 'G':'Back to City Filter', 'H':'Back to Time Filter'},
                   'dest': {'G':'menu_city', 'H':'menu_time'}},
     'menu_dow': {'choice': {'A':'Sunday', 'B':'Monday', 'C':'Tuesday', 'D':'Wednesday', 'E': 'Thursday', 'F':'Friday', 'G':'Saturday','H':'Back to City Filter', 'I':'Back to Time Filter'},
                 'dest': {'H':'menu_city', 'I':'menu_time'}},
     'menu_ind_data': {'choice': {'A':'Yes', 'B':'No'},
                      'dest': {'A':'menu_more_data'}},
     'menu_more_data': {'choice': {'A':'Yes', 'B':'No'},
                      'dest': {'A':'menu_more_data'}}}

while True:
    #list [city,time,month,dow]
    list_filters=get_filters()
    filename="{}.csv".format(list_filters[0].lower().replace(' ','_'))
    df=pd.read_csv(filename)

    #creates Month and Day of Week column
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month']=df['Start Time'].dt.month
    df['Dow']=df['Start Time'].dt.weekday_name

    #filters Data Frame according to user's input
    if list_filters[3]!='none':
        df=df[df['Dow']==list_filters[3]]
    if list_filters[2]!='none':
        month=list(menu['menu_month']['choice'].values()).index(list_filters[2])+1
        df=df[df['Month']==month]


    #with filtered Data Frame, shows users the stats
    get_stats(df)

    #ask users if wants to see individual data
    df.drop(df[['Unnamed: 0','Month','Dow']], axis=1, inplace=True)
    menu_ind_data()

    print('\nWould you like to head back to the main menu?\nA) Yes\nB) No')
    choice=input('Please choose a letter: ').upper()
    while choice!='A' and choice!='B':
        print("\nSorry! I can seem to read this.\nCan you please type that again?\n")
        print('\nWould you like to head back to the main menu?\nA) Yes\nB) No')
        choice=input('Please choose a letter: ').upper()

    #if user does not wish to go back to main menu then quit program
    if choice=='B':
        break

print('\nFarewell Earthlings!')
