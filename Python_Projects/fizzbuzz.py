
#if a number is divisible by 3 print(fizz)
#if a number is divisible by 5 print(buzz)
#if a number is divisible by 3 and 5 print(fizzbuzz)

for i in range(101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 ==0 and i % 5 != 0:
        print("FIZZ")
    elif i % 3 != 0 and i % 5 == 0:
        print("BUZZ")
    elif i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    
