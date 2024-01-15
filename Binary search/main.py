import time
# Find a number using binary search

# Naive search algorithm:
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target: return i
    return -1

# Binary search algorithm:
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint-1)
    else: # l[mp] < target
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    # List with ordered numbers from 1 to 10000
    l = [i+1 for i in range(10000)]

    start = time.time()
    time.sleep(1)
    naive_search(l, 9000)
    end = time.time()
    print(f'Naive search result: {end - start - 1} secs')

    start = time.time()
    time.sleep(1)
    binary_search(l, 9000)
    end = time.time()
    print(f'Binary search result: {end - start - 1} secs')