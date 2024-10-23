import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};
        int len = sequence.length;
        int start = 0, end = 0;
        int sum = sequence[0];
        
        while (start < len && end < len) {
            if (sum == k) {
                if (answer.length == 0 || (end - start) < (answer[1] - answer[0])) {
                    answer = new int[]{start, end};
                }
            }

            if (sum <= k) {
                end++;
                if (end < len) sum += sequence[end];
            } else {
                sum -= sequence[start];
                start++;
            }
        }

        return answer;
    }
}
