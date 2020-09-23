'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here
    # max_nums = []
    # i = 0
    # while i+k < len(nums)+1:
    #     window = nums[i:i+k]
    #     max_num = max(window)
    #     max_nums.append(max_num)
    #     print(max_num)
    #     i += 1
    # return max_nums

    window = []
    max_nums = []

    for i in range(len(nums)):
        # the first loop skips this while loop because it's empty
        # remove index at the end of window if its num is less than current number
        # this ensures that the first item in the window is always the index of the largest number in the window
        while window and nums[window[-1]] <= nums[i]:
            window.pop()
        # add the index of the current number to que
        window.append(i)
        # if the index in the front of the que is outside of the window, remove it
        if window[0] == i - k:
            window = window[1:]
        # once current index is at the end of window, add the first item in window
        if i >= k - 1:
            max_nums.append(nums[window[0]])
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
