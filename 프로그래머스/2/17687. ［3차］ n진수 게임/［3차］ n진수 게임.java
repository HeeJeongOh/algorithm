import java.util.*;
/*
- 숫자를 돌아가면서 말하기
    0 1 2 3 ... 1 0 1 1 1 2
- N진수로 변경하여 게임
[내시도]
1. 4
    01234
    011011100
    0 1 1 1
2. sb = 0110 , current = 3(11), total = 4
3. start = 4 ~ 4+2

[다른사람풀이]
ㄴ 불필요한 저장공간 사용 x
https://school.programmers.co.kr/questions/64995
*/
class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuffer answer = new StringBuffer();
        StringBuffer sb = new StringBuffer();
        
        boolean exit = false;
        int current = 0;
        int total = 0;
        while(true){
            if(exit == true){
                break;
            }
            String changed = Integer.toString(current, n).toUpperCase();
            sb.append(changed);

            for(int start = total; start < total + changed.length(); start++){
                if(start % m == (p-1)){
                    answer.append(sb.charAt(start));
                    
                    if(answer.length() == t){
                        exit = true;
                        break;
                    }
                }
            }
            total += changed.length();
            current += 1;
        } 
        
        // System.out.println(sb.toString());
        
        return answer.toString();
    }
}