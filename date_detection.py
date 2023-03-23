import re

'''
Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it’ll have a leading zero.
'''

date = re.compile(r'''(^
(0?[1-9] | [12][0-9] | 3[1]) #[12][0-9] respectively 10 or 29
/
(0?[1-9]|1[0-2])   #1-12 month
/
(1[0-9][0-9][0-9]|2[0-9][0-9][0-9]) #1000-2999 year
$)''',re.VERBOSE)

searchdate = '29/12/2020'
mo = date.findall(searchdate)


'''Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date.
April, June, September, and November have 30 days,
February has 28 days, and the rest of the months have 31 days.
February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divisible by 100,
unless the year is also evenly divisible by 400. '''

# Group the regex and sub it into variables in a loop
#for days in mo:


def isLeapYear(year):
      
        if((year % 4 == 0) or (year % 4 == 0 and year % 100 == 0  and year % 400 == 0)):
            print('this is a leap year: ' + str(year))
            return True
        else:
            return False
   

months = {'30':['04','06','09','11'],
          '28':['02']}

def checkMonth(month):
        val = '';
        for key, list_of_months in months.items():
         if month in list_of_months:
                val = key
                break
        else:
               val = '31'
        return val



def isValidDate(date):
    
    if (isLeapYear(int(date[3])) and int(date[1]) <= 29):
            return True
            
    elif  (date[1] <= checkMonth(date[2]) ):
            print('check Month of day: ' + str(checkMonth(date[2])))
            return True
          
    else:
            return False
           
matches = []
def checkDate(matchedObject):
    if(len(matchedObject) > 0):
        for day in matchedObject:
            if(isValidDate(day)):
                matches.append(day[0])
                print('The date is: ' + day[0])
            else:
                print('not a valid day')
    else:
          print('not a valid day')



checkDate(mo)  

