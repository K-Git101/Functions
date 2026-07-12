def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n-1) + recur_fibonacci(n-2)

num = int(input("Enter the number of terms: "))

if num <= 0:
    print("Please enter a positive integer.")

else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(recur_fibonacci(i))