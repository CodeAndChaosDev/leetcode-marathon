from typing import List

# Different Two Sum Solutions
class Solutions:
    @staticmethod
    def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
    
    @staticmethod
    def two_sum_binary_search(nums: List[int], target: int) -> List[int]:
        nums_with_indices = [(num, idx) for idx, num in enumerate(nums)]
        nums_with_indices.sort()
        for i, (num, original_idx) in enumerate(nums_with_indices):
            complement = target - num
            left, right = i + 1, len(nums_with_indices) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums_with_indices[mid][0] == complement:
                    return [original_idx, nums_with_indices[mid][1]]
                elif nums_with_indices[mid][0] < complement:
                    left = mid + 1
                else:
                    right = mid - 1
        return []

    @staticmethod
    def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Test Cases
test_cases = [
    {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
    {"nums": [-2, -5, 12, 1, 20, 2], "target": 0, "expected": [0, 5]},
    {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
    {"nums": [3, 3], "target": 6, "expected": [0, 1]},
]

# Test Runner
if __name__ == "__main__":
    solutions = [
        Solutions.two_sum_hashmap,
        Solutions.two_sum_binary_search,
        Solutions.two_sum_bruteforce
    ]
    for i, test in enumerate(test_cases, 1):
        nums, target, expected = test["nums"], test["target"], test["expected"]
        print(f"Test Case {i}: nums={nums}, target={target}")
        for solution in solutions:
            result = solution(nums.copy(), target)
            print(f"  {solution.__name__} -> {result} {'✅' if result == expected else '❌'}")
        print()
