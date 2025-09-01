from typing import List
from utils.utils import timeit

@timeit
def has_duplicate(nums: List[int]) -> bool:
    # using built-in objects
    return len(nums) != len(set(nums))

@timeit
def has_duplicate_v2(nums: List[int]) -> bool:
    # using data structures
    seen = {}
    for num in nums:
        key = str(num)
        if key in seen: return True
        seen[key] = True
    return False