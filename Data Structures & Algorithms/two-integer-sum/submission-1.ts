class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen: Record<number, number> = {}

        let diff: number;

        for (let i=0; i < nums.length; i++) {
            diff = target - nums[i]
            if (diff in seen) {
                return [i, seen[diff]]
            }
            seen[nums[i]] = i
        }

    }
}
