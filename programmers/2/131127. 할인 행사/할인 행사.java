import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        // 1. 목표 장바구니 구성
        Map<String, Integer> wantMap = new HashMap<>();
        for(int i = 0; i < want.length; i++){
            wantMap.put(want[i], number[i]);
        }
        // 2. 초기 10일치 세팅
        Map<String, Integer> currentMap = new HashMap<>();
        for(int i = 0; i < 10; i++){
            currentMap.put(discount[i], currentMap.getOrDefault(discount[i], 0)+ 1);
        }
        
        // 3. 슬라이딩 시작
        for(int i = 0; i <= discount.length - 10; i++){
            if(i > 0){
                // (In) 새로운 끝점 추가: i + 9 번째 날의 상품
                String newItem = discount[i + 9];
                currentMap.put(newItem, currentMap.getOrDefault(newItem, 0) + 1);
                // (Out) 이전 시작점 제거: i - 1 번째 날의 상품
                String outItem = discount[i - 1];
                currentMap.put(outItem, currentMap.get(outItem) - 1);
            }
            
            // 4. Map 전체를 통째로 비교
            boolean isMatch = true;
            for(String key : want){
                if(wantMap.get(key) != currentMap.get(key)){
                    isMatch = false;
                    break;
                }
            }
            if(isMatch){ answer++; }
        }
        return answer;
    }
}
