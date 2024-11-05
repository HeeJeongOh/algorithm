import java.util.*;
/*
- 각 대기실별로 거리두기를 잘 지키고 있는지 판단

[시도1] 실패 6 / 31
1. 맨해튼 거리가 2 이내에서 있는 후보들끼리 파티션이 존재하는지 파악하기
(반례)
 0 0 p 0 0
   0 0 0 
     0

*/
class Solution {
    int[] dy = {0, 0, 0, 0, 1, 1, 1, 2};
    int[] dx = {-2, -1, 1, 2, -1, 0, 1, 0};
    
    private boolean inBoard(int y, int x){
        if(0 <= y && y < 5 && 0 <= x && x < 5){
            return true;
        }
        return false;
    }
    
    private int getDistance(int y1, int x1, int y2, int x2){
        return Math.abs(y1-y2) + Math.abs(x1-x2);
    }
    
    private boolean isPartitioned(char[][] room, int y1, int x1, int y2, int x2){
        if(y1 == y2){
            if((x1+1 < 5 && room[y1][x1+1] == 'X') || (0 < x1 && room[y1][x1-1] == 'X')){
                return true;
            }
        }
        
        else if(x1 == x2 && y1+1 < 5 && room[y1+1][x1] == 'X'){
            return true;
        }
        else if(x1+1 < 5 && room[y1][x1+1] == 'X' && y1+1 < 5 && room[y1+1][x1] == 'X'){
                return true;
        }
        else if(0 < x1 && room[y1][x1-1] == 'X' && y1+1 < 5 && room[y1+1][x1] == 'X'){
                return true;
        }
        
        return false;
        
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        int idx = 0;
        for(String[] place : places){
            char[][] room = new char[5][5];
            for(int i = 0; i < 5; i++){
                for(int j = 0; j < 5; j++){
                    room[i][j] = place[i].charAt(j);
                }
                // System.out.println(Arrays.toString(room[i]));
            }
            
            boolean flag = true;
            for(int i = 0; i < 5; i++){
                for(int j = 0; j < 5; j++){
                    if(room[i][j] == 'P'){
                        for(int d = 0; d < 8; d++){
                            int y2 = i + dy[d];
                            int x2 = j + dx[d];

                            if(inBoard(y2, x2) && room[y2][x2] == 'P'){  
                                // System.out.println("(" + i + "," + j + ")" + " " + "(" + y2 + "," + x2 + ")");

                                int dist = getDistance(i, j, y2, x2);
                                if(dist == 1){
                                    flag = false;
                                    break;
                                }
                                else if(dist == 2){
                                    // 파티션 존재 여부 확인
                                    if(!isPartitioned(room, i, j, y2, x2)){
                                        flag = false;
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
                
                if(!flag){
                    break;
                }
            }
            
            if(flag){
                answer[idx++] = 1;
            }
            else{
                answer[idx++] = 0;
            }
        }
        
        return answer;
    }
}