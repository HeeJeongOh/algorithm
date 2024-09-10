import java.util.*;
/*
- n명의 사람
- 가장 먼저 탈락하는 사람의 번호와 몇번째 차례인지
*/
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        
        Set<String> wordset = new HashSet<>();
        
        char last_letter = words[0].charAt(words[0].length()-1);
        wordset.add(words[0]);
        
        int turn = 1;

        for(int i = 1; i < words.length; i++){
            if(i % n == 0){
                turn += 1;
            }
            String w = words[i];
            // System.out.println("i: " + i + " t: " + turn + " w: " + w);

            int size = w.length() - 1;
            if(wordset.contains(w) || last_letter != w.charAt(0)){
                answer[0] =  (i % n) + 1;
                answer[1] = turn;
                break;
            }
            wordset.add(w);
            last_letter = w.charAt(size);
        }
        return answer;
    }
}