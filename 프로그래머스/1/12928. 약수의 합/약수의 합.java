import java.util.*;
/*
1. 1부터 n까지 중 나머지 0인 값 더하기
    1.1 n 최댓값이 3000이라 가능할 듯
2. dp ? 규칙을 모르겠음
3. n = 0과ㅏ 1 예외처리
*/
class Solution {
    public int solution(int n) {
        if(n == 0 || n == 1){
            return n;
        }
        
        int answer = 1 + n;
        for(int i = 2; i < n; i++){
            if(n % i == 0){
                answer += i;
            }
        }
        return answer;
    }
}