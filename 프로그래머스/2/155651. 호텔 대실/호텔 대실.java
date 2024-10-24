import java.util.*;
/*
- 최소한의 객실 사용
- 퇴실 시간 + 10분 후 다음 손님 가능

[시도2]
1. 입실 시간 기준으로 정렬 ?
2. record = 방의 개수
    2.1 사용 중인 방에 대해 그 방 이후에 넣을 수 있다면 갱신
    2.2 없다면 새로운 방 확보
*/
class Solution {
    public int solution(String[][] book_time) {
        int len = book_time.length;
        int[][] time = new int[len][2];
        
        for(int i = 0; i < len; i++){
            String[] start = book_time[i][0].split(":");
            String[] end = book_time[i][1].split(":");
            
            int startInt = Integer.parseInt(start[0]) * 60 + Integer.parseInt(start[1]);
            int endInt = Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1]);
            
            time[i] = new int[]{startInt, endInt};
        }
        
        Arrays.sort(time, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0];
            }
        });
        
        // for(int[] t : time){
        //     System.out.println(Arrays.toString(t));
        // }
        
        int answer = 0;

        Deque<Integer> records = new ArrayDeque<>();
        for(int i = 0; i < len; i++){
            // 방문하지 않은 곳이고, 현재 끝나는 시간보다 다음 시작시간이 나중
            boolean flag = false;
            int rm = 0;
            for(int idx : records){
                int end = time[idx][1] + 10;
                if(end <= time[i][0]){
                    records.remove(idx);
                    break;
                }
            }
            if(flag == false){
                records.add(i);
            }
            // System.out.println(records);
        }
        return records.size();
    }
}