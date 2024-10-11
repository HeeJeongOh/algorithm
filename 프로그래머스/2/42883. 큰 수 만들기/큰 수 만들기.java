import java.util.*;
/*
1. (n-k)길이의 숫자
2. 순서는 변하지 않음

*/
class Solution {
    public String solution(String number, int k) {
        char[] answer = new char[number.length() - k];
        
        Stack<Character> stack = new Stack<>();
        for(char num : number.toCharArray()){
            while(stack.size() > 0 && stack.peek() < num && k > 0){
                stack.pop();
                k--;
            }
            stack.add(num);
            // System.out.println(stack);
        }
        
        for(int i = 0; i < answer.length; i++){
            answer[i] = stack.get(i);
        }
        return new String(answer);
    }
}