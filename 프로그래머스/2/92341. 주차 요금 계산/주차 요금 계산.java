import java.util.*;
/*
- 주차요금 계산하기

1. 머물은 시간을 분 단위로 계산하기
    1.1 Map<차량번호, [입차시간, 출차시간]>
    1.2 시간을 분으로 표현하기
2. 기본시간과, 단위시간 분리하기
3. 기본 요금 + 단위 요금 * 단위시간 계산하기
4. 여러 차례 입출차 가능 -> 2개의 맵 활용하기

*/
class Solution {
    private int toMinute(String time){
        String[] times = time.split(":");
        int hour = Integer.parseInt(times[0]) * 60;
        int minute = Integer.parseInt(times[1]);
        
        return hour + minute;
    }
    
    public int[] solution(int[] fees, String[] records) {
        
        Map<String, Integer> total = new TreeMap<>();
        Map<String, Integer> status = new HashMap<>();
        
        for(String rec : records){
            String[] info = rec.split(" ");
            
            // 출차 정보
            if(info[2].equals("OUT")){
                int start = status.get(info[1]);
                int end = toMinute(info[0]);
                
                total.put(info[1], total.getOrDefault(info[1], 0) + (end - start));
                status.remove(info[1]);
            }
            else{
                // 입차 정보
                status.put(info[1], toMinute(info[0]));
            }
        }
        
        int end = toMinute("23:59");
        for(String key : status.keySet()){
            int start = status.get(key);
            total.put(key, total.getOrDefault(key, 0) + (end - start));            
        }
        
        int[] answer = new int[total.size()];
        int idx = 0;
        for(String key : total.keySet()){
            int fee = fees[1];
            int stayed = total.get(key);
            
            if(stayed > fees[0]){
                fee += (Math.ceil((double)(stayed - fees[0]) / fees[2]) * fees[3]);
            }
            answer[idx++] = fee;
        }
        return answer;
    }
}