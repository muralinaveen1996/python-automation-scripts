total = 0
for num in range(1,101):
    if num % 2 ==0:
        total += num

print("sum of even numbers from 1 to 100 is:",total)

#short cut version.
total = sum(range(2,101,2))
print(total)
