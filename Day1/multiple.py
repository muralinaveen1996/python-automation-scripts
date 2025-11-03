number  = int(input("Enter a number to generate it's multiplication table : "))
print(f"\nMultiplication Table for {number}\n"+"-"*30)

for i in range(1,21):
    print(f"{number} x {i} = {number * i}")