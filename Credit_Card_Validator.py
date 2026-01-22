number = input("Enter Your Credit Card Number: ")

#Removing Any '-' or " " 
number = number.replace("-","")
number = number.replace(" ","")
number = number[::-1]
#Adding All digits in Odd places from right to left
Sum1 = 0
for i in number[::2]:
    Sum1 += int(i)

#Double every second digit from right to left and add them(if result is of Two Digit , add both digits and then calculate sum)
Sum2 = 0
for i in number[1::2]:
    x = int(i) *2
    if x>=10:
        x = 1 + (x%10)
    Sum2 += x

#Adding Both The Sums 
Total_Sum = Sum1 + Sum2

#If Sum is divisble By 10 Then Card Number Is Valid Else Not

if Total_Sum%10 == 0:
    print("Your Card Number Is Valid")
else:
    print("INVALID CREDIT CARD NUMBER")




