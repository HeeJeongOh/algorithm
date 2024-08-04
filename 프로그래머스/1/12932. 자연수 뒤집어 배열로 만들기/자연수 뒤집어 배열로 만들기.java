import java.util.*;

class Solution {
    public int[] solution(long n) {
        
        String[] numbers = String.valueOf(n).split("");
        int len = numbers.length;           
        int[] answer = new int[len];

        for(int i = 0; i < len; i++){
            answer[len-i-1] = Integer.parseInt(numbers[i]);
        }
        return answer;
    }
}