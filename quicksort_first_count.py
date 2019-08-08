data = []
with open('input.txt') as datxt:
    for line in datxt:
        data.append(int(line))
import statistics
def CountQuickSort(input_data,start_idx,end_idx):
    if end_idx - start_idx > 1:
        #1 - Choose a pivot and place it at beginning
        # #1.1 - Choose a pivot
        pivot_index = start_idx
        p = input_data[pivot_index]
        # #1.2 - Swap at first location
        SwapNos(input_data,start_idx,pivot_index)
        #2 - Partition the array
        # #2.1 - Sort numbers by more or less than p
        limit_more_less_p = start_idx + 1
        for element in range(limit_more_less_p, end_idx + 1):
            if input_data[element] < p:
                SwapNos(input_data, element, limit_more_less_p)
                limit_more_less_p += 1
        #2.2 - Send pivot to its rightful position
        SwapNos(input_data,start_idx,limit_more_less_p - 1)
        #3 - Recursively call partitions of the array
        #3.1 - Call recursions
        left_count = CountQuickSort(input_data , start_idx,limit_more_less_p - 2)
        right_count = CountQuickSort(input_data , limit_more_less_p, end_idx)
        return right_count + left_count + end_idx - start_idx
    elif end_idx - start_idx == 1:
        if input_data[start_idx] > input_data[end_idx]:
            SwapNos(input_data,start_idx,end_idx)
        return 1
    else:
        return 0
def SwapNos(array,index1,index2):
    # Function performs swaps between values in index1 and index2
    if index1 != index2:
        array[index1] , array[index2] = array[index2] , array[index1]
print('Count:',CountQuickSort(data,0,len(data)-1))