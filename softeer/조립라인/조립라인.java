import java.io.*;
import java.util.*;
/*
- 조립라인 A, B
- 각각 N개의 작업장
- 동일작업을 수행하지만 작업시간은 다를 수 있다.
- 경우에 따라 a, b 이동 가능
*/
public class Main {

    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);

        int N = sc.nextInt();

        int[][] info = new int[N][4];

        for(int i = 0; i < N; i++){
            
            int aTime = sc.nextInt();
            int bTime = sc.nextInt();

            if(i == N-1){
                info[i] = new int[]{aTime, bTime, 0, 0};

            }else{
                int aTob = sc.nextInt();
                int bToa = sc.nextInt();
    
                info[i] = new int[]{aTime, bTime, aTob, bToa};
            }
            // System.out.println(Arrays.toString(info[i]));
        }

        int[][] dp = new int[N][2];
        
        dp[0][0] = info[0][0];
        dp[0][1] = info[0][1];
        
        for(int i = 1; i < N; i++){            
            // 0(A), 1(B), 2(A-B), 3(B-A)
            // 같은 조립라인을 더하는 것과 이전 조립라인+이동시간을 더하는 것 중에 고르기
            dp[i][0] = info[i][0] + Math.min(dp[i-1][0], dp[i-1][1] + info[i-1][3]);
            dp[i][1] = info[i][1] + Math.min(dp[i-1][1], dp[i-1][0] + info[i-1][2]);
            // System.out.println(Arrays.toString(dp[i]));
        }
        
        System.out.println(Math.min(dp[N-1][0], dp[N-1][1]));
    }
}
