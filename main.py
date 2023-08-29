import random
from typing import Sequence, TypeVar

unsorted_list = random.sample(range(12_000), 10_000)

T = TypeVar('T', int, float)


def find_smallest(items: Sequence[T]) -> int:
    smallest_item = items[0]
    smallest_index = 0
    for i, item in enumerate(items):
        if item < smallest_item:
            smallest_item = item
            smallest_index = i
    return smallest_index


def sort_with_selection_sort(items: list[T]) -> list[T]:
    items = items.copy()
    return [items.pop(find_smallest(items)) for _ in range(len(items))]
