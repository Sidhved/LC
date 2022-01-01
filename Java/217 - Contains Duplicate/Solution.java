// 217 - Contains Duplicate
//Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        return Arrays.stream(nums).boxed().collect(Collectors.toSet()).size() < nums.length;
    }
}