'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    checked_arr = []

    for num in arr:
        if num in checked_arr:
            checked_arr.remove(num)
        else:
            checked_arr.append(num)

    return checked_arr[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")