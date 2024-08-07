import java.util.*;
/*
- n*m 땅
- 여러 덩어리의 석유
- 시추관을 수직으로 뚫어 가장 많은 석유 뽑기

0    0 0 0 1 1 1 0 0    
1    0 0 0 0 1 1 0 0
2    2 2 0 0 0 1 1 0
3    2 2 2 0 0 0 0 0
4    2 2 2 0 0 0 3 3

1. 석유 그룹핑 _ oilSizeMap
    {1: 7, 2: 8, 3: 2}
2. 각 행별로 그룹핑 된 덩어리 수 기록 - cntByColMap
    {0: [2], 1: [2], 2: [2] 3: [1], 
     4: [1], 5: [1], 6: [1, 3], 7: [3]}  
    
*/
class Solution {
    private static int[] dy = {1, -1, 0, 0};
    private static int[] dx = {0, 0, 1, -1};
        
    public int solution(int[][] land) {
        
        int n = land.length;
        int m = land[0].length;
        
        int group = 2;
        
        Map<Integer, Integer> oil_size_map = new HashMap<>();
        Map<Integer, Set<Integer>> count_by_col_map = new HashMap<>();
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(land[i][j] == 1){
                    int cnt = 0;
                    
                    Deque<int[]> stack = new ArrayDeque<>();
                    stack.add(new int[]{i, j});
                    land[i][j] = group;
                    
                    while(stack.size() > 0){
                        int[] rc = stack.pollLast();
                        cnt += 1;
                        
                        Set<Integer> tmp = new HashSet<>();
                        if(count_by_col_map.containsKey(rc[1])){
                            tmp = count_by_col_map.get(rc[1]);
                        }
                        tmp.add(group);
                        count_by_col_map.put(rc[1], tmp);                     

                        for(int d = 0; d < 4; d++){
                            int r = rc[0] + dy[d];
                            int c = rc[1] + dx[d];
                            
                            if(0 <= r && r < n && 0 <= c && c < m && land[r][c] == 1){
                                land[r][c] = group;
                                stack.add(new int[]{r, c});
                            }
                        }
                    }              
                    oil_size_map.put(group, cnt);
                    group += 1;

                }
            }
        }
        

        // for(int i = 0; i < n; i++){
        //     System.out.println(Arrays.toString(land[i]));
        // }
        // System.out.println(oil_size_map);
        // System.out.println(count_by_col_map);
        
        int answer = 0;
        
        for(Integer key : count_by_col_map.keySet()){
            int sum = 0;
            for(Integer value : count_by_col_map.get(key)){
                sum += oil_size_map.get(value);                
            }
            if(sum > answer){
                answer = sum;
            }
        }
                
        return answer;
    }
}