/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    nums = String(x)
    resrve = nums.split("").reverse().join("")
    if(nums === resrve){
        return true
    }else{
        return false
    }
    
};