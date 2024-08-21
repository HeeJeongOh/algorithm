import java.util.*;
// 대문자는 소문자보다 작은 것
/* StringBuffer 함수 활용
    char[] ch = s.toCharArray();
    Arrays.sort(ch);
    StringBuffer st = new StringBuffer(String.valueOf(ch));
    st.reverse();
    return  st.toString();
*/
class Solution {
    public String solution(String s) {
        StringBuffer answer = new StringBuffer();
        
        String[] slist = s.split("");
        Arrays.sort(slist);
        
        for(int i = slist.length-1; 0 <= i; i--){
            answer.append(slist[i]);
        }
        
        return answer.toString();
    }
}