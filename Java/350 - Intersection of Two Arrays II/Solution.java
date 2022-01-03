class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        if(nums1.length>nums2.length){
            return intersect(nums2,nums1);
        }
        for(int x : nums1){
            hm.put(x, hm.getOrDefault(x, 0)+1);
        }
        int k=0;
        for(int x:nums2){
            if(hm.getOrDefault(x,0)>0){
                nums1[k++]=x;
                hm.put(x,hm.get(x)-1);
            }
        }
        int ans[]=new int[k];
        for(int i=0;i<k;i++){
            ans[i]=nums1[i];
        }
        return ans;
    }
}