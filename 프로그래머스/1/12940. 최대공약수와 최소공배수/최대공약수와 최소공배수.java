class Solution {
    public int[] solution(int n, int m) {
        int maxn = 1;
        for(int i = Math.max(n, m); 0 < i; i--){
            if(n % i == 0 && m % i == 0){
                n = n / i;
                m = m / i;
                
                maxn *= i;
            }
        }
        int minn = maxn * n * m;
        return new int[]{maxn, minn};
    }
}