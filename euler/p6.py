sum_of_squares = 0
for num in range(1, 101, 1):
    # print("Attempt: {}".format(num))
    sum_of_squares = num**2+sum_of_squares
print(sum_of_squares)
square_of_sum = sum(range(1, 101, 1))**2
print(square_of_sum)
print(square_of_sum-sum_of_squares)
