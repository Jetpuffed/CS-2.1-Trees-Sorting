#!/usr/bin/python3


# Stretch Challenges:
# [X] Extend sorting algorithms with an "order" parameter to specify ascending or descending order.
# [X] Extend sorting algorithms with a "key" parameter to specify a function to call on each item when making comparisons.
# [] Implement an insertion sort variation using binary search to find the position to insert each item. 
# [] Implement improved iterative sorting algorithms: cocktail shaker sort, library sort, or shell sort.
# [X] Annotate functions with complexity analysis of running time (operations) and space (memory usage).

def is_sorted(items, key=None, reverse=False):
    """Return a boolean indicating whether given items are in sorted order.
    Time Complexity: O(n) - It iterates through the entire length of the array.
    Space Complexity: O(n) - Memory usage grows in relation to the length of the array."""
    for i, j in enumerate(items[1:]):
        if key is not None:
            if key(j) < key(items[i]) and reverse is False or key(j) > key(items[i]) and reverse is True:
                return False
        if j < items[i] and reverse is False or j > items[i] and reverse is True:
            return False
    return True


def bubble_sort(items, key=None, reverse=False):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Time Complexity: O(n^2) - It iterates exponentially through the length of the array.
    Space Complexity: O(1) - Memory usage does not grow because of in-place sorting."""
    while True:
        for i, _ in enumerate(items[1:]):
            if key is not None:
                if key(items[i + 1]) < key(items[i]) and reverse is False or key(items[i + 1]) > key(items[i]) and reverse is True:
                    items[i + 1], items[i] = items[i], items[i + 1]
            if items[i + 1] < items[i] and reverse is False or items[i + 1] > items[i] and reverse is True:
                items[i + 1], items[i] = items[i], items[i + 1]
        if is_sorted(items, key, reverse):
            break
    return items


def selection_sort(items, key=None, reverse=False):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Time Complexity: O(n^2) - It iterates exponentially through the length of the array.
    Space Complexity: O(1) - Memory usage does not grow because of in-place sorting."""
    while True:
        for i, _ in enumerate(items[1:]):
            min = i
            if key is not None:
                if key(items[i + 1]) < key(items[min]) and reverse is False or key(items[i + 1]) > key(items[min]) and reverse is True:
                    min = i + 1
            if items[i + 1] < items[min] and reverse is False or items[i + 1] > items[min] and reverse is True:
                min = i + 1
            if min != i:
                items[i], items[min] = items[min], items[i]
        if is_sorted(items, key, reverse):
            break
    return items


def insertion_sort(items, key=None, reverse=False):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Time Complexity: O(n^2) - It iterates exponentially through the length of the array.
    Space Complexity: O(1) - Memory usage does not grow because of in-place sorting."""
    while True:
        for i, _ in enumerate(items[1:]):
            j = i
            k = items[i + 1]
            if key is not None:
                while (j >= 0 and key(k) < key(items[j])) and reverse is False or (j >= 0 and key(k) > key(items[j])) and reverse is True:
                    items[j + 1] = items[j]
                    j -= 1
            while (j >= 0 and k < items[j]) and reverse is False or (j >= 0 and k > items[j]) and reverse is True:
                items[j + 1] = items[j]
                j -= 1
            items[j + 1] = k
        if is_sorted(items, key, reverse):
            break
    return items
