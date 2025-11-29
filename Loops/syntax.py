# LOOPS
# 1. FOR LOOP
#    for var_name in ____:
#       statement
# 2. WHILE LOOP
#    while(condition):
#       

# counting the number of i in word 
word = "artificial intelligence"
count = 0
for i in word:
    if i == 'i':
        count += 1
print(count)

# vowel count in the word
count = 0
for ch in word:
    if ((ch == 'a') or (ch == 'e') or (ch == 'i') or (ch == 'o') or (ch == 'u')):
        count += 1
print(count)

# sum of n natural numbers 
n = int(input("Enter the limit to calculate sum: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)

# printing numbers in ascending or descending number
i = 1
while(i < 5):
    print(i)
    i = i + 1
while(i > 0):
    print(i)
    i -= 1

# multiplication table
n = int(input("Enter the number : "))
i = 1
while(i <= 10):
    print(n * i)
    i += 1