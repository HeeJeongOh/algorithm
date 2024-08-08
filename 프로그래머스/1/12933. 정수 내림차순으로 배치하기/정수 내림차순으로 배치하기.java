import java.util.*;
// n의 각 자릿수를 큰것부터 작은 순으로 정렬
class Solution {
    public long solution(long n) {
        long answer = 0;
        
        String[] slist = String.valueOf(n).split("");
        Arrays.sort(slist);
        // System.out.println(Arrays.toString(slist));
        
        int len = slist.length;
        for(int i = 0; i < len; i++){
            answer += Integer.parseInt(slist[i]) * Math.pow(10, i);
        }
        return answer;
    }
}