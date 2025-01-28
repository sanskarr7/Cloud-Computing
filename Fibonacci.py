# Generate Fibonacci sequence up to n terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci(n_terms)
