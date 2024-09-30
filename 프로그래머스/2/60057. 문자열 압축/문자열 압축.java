import java.util.*;
/*
- 반복되는 문자의 개수와 반복되는 값으로 표현하기
- 1개 이상의 단위로 잘라 압축
- 문자열은 제일 앞부터 정해진 길이만큼 자르기

[시도1] output 그대로 저장 실패 1 / 31
[시도2] 길이만 저장으로 변경 실패 12 / 31
*/

class Solution {
    public int solution(String s) {
        int answer =  1001;
        
        int len = s.length();
        if(len == 1){
            return 1;
        }
        for(int size = 1; size < len; size++){
            StringBuffer output = new StringBuffer();
            // int output = 0;
            
            String before = s.substring(0, size);
            int cnt = 1;
            int start = size;
            for(start = size; start < len-size; start += size){
                String current = s.substring(start, start+size);
                if(before.equals(current)){
                    cnt += 1;
                }
                else{
                    if(cnt == 1){
                        output.append(before);
                        // output += before.length();
                    }else{
                        output.append(cnt+before);
                        // output += (1 + before.length());

                    }
                    before = current;
                    cnt = 1;
                }
            }
            String current = s.substring(start, len);
            if(before.equals(current)){
                cnt += 1;
                output.append(cnt+current);                        
                // output += (1 + before.length());


            }
            else{
                if(cnt == 1){
                    output.append(before);
                    // output += before.length();

                }else{
                    output.append(cnt+before);
                    // output += (1 + before.length());

                }
                output.append(current);
                // output += current.length();
            }
            if(output.length() < answer){
                answer = output.length();
            }
            // if(output < answer){
            //     answer = output;
            // }
            // System.out.println(output.length() + " " + output.toString());
        }
        
        return answer;
    }
}