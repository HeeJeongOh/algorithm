import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = -1;
        
        double tmp = Math.pow(n, 0.5);
        System.out.println(tmp);
        if(tmp == (long)(tmp)){
            answer = (long) Math.pow(tmp+1, 2);
        }
        return answer;
    }
}