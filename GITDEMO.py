user = int(input("Enter number: "))
i = 0
while user > 0:
    digit = user % 10
    i = i * 10 + user
    user//= 10
print(i) 
