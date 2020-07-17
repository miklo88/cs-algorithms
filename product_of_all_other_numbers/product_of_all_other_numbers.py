'''
Input: a List of integers
Returns: a List of integers
'''
'''
UPER NOTES
so you're given an array.
for every index in that array you must use a certain 
multiplication pattern to return that indexs value 
so you have to do some super tricky math here. 
example array of [1,7,3,4] 
you would multiply each value in this array like so
[7*3*4,1*3*4,1*7*4,1*7*3] so the pattern is obv when you see it
"breakdown" this is where i talk to myself in my room.
arr[1, 7, 3, 4]
   arr[0]start=[1][2][3]
   start arr[1] 7*3*4 = 84 mult all but index0
   then arr[2] 1*3*4 = 12 mult all but index1
   then arr[3] 1*7*4 = 28 mult all but index2
   then arr[0] 1*7*3 = 21 mult all but index3
so while you are on a specific arr[index] you multiply everything BUT itself.
   a couple thoughts. slicing the array. 'to start' arr[1:]
   so you multiply everything in the arr EXCEPT that specific index your pointing at.
   
   current = current index
   loop over the data. index by index in the arr.
   so if at currentIndex mult what is before :0 and after 0: it
   store that to [] so you can get [120,60,40,30,24]

# arr = [1, 2, 3, 4, 5]

1 2*3*4*5 = 120
2 1*3*4*5 = 60
3 1*2*4*5 = 40
4 1*2*3*5 = 30
5 1*2*3*4 = 24
now how do i multiply everything up.
if on the current index. check left and right.
if numbers on left of current index, multiply them, if not check right
if nums on right multiply them and combine, multiply with left side if any.
then add that sum to a list and repeat for the next index
'''
    # for i in range(0, len(arr)):
    #     # zeros = []
    #     if arr[i] == 0:
    #         arr.remove(arr[i])
    #         arr.append(0)
def product_of_all_other_numbers(arr):
#   # Your code here
    #results of mult
    n = len(arr)
    items = []
    temp = []
    results = 1
    # locate the variable. relocate it to the front of the list.
    for i in range(n):
        current = i
        print(f'current index {current}')
        for j in range(n):
            if current != arr[j]:
                results = results * arr[j]
                print(results)
            elif current == arr[j]:
                print('equals')
                
                # arr.remove(arr[j])
                # temp = arr.remove(current)

                # items.append(current)
        print(arr)

    # arr.append(arr[0])
    # arr.remove(arr[0])
    # results.append(arr[0])
    # print('result of array',arr)
    # print('results',results)

if __name__ == '__main__':
#     # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
