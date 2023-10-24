class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set set = new HashSet();

        for(int i : nums) {
            set.add(i);
        }
        if (set.size() == nums.length) {
            return false;
        }
        else {
            return true;
        }
    }
}