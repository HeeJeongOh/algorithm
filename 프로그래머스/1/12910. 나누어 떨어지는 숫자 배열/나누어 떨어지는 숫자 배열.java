import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int n : arr){
            if(n % divisor == 0){
                answer.add(n);
            }
        }
        if(answer.size() == 0){
            return new int[]{-1};
        }
        int[] array_answer = answer.stream().mapToInt(i -> i).toArray();
        Arrays.sort(array_answer);
        return array_answer;
        
    }
}