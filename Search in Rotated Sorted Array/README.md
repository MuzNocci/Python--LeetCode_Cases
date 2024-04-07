There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` ( **0-indexed** ). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of *`target`* if it is in *`nums` *, or * `-1`* if it is not in *`nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre>

**Example 2:**

<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre>

**Example 3:**

<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>

**Constraints:**

* `1 <= nums.length <= 5000`
* `-10<sup>4</sup><span> </span><= nums[i] <= 10<sup>4</sup>`
* All values of `nums` are  **unique** .
* `nums` is an ascending array that is possibly rotated.
* `-10<sup>4</sup><span> </span><= target <= 10<sup>4</sup>`
