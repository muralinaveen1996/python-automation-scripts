start = int(input("Enter a start number : "))
end = int(input("Enter a end number : "))

for num in range(start,end+1):
    print(f"\nTable for {num}\n" +"-"*20)
    
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")