def ASSIGNMENT(new_list, i, old_list, j):
    """
    Assigns the element from old_list[j] to new_list[i].
    """
    new_list[i] = old_list[j]

def mergeSort(list_to_sort):
    """
    Recursively splits and sorts a list using the merge sort algorithm.
    
    Parameters:
    list_to_sort (list): The list to be sorted.
    
    Returns:
    None: The list is sorted in place.
    """
    if len(list_to_sort) > 1:
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        # Recursively sort the left and right halves
        mergeSort(left)
        mergeSort(right)

        l = r = i = 0

        # Merge the sorted halves
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(list_to_sort, i, left, l)
                l += 1
            else:
                ASSIGNMENT(list_to_sort, i, right, r)
                r += 1
            i += 1

        # Copy any remaining elements of left
        while l < len(left):
            list_to_sort[i] = left[l]
            l += 1
            i += 1

        # Copy any remaining elements of right
        while r < len(right):
            list_to_sort[i] = right[r]
            r += 1
            i += 1

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Example list to sort
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    
    # Plot the unsorted list
    plt.plot(range(len(my_list)), my_list, label='Unsorted')
    plt.legend()
    plt.show()
    
    # Sort the list
    mergeSort(my_list)
    
    # Plot the sorted list
    plt.plot(range(len(my_list)), my_list, label='Sorted')
    plt.legend()
    plt.show()
