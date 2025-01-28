# Find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The largest number in the list is {find_largest(nums)}.")
