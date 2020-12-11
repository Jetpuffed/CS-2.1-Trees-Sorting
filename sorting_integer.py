#!/usr/bin/python3

from sorting_recursive import quick_sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    count = [0] * (max(numbers) + 1)
    for i in numbers:
        count[i] += 1
    ndx = 0
    for i, _ in enumerate(count):
        while 0 < count[i]:
            numbers[ndx] = i
            ndx += 1
            count[i] -= 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    min_n, max_n = min(numbers), max(numbers)
    buckets = [[] for _ in range(num_buckets)]
    for i in numbers:
        index = (i - min_n) // ((max_n - min_n) // num_buckets + 1)
        buckets[index].append(i)
    for i, _ in enumerate(buckets):
        quick_sort(buckets[i])
    k = 0
    for i, _ in enumerate(buckets):
        for j, _ in enumerate(buckets[i]):
            numbers[k] = buckets[i][j]
            k += 1
