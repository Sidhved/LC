class Solution {
    public int addDigits(int num) {
        int sum = 0;
        while(num>0){
            int d = num % 10;
            sum += d;
            num /= 10;
        }
        if(sum>9){
            int a = addDigits(sum);
            return a;
        }
        return sum;
    }
}