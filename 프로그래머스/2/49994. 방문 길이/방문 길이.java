import java.util.*;
/*
1. 좌표를 hashset에 저장
2. 그 길이가 처음 걸어본 길의 길이
    // 힌트
    2.1 (0, 0)-(1, 0) 과 (1,0)-(0,0) 동일 경로
3. 좌표평면 경계를 넘어가면 무시
*/
class Solution {
    Map<String, int[]> mapping = new HashMap<>();
    public int solution(String dirs) {
        mapping.put("U", new int[]{0, 1});
        mapping.put("D", new int[]{0, -1});
        mapping.put("R", new int[]{1, 0});
        mapping.put("L", new int[]{-1, 0});
        
        Set<String> route = new HashSet<>();
        String[] dirlist = dirs.split("");
        
        int[] loc = new int[]{0, 0};
        
        for(String d : dirlist){
            int newX = loc[0] + mapping.get(d)[0];
            int newY = loc[1] + mapping.get(d)[1];
            
            if(-5 <= newX && newX <= 5 && -5 <= newY && newY <= 5){                
                // 0001 0100
                // 1101 0111
                String path1 = loc[0] + "," + loc[1] + "-" + newX + "," + newY;
                String path2 = newX + "," + newY + "-" + loc[0] + "," + loc[1];
                route.add(path1);
                route.add(path2);
                
                loc = new int[]{newX, newY};         

                // System.out.println(path1 + " " + path2);

            }
            
            // System.out.println(d + " " + Arrays.toString(loc) + " " + route.size());
        }
        
        return route.size() / 2;
    }
}