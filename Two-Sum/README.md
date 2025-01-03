# Two Sum Problem - Solution Testing

This project provides implementations and tests for solving the classic **Two Sum** problem using multiple algorithms. It includes a variety of approaches, from the most efficient (hashmap) to the simplest (brute force). The goal is to compare the performance and correctness of these solutions.

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

**Constraints:**
- Each input has exactly one solution.
- You may not use the same element twice.
- The solution can be returned in any order.

**Example:**

python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9



## Implemented Solutions

### 1. **Hashmap (Efficient)**
- **Time Complexity:** \(O(n)\)
- **Space Complexity:** \(O(n)\)
- Uses a dictionary to store numbers and their indices for quick lookup of complements.

### 2. **Binary Search (Efficient with Sorting)**
- **Time Complexity:** \(O(n \log n)\)
- **Space Complexity:** \(O(n)\)
- Sorts the array and uses binary search to find complements while retaining original indices.

### 3. **Brute Force (Simple but Slow)**
- **Time Complexity:** \(O(n^2)\)
- **Space Complexity:** \(O(1)\)
- Checks all possible pairs to find a match.



## Project Structure


.
├── README.md         # Project documentation
├── two_sum.py   # Python script containing solutions and test cases



## Running the Project

### Prerequisites
- Python 3.8 or higher

### Steps
1. Clone this repository:

   git clone https://github.com/CodeAndChaosDev/leetcode-marathon/tree/master/Two-Sum
   cd two-sum


2. Run the test script:
  
   python test_two_sum.py
  

### Example Output:

Test Case 1: nums=[2, 7, 11, 15], target=9
  two_sum_hashmap -> [0, 1] ✅
  two_sum_binary_search -> [0, 1] ✅
  two_sum_bruteforce -> [0, 1] ✅

Test Case 2: nums=[-2, -5, 12, 1, 20, 2], target=0
  two_sum_hashmap -> [1, 5] ✅
  two_sum_binary_search -> [1, 5] ✅
  two_sum_bruteforce -> [1, 5] ✅




## Adding New Solutions

1. Define a new method in the `Solutions` class inside `test_two_sum.py`.
2. Implement the logic for solving the Two Sum problem.
3. Add the method to the `solutions` list in the `if __name__ == "__main__":` block.



## Test Cases

The test file includes a set of predefined test cases to validate the solutions. Each test case specifies:
- **Input:** Array `nums` and `target`.
- **Expected Output:** Indices of the two numbers that sum to the target.



## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or new features.


## Author

**CodeAndChaos**  
GitHub: [@CodeAndChaosDev](https://github.com/CodeAndChaosDev)  

