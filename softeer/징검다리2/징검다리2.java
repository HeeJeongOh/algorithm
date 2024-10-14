import java.io.*;
import java.util.*;
/*
"최장 증가 수열 (LIS)"
- 징검다리 돌의 높이는 일정하지 않다.
- 개울의 서쪽에서 동쪽으로 높이가 점점 높은 돌을 밟다가 낮은 돌을 밟으면서 지나가고자한다.
- 돌의 높이가 증가하다가 감소하는 흐름을 유지하며 밟을 수 있는 돌의 최대 개수

[시도1] DP
1. 증가 따로 감소 따로 계산
2. 두개르 합했을 때 최대인 값
*/
public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] rock = new int[N];
        for(int i = 0; i < N; i++){
            rock[i] = sc.nextInt();
        }
        
        // System.out.println(Arrays.toString(rocks));   
        int[] increase = new int[N];
        for(int i = 0; i < N; i++){
            increase[i] = 1;
            for(int j = 0; j < i; j++){
                if(rock[i] > rock[j]){
                    increase[i] = Math.max(increase[i], increase[j]+1);
                }
            }
        }
        // System.out.println(Arrays.toString(increase));   

        int[] decrease = new int[N];
        for(int i = 0; i < N; i++){
            decrease[i] = 1;
            for(int j = 0; j < i; j++){
                if(rock[i] < rock[j]){
                    decrease[i] = Math.max(decrease[i], decrease[j]+1);
                }
            }
        }
        // System.out.println(Arrays.toString(decrease));   

        int maxValue = 0;
        for(int i = 0; i < N; i++){
            if(maxValue < (increase[i] + decrease[i])){
                maxValue = increase[i] + decrease[i];
            }
        }

        System.out.println(maxValue);
    }
}
