'''
Input: a List of integers
Returns: a List of integers
'''
'''
UPER UPER
understanding - so you have to understand that is is very vague. now i discovered the readmes in each 
folder lol
creating a function that moves the non-zeros to the left side of the array. 
order of non zero ints does not matter.
"what i need to do." i need to be able to re-order an array
"how will i do it"
you have to loop throught the array to read the values no?
if any values aren't zero they must shift to the left.
non zeros to the left, zeros to the right.
how am i going to manipulate this array?
shift? rotate? how do i move an ele to the front of an array?
if there are no zeros then do nothing with the array.
'''
def moving_zeroes(arr):
    # Your code here
    
    for i in range(0, len(arr)):
        # zeros = []
        if arr[i] == 0:
            arr.remove(arr[i])
            arr.append(0)
            # print(f'zeros is this',zeros)
        # else:
        #     pass
    return arr
    # pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")