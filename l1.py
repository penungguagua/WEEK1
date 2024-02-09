import random
import math
import time
import datetime
    
# pending with question. need to brush up more on 
"""
what is pending 
1.question 7
2.need to brush up more on variable

correct method below
y = z 
x = z

confusing method which is my method below
z = y
x = z

3.need to brush up on time
1 hour = 60 mins
after1 hour = 

55 mins = 0.91 hours
60 mins = 1 hour


60 second = 1 min
3,300 seconds = 55 mins
= 1320 mins

4.need to brush on //

5.need to brush up %

6.need to brush up on formatholder. take email as an examples

variable name format()
-got place holder {}
what it does?
-format the specified value
-enter the string's placeholder
-can either use variable or format

so 
email = aishahmalekx@gmail.com
print('To', email)

or

sendemailaddress = "To : {email} ".format(email=aishahmalekx@gmail.com)



"""


# below is what i need to learn
# Get current time input
current_hour = int(input("Enter current hr: "))
current_minute = int(input("Enter current min: "))
current_second = int(input("Enter current sec: "))

# Calculate total seconds and add 1 hour
total_seconds = current_hour * 3600 + current_minute * 60 + current_second + 3600

# Calculate updated time without using if statements
new_hour = total_seconds // 3600 % 24
new_minute = total_seconds // 60 % 60
new_second = total_seconds % 60

# Display the original and updated time
print("Clock time is {:02d}:{:02d}:{:02d}".format(current_hour, current_minute, current_second))
print("After 1 hour, the time is {:02d}:{:02d}:{:02d}".format(new_hour, new_minute, new_second))



# answer to question 4 lecturer's method
number = int(input('Enter seconds in integer'))
seconds = number % 60 # convert to seconds
minutes = number // 60 % 60 # convert to minutes. 60 % 60 cause minutes. if hours it's just one time 
hours = number // 3600 % 24 # convert to hours

#display result
print(hours, "hr, ", minutes, "mins and ", seconds, "seconds")



""""
below is my method
convertchgto50centOutput = int(math.remainder(convertchgto50cent, 50))
convert50centto10cent= int(math.remainder(convertchgto50centOutput, 10))
convert50centto10centoutput= int(math.remainder(convert50centto10cent, 5))
lastchg=int(math.remainder(convert50centto10centoutput, 1))
"""""

print(
    '50 cent :', convertchgto50cent,
    '10 cent :', convertchgto50centremainder
)




#question 2
""""
2. Write a program that reads 3 numbers and displays the sum and average of
these 3 numbers.
"""
no1, no2, no3 = 1,2,3

sum = no1 + no2 + no3
print(sum)
average = sum / 3
print(average)

#question 1
""""
The formula to convert temperature in fahrenheit to centigrade is as follows:
c = 5
9 ( f − 32)
Write a program that reads an input in fahrenheit and displays the
temperature in centigrade.
"""
farenheit = input('Guess the farenheit')
chgtoSfarenheit = int(farenheit)
centigrade = (chgtoSfarenheit - 32) * 5/9.


print(chgtoSfarenheit, 'to centigrade is', centigrade) # this is crucial. need to have comma to use variable in print

#question 3
""""
3. Write a program that takes in a 3 digit integer and displays the sum and
product of the digits. E.g. if the number is 123, the sum displayed is 6 and the
product is also 6.
"""""
takeInt = 654
sumofTakeInt = int(654)


#question 4
""""
4. Write a program that reads in a positive integer representing time in seconds
and converts it to hour, minute and seconds. For example, if the input is 3670
seconds, output 1 hour, 1 minute and 10 seconds.
"""""

gettimeinseconds = input('How many seconds?')
updatedseconds = int(gettimeinseconds)
convertsecondtohours = int(updatedseconds / 3600) # lets say. if enter 3600 seconds, it will give 1. so 1 hour
convertsecondtohours2 = math.remainder(updatedseconds, 3600)
convertremaindertominutes = int(math.remainder(convertsecondtohours2, 60)) # convert to int , cause dw the output to print 0.0
convertremaindertoseconds = int(math.remainder(convertremaindertominutes, 60))


print('output is', convertsecondtohours, 'hours and', convertremaindertominutes, 'mintues and' ,convertremaindertoseconds ,'seconds')



#print('output is' final-hour ,final-minute, ', minute and' final-seconds 'seconds' )


#question 5
#incomplete
""""
5. Write a program that reads an input representing a change which is an
amount less than 1 dollar. The program calculates the change into 50, 10, 5
and 1 cent coins. The program then displays the number of each coin
required for that change. E.g.
Enter change: 47
50 dollars: 0
10 dollars: 4
5 dollars: 1
1 dollars: 2
"""
money = int(input('Balance change ')) # 1 dollar is 100 and not 1
# perlukan remainder maybe divide by
# below is cikgu nye method
fiftydollar = money // 50 
tendollar = money % 50 // 10
fivedollar = money % 50 % 10 // 5
onedollar = money % 50 % 10 % 5 // 1 
#print(fiftydollar, tendollar,fivedollar,onedollar)
print( 
    '$50 :' ,fiftydollar, "\n\n"
    '$10 :' , tendollar, "\n\n"
    '$5 :', fivedollar,"\n\n"
    '$1 :', onedollar)


