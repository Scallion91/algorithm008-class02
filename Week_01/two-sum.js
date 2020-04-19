let twoSum = function(nums, target) {
    let str = '', i = 0;
    while (i < nums.length) {
        let another = String(target - nums[i]);
        if (str.lastIndexOf(another) > -1) return [str.lastIndexOf(another), i];
        str += another;
        i++
    }
}