import java.util.*;
/* 
- 길이가 1인 모든 단어를 포함하도록 사전 초기화
- 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
- w에 해당하는 색인번호 출력 후, w 제거
- 처리되지 않은 글자 c에 대해서 w+c에 해당하는 단어를 사전에 등록
- 다시 

*/
class Solution {
    public int[] solution(String msg) {

        String abcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Map<String, Integer> dict = new HashMap<>();
        for(int i = 0; i < abcd.length(); i++){
            dict.put(String.valueOf(abcd.charAt(i)), i+1);   
        }
        
        String[] message = msg.split("");
        ArrayList<Integer> answerList = new ArrayList<>();
        
        int current_idx = 0; 
        StringBuffer sb = new StringBuffer();
        while(current_idx < msg.length()){
            sb.append(message[current_idx]);
        
            if(!dict.containsKey(sb.toString())){
                dict.put(sb.toString(), dict.size()+1);
                sb.deleteCharAt(sb.length() - 1);
                answerList.add(dict.get(sb.toString()));
                
                sb = new StringBuffer(message[current_idx]);
            }
            current_idx += 1;
            // System.out.println(sb.toString());
        }
        if(dict.containsKey(sb.toString())){
            answerList.add(dict.get(sb.toString()));
        }
        // System.out.println(answerList);
        
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++){
            answer[i] = answerList.get(i).intValue();
        }
        return answer;
    }
}