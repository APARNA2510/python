# to take numbers and convert in integer in a single input

numbers = list(map(int, input().split()))
print(numbers)

numbers_halfed = list(map(lambda i: int(i)/2, input('>>').split()))
print(numbers_halfed)