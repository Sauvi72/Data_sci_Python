print("hello")

-------------------------------

a = 0 

while a<10:
    print(a)
    a = a + 1


--------------------------------

# using for loop

for i in range(1, 50):
    if (i % 2 == 0):
        print("EVEN",i)
        
    else:
        print("ODD",i)

---------------------------------

a=3

if a%2==0:
  print("even")
else:
    print("odd")



---------------------------------

a = 0 

while a<10:
    print(a)
    a = a + 1




----------------------------------

# check PALINDROME


s = input("Enter text: ")

n = len(s)

left = 0
right = n - 1

is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

----------------------------------------
# IMPORTANT 

# a & b
# a/b = decimal \value
# a//b = integer value
# a**b = a^b



----------------------------------------




