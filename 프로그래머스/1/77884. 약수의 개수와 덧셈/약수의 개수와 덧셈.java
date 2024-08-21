class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int n = left; n < right+1; n++){
            // 약수 개수 더하기
            int cnt = 0;
            for(int i = 1; i <= n; i++){
                if(n % i == 0){
                    cnt += 1;
                }
            }
            // 짝수 홀수 경우 나누기
            if(cnt % 2 == 0){
                answer += n;
            }else{
                answer -= n;
            }
        }
        return answer;
    }
}