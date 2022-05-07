/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let seen = new Map();
    for (let num = 0; num < nums.length; num++) {
        if (seen.has(nums[num])) {
            return true;
        }
        seen.set(nums[num]);
    }
    return false;
};