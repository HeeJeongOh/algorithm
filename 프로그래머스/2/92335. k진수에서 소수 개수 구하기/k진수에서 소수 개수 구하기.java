import java.util.*;
/*
- n을 k진법으로 변환해서
- 소수의 개수 찾기 0p0, 0p, p0, p

[시도1] 런타임에러 2 / 16
1. n을 k진법 변환
2. 0을 기준으로 split
3. 10진법 기준 소수 파악하기

[시도2] 자료형 범위
1. long n = Long.parseLong(num);
2. 
*/
class Solution {
    private boolean isPrime(String num){
        long n = Long.parseLong(num);
        if(n == 1){
            return false;
        }
        for(int i = 2; i <= Math.pow(n, 0.5); i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }
    public int solution(int n, int k) {
        int answer = 0;
        // k진법 전환
        String knum = Integer.toString(n, k);
        for(String num : knum.split("0")){
            if(num.equals("")){ continue; }
            // System.out.println(num + " " + isPrime(num));
            if(isPrime(num)){
                answer += 1;
            }
        }
        return answer;
    }
}