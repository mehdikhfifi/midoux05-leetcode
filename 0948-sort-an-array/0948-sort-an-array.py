import copy
from typing import List

def compareSiblings(i, nums):
    """
        Compare siblings takes an index into the array and returns 
        the index that represents the sibling to the index that 
        contains the maximum value in the array.
    """
    if i == 0:
        return 0
    # if i is odd it does not have a sibling so we return its value
    if i % 2 == 1:
        return i
    if nums[i] > nums[i-1]:
        return i
    return i - 1

def swapParent(i, nums):
    """
        Swap parent swaps the value at index i with its parent if it is bigger than 
        parent.
    """
    parent = (i - 1) // 2
    if nums[i] > nums[parent]:
        swap(i, parent, nums)
        return i
    return parent

def nextIndex(i):
    """
        Next index returns the right-most index of the next pair of siblings to     
        consider
    """
    if i % 2 == 1:
        return i - 1
    return i - 2

def leftChild(parent):
    return parent * 2 + 1

def rightChild(parent):
    return parent * 2 + 2

def bubbleDown(i, nums, heapSize):
    """
        Bubble down takes the root of the heap and places it in its correct position
        in the heap. It does this by swaping a parent with the bigger value of its 
        two children until it is no longer smaller than either of its children.
    """
    while leftChild(i) < heapSize:
        rightMostChild = rightChild(i) if rightChild(i) < heapSize else leftChild(i)
        bigger = compareSiblings(rightMostChild, nums)
        if nums[bigger] <= nums[i]:
            return
        swap(bigger, i, nums)
        i = bigger

def swap(i, j, array):
    """
        Swaps the elements at the index i and j in the array
    """
    tmp = array[j]
    array[j] = array[i]
    array[i] = tmp

def heapify(nums):
    """
        Heapify starts at the last leaf, compares itself to its sibling and then 
        swaps the larger of their values with their parent if either is bigger than
        the parent. It then moves on to the next sibling pair until it is at the 
        root.
    """
    i = len(nums) - 1
    while i > 0:
        bigger = compareSiblings(i, nums)
        parent = swapParent(bigger, nums)
        bubbleDown(parent, nums, len(nums))
        i = nextIndex(i)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
            We take the approach of HeapSort. Specifically, we treat the array 
            as if it represents a binary heap, which means it is a complete, 
            binary tree. We then run a process to promote the maximum value in 
            the heap to the top of the tree. We do this by looking at all leaves
            and comparing them to their parents. If one of the leaves is bigger 
            than their parent, we take the maximum element from the pair of leaves
            and we swap it with its parent. If we swap the parent, we bubble the 
            parent down until it is in the correct portion of the tree. We then 
            continue this for the next layer of nodes, until we get to the root node. 
            When we have reached the root node, we remove this element from the heap 
            by swapping it with the last leaf in the heap and decreasing the size of 
            the heap by one. This puts the element at the end of the array. We then 
            bubble down the root to its appropriate position in the heap, and repeat 
            this process until the size of the heap is zero. At this point, the 
            resulting array is sorted.
        """
        heapSize = len(nums)
        heapify(nums)
        while heapSize > 1:
            swap(0, heapSize - 1, nums)
            bubbleDown(0, nums, heapSize - 1)
            heapSize -= 1
        return nums