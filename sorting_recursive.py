#!/usr/bin/python3


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    result = []
    while items1 and items2:
        if items1[0] <= items2[0]:
            result.append(items1[0])
            items1 = items1[1:]
        else:
            result.append(items2[0])
            items2 = items2[1:]
    while items1:
        result.append(items1[0])
        items1 = items1[1:]
    while items2:
        result.append(items2[0])
        items2 = items2[1:]
    return result


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    pivot = items[low]
    i, j = low - 1, high + 1
    while True:
        i += 1
        while items[i] < pivot:
            i += 1
        j -= 1
        while items[j] > pivot:
            j -= 1
        if i >= j:
            return j
        items[i], items[j] = items[j], items[i]


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low is None and high is None:
        return items
    if len(items) <= 1:
        return items
    if low < high:
        p = partition(items, low, high)
        quick_sort(items, low, p)
        quick_sort(items, p + 1, high)
