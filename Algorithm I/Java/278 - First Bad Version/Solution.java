class VersionControl{
    boolean isBadVersion(int version){
        return true;
    }
}

// The above is just place holder and pre defined in leetcode

public class Solution extends VersionControl {

    public int firstBadVersion(int n) {
        if(n == 1){
            return 1;
        }
        int begin = 1;
        int end = n;
        while(begin<end){
            int mid = begin + (end-begin)/2;
            if(isBadVersion(mid)){
                end = mid;
            }
            else{
                begin = mid + 1;
            }
        }
        return (begin);
    }
}