#question 6
"""
6. A restaurant is offering meals at 50% discount. A service charge (10%) and
GST (7%) apply to the discounted cost. While the service charge applies to
the discounted price, note that the GST calculation is based on the total of the
discounted amount and the service charge.
Write a program that reads in the cost of the meal and displays a detailed
receipt. An example is as follows:
Enter meal amount ($): 120
Receipt
Cost of meal: $120.00
50% discount: $ 60.00
Service charge: $ 6.00
GST: $ 4.62
Total amount: $ 70.62
(Output should be formatted.)

datatype - float

discount = 0.5
serviceCharge = 0.1
GST = 0.07
GST = 0.07 x discounted meals

discounted meal = 0.5 x meal
"""

mealamount = float(input('enter meal amount'))
discountedMeal = mealamount * 0.5
serviceCharge = 0.1 * discountedMeal
gst = round(0.07 * discountedMeal * serviceCharge,2)
totalamount = round(discountedMeal + serviceCharge + gst,2)



print(
    'Attached below is your receipt :', "\n\n"
    'Enter meal amount ($) :' , mealamount, "\n\n",
    '50% discount :', '$', discountedMeal,"\n\n",
    'Service charge :', '$', serviceCharge, "\n\n",
    'GST :', '$', gst, "\n\n",
    'Total amount :', '$', totalamount ,"\n\n",
)

"""
question 7
. The area of a triangle with sides a, b, c can be determined using Heron’s
formula:
where s = ½ (a + b + c) is the semi-perimeter, or half of the triangle's
perimeter.
Write a program that reads the lengths of the sides of a triangle and displays
the area. Assume that input is valid, i.e. the sides are able to form a triangle.
Import the Math library to use the square root function

"""


"""
# question 8
the formula to compute compound interest C for a loan L at the end of n
years at i % interest per annum is as follows:
C = 𝐿 (1 + 𝑖
100)𝑛
Write a program that has 3 inputs – loan amount, duration in years and
interest rate. The program displays the compound interest based on the
formula above

l ( 1 + i // 100  ** n)
"""
#question 8
loan_amount = int(input('Enter loan amount'))
duration_in_years = int(input('Enter duration in years')) # need to be float cause can return 4.5 years
interest_rate = float(input('Enter interest rate')) # need to be float cause dealing with percentage and returning decimal places

loan_formula = loan_amount * (pow((1 + interest_rate / 100), duration_in_years))

print(loan_formula) # will return compount interest

# below is my code
getcurrenthour = int(input('Enter current hr'))
getcurrentmin = int(input('Enter current min'))
getcurrentsec = int(input('Enter current sec'))


new_seconds = getcurrentsec % 60 # convert to seconds
new_minutes = getcurrentmin // 60 % 60 # convert to minutes. 60 % 60 cause minutes. if hours it's just one time 
new_hours = getcurrenthour // 3600 % 24 # convert to hours


print('Clock time is ' , getcurrenthour, ':', getcurrentmin, ':', getcurrentsec,)
print('After 1 second the time is', getcurrenthour, ':', getcurrentmin, ':', getcurrentsec+1)
print('After 1 hour the time is', '0',new_hours, ':', getcurrentmin, ':', getcurrentsec)


weightadidah = 80 # numeric
updatedweightadidah = int(guessweightadidah)
while updatedweightadidah < 80:
    break
else:
    print('masih gemok')
    


#nak convert the below to int
updatedguess = int(guessweightadidah) # convert to string


if updatedguess > weightadidah:
    print('tolong kuruskan badan')
else:
    print('biar betul')
    



print(random.randint(0,9))

askingQuestion = input('Adakah adidah gemok?|')

if askingQuestion == 'yes':
    print('kau memang gemok')
else:
    print('kau tetap gemok')


while (weightadidah > 80):
    print('siak ah gemok pe')

    

"""
1.naming of variable
think is as nama anak kau. takkan kau nak include the below untuk nama kan anak kau
no spaces commas and special case character
cannot start with number
cannot start with -, minus infront

2.assignment
something like math (assignment)
x,y = 5,2
so x is equal to 5 and y equals to 2


3. print()
print() will visibly show , the output. print will show the output
print(chgtoSfarenheit, 'to centigrade is', centigrade) # this is crucial. need to have comma to use variable in print

4.input()
must be string

5.cannot add string and number together

6.examples of while loop can be.
selagi rahul tak datang, selagi tu kau tak leh balik

7.round (n,p)

8. \n\n -- will return a new line. will paste to another line when it prints the output

9.% will give the remainder. example 10 % 3 so it will give 1.

10.// will give the remainder. but if it is in a form of decimal then it will round up to the nearest whole number



""" 




