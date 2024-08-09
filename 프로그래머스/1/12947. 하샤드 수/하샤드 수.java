import java.util.*;
class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        
        String[] strx = String.valueOf(x).split("");
        int sum = 0;
        for(String s : strx){
            sum += Integer.parseInt(s);
        }
        
        if(x % sum == 0){
            answer = true;
        }
        return answer;
    }
}