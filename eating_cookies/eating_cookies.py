'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = {}):
    # Your code here
    cache = cache if not isinstance(cache, list) else {}

    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
          
    sum_of_n = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    cache[n] = sum_of_n
    return cache[n]
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
