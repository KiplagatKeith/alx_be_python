X = int(input("Enter a number to see its multiplication table: "))

for Y in range(1, 11):
    product = X * Y
    print(X, "*", Y, "=", product)
    Y += 1

