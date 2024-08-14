import java.util.*;
/*
선행 가능한 스킬트리 구하기
1. StringBuffer를 이용해서 선행스킬에 있는 애들은 추가
    1.1 Map<Skill, List>
    1.2 values를 정렬하지 않았을 때랑 정렬했을 때 결과가 같아야함.
2. 선행스킬과 다른 구성이면 탈락
3. CBD - CCBD : 스킬 중복 x

*/


class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        Map<Character, Integer> mapping = new LinkedHashMap<>();
        for(char c : skill.toCharArray()){
            mapping.put(c, 0);
        }
        for(String st : skill_trees){
            StringBuffer sb = new StringBuffer();
            for(char c : st.toCharArray()){
                if(mapping.containsKey(c)){
                    sb.append(c);
                }
            }
            // System.out.println(sb.toString());
            String output = sb.toString();
            boolean flag = true;
            for(int i = 0; i < output.length(); i++){
                if(skill.charAt(i) != output.charAt(i)){
                    flag = false;
                }
            }
            if(flag){
                answer += 1;
            }
        }
        
        return answer;
    }
}