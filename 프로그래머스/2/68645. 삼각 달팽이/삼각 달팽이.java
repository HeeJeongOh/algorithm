import java.util.*;
// /*
// - n = 밑변의 길이와 높이가 n

// 1. 재귀 함수로 생각하기
// 2. ㄴ 채우고 \ 채우기 반복
// 3. 

// */

class Solution {
    
    private void print(int[][] numbers){
        for(int[] n : numbers){
            System.out.println(Arrays.toString(n));
        }
        System.out.println();
    }
    
    public int[] solution(int n) {
        if(n == 1){ return new int[]{1}; }
        
        int total = 0;
        for(int i = 0; i < n; i++){
            total += (i+1);
        }
        
        int[][] numbers = new int[n][n];

        int size = n;
        int y = 0;
        int x = 0;
        int cnt = 1;
        
        
        while(cnt <= total && size > 1){        
            // 하강
            while(y < size && numbers[y][x] == 0){
                numbers[y++][x] = cnt++;
            }
            y--; // 마지막 y가 배열 크기 벗어났으므로 1 감소
            x++; // 다음 위치로 이동
            
            // 우측 이동
            while(x < size && numbers[y][x] == 0){
                numbers[y][x++] = cnt++;
            }
            // System.out.println("(" +  y + "," + x + ")");

            x -= 2; // 마지막 x가 배열 크기 벗어났으므로 1 감소
            y -= 1; // 다음 위치로 이동
            
            // 대각선 이동
            while(0 <= y && 0 <= x && numbers[y][x] == 0){
                numbers[y--][x--] = cnt++;
            }
            // System.out.println("(" +  y + "," + x + ")");

            y += 2; // 마지막 y와 x가 -1로 되어있으므로 2 증가
            x++; // 다음 위치로 이동
            size--; // 한 바퀴 돌았으므로 범위 축소
            // print(numbers);
        }

        // 결과를 1차원 배열로 변환
        int[] answer = new int[total];
        int idx = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(numbers[i][j] == 0){ break; }
                answer[idx++] = numbers[i][j];
            }
        }
        
        return answer;
    }
}
