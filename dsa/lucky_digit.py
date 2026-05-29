input_number=int(input("enter a number to find your lucky digit:"))
print(f"number you input is {input_number}")
sum_of_digits=0
while input_number!=0:
    remainder=input_number % 10
    input_number=input_number//10
    sum_of_digits+=remainder
    if sum_of_digits>9 and input_number==0:
        input_number=sum_of_digits
        sum_of_digits=0
print(f"your lucky digit is {sum_of_digits}")
