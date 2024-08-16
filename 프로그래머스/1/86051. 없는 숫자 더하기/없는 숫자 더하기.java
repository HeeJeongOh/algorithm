import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));
        int pointer = 0;
        for(int i = 0; i < 10; i++){
            if(pointer >= numbers.length){
                for(int j = i; j < 10; j++){
                    answer += j;
                }
                break;
            }
            // System.out.println(numbers[pointer] + " " + i);

            if(numbers[pointer] != i){
                answer += i;
            }
            else{
                pointer += 1; 
            }
        }
        return answer;
    }
}