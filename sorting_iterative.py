#!/usr/bin/python3


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Time Complexity: O(n) - It iterates through the entire length of the array.
    Space Complexity: O(n) - Memory usage grows in relation to the length of the array."""
    for i, j in enumerate(items[1:]):
        if j < items[i]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Time Complexity: O(n^2) - It iterates exponentially through the length of the array.
    Space Complexity: O(1) - Memory usage does not grow because of in-place sorting."""
    while True:
        for i, _ in enumerate(items[1:]):
            if items[i + 1] < items[i]:
                items[i + 1], items[i] = items[i], items[i + 1]
        if is_sorted(items):
            break
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Time Complexity: O(n^2) - It iterates exponentially through the length of the array.
    Space Complexity: O(1) - Memory usage does not grow because of in-place sorting."""
    while True:
        for i, _ in enumerate(items[1:]):
            min = i
            if items[i + 1] < items[min]:
                min = i + 1
            if min != i:
                items[i], items[min] = items[min], items[i]
        if is_sorted(items):
            break
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    while True:
        for i, _ in enumerate(items[1:]):
            j = i
            k = items[i + 1]
            while j >= 0 and k < items[j]:
                items[j + 1] = items[j]
                j -= 1
            items[j + 1] = k
        if is_sorted(items):
            break
    return items
