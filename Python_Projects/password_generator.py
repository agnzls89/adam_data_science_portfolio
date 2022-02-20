import random
letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'

numbers='1,2,3,4,5,6,7,8,9,0'

symbols = '!,@,#,$,%,^,&,*,(,),+'

upper_letters = letters.upper().split(',')
lower_letters = letters.split(',')
numerals = numbers.split(',')
symbol_list = symbols.split(',')

print("This is the Python Random Password Generator")
nr_cap_letters = int(input("How many upper case letters does your password require?"))

nr_low_letters = int(input("How many lower case letters does your password require?"))

nr_numbers = int(input("How many digits does your password require?"))

nr_symbols = int(input("How many symbols does your password require?"))



random_password_chars = []
for i in range(nr_cap_letters):
    random_password_chars.append(random.choice(upper_letters))
for i in range(nr_low_letters):
    random_password_chars.append(random.choice(lower_letters))
for i in range(nr_numbers):
    random_password_chars.append(random.choice(numerals))
for i in range(nr_symbols):
    random_password_chars.append(random.choice(symbol_list))
print(random_password_chars)


password = ''
for i in range(len(random_password_chars)):
    char = random.choice(random_password_chars)
    password +=char
    random_password_chars.remove(char)

print(password)
