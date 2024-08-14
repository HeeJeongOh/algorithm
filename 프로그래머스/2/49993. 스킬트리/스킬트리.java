import java.util.*;
/*
선행 가능한 스킬트리 구하기
[시도1]
1. StringBuffer를 이용해서 선행스킬에 있는 애들은 추가
    1.1 Map<Skill, 0>
2. 선행스킬과 다른 구성이면 탈락
3. CBD - CCBD : 스킬 중복 x

[시도2]
ㄴ 자료형을 조금더 적합한 것으로 변경
*/
class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        List<String> arrayList = new ArrayList<>(Arrays.asList(skill.split("")));
        for(String st : skill_trees){
            StringBuffer sb = new StringBuffer();
            for(char c : st.toCharArray()){
                if(arrayList.contains(String.valueOf(c))){
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