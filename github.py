import datetime
# This is a program that asks a user for their date of birth, then prints it
Months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
Endings = ['st', 'nd', 'rd'] + 17* ['th']\
          + ['st', 'nd', 'rd'] + 7* ['th']\
          + ['st']
day = input('Day: ')
month = input('Month: ')
year =(input('Year: '))
# we now convert the day,month and year to intergers
day_number = int(day)
month_number = int(month)
Year = int(year)
# inorder to call the correct day ending and month name, we now subtract 1 from each
day_ending = Endings[day_number-1]
month_name = Months[month_number-1]
correct_day = day + day_ending
correct_day_name = datetime.date(Year,month_number,day_number)
print (month_name + ' '+ correct_day + ' '+ year + ' ' + 'which was a', correct_day_name.strftime('%a'))

