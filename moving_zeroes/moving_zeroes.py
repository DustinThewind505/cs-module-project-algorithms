'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    read = 0
    write = 0

    if arr == []:  # ====== Returns empty list is list is empty ======
        return []
    
    for i in arr:                   # ====== If the element is 0, add only to 'read' ======
        if i != 0 or i is False:
            arr[write] = arr[read]
            read += 1
            write += 1
        else:
            read += 1
        
    for zeros in range(write, len(arr)):
        arr[zeros] = 0

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")