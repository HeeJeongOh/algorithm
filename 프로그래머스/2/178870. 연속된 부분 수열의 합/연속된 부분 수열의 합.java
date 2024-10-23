import java.util.*;
/*
[힌트] 투포인터

*/
class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};
        int len = sequence.length;
        int start = 0;
        int end = 0;
        
        int sum = sequence[0];
        while(start < len && end < len){
            if(sum < k){
                end += 1;
                
                if(end < len) {  // 배열 범위 체크
                    sum += sequence[end];
                }
            }
            else if(sum > k){
                sum -= sequence[start];
                start += 1;
            }
            else{
                if(answer.length > 0){
                    if(answer[1] - answer[0] > end-start){
                        answer = new int[]{start, end};
                    }
                }else{
                    answer = new int[]{start, end};
                }
                
                // end 포인터 증가
                end += 1;
                if(end < len) {  // 배열 범위 체크
                    sum += sequence[end];
                }
            }
            // System.out.println(start + "-" + end + " : " + sum);
        }
        return answer;
    }
}