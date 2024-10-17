import java.util.*;
/*
- 일렬로 나열된 n개의 집
- 모두 크기가 동일한 택배상자에 담아 배달
- 빈 상자들은 수거 가능

- i번째 집은 i거리에 위치
- 최대 cap만큼의 상자를 트럭에 실을 수 있음
- 각 집마다 배달할 상자의 개수와 수거할 상자의 개수를 알고 있으며
- 트럭 하나로 모든 배달과 수거를 마치고 돌아올 수 있는 최소 이동 거리
- 배달 및 수거 방법은 하나가 아님

1. 배달 후 수거
2. 이동 거리는 항상 배달 집 중 가장 큰 값 * 2
3. 트럭이 현재 집에서 실제로 배달할 수 있는 상자 수 계산 : Math.min(d[j], currentCap)
    3.1 현재 집에 배달해야 할 상자 수 (d[j])
    3.2 트럭의 현재 남은 용량 (currentCap)
4. 최대 거리 계산 
    4.1 배달 거리
    4.2 수거 거리

*/
import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] d, int[] p) {
        long answer = 0;
        int deliveryIndex = n - 1; // 배달할 마지막 집의 인덱스
        int pickupIndex = n - 1; // 수거할 마지막 집의 인덱스

        // 배달과 수거 작업을 모두 처리할 때까지 반복
        while (deliveryIndex >= 0 || pickupIndex >= 0) {
            // 트럭이 갈 수 있는 가장 먼 거리 (배달 또는 수거 중 더 먼 거리)
            int maxDistance = 0;

            // 배달 작업
            int currentCap = cap; // 트럭의 남은 용량
            while (deliveryIndex >= 0 && currentCap > 0) {
                if (d[deliveryIndex] > 0) {
                    int deliverAmount = Math.min(d[deliveryIndex], currentCap); // 배달 가능한 상자 수
                    
                    d[deliveryIndex] -= deliverAmount; // 배달 후 남은 상자
                    currentCap -= deliverAmount; // 트럭의 남은 용량 갱신
                    
                    maxDistance = Math.max(maxDistance, deliveryIndex + 1); // 왕복 거리 계산
                    // System.out.println("집 " + deliveryIndex + "에 " + deliverAmount + "개의 상자 배달");
                }
                if (d[deliveryIndex] == 0) {
                    deliveryIndex--; // 현재 집의 배달이 완료되면 다음 집으로 이동
                }
            }

            // 수거 작업
            currentCap = cap; // 트럭 용량 초기화
            while (pickupIndex >= 0 && currentCap > 0) {
                if (p[pickupIndex] > 0) {
                    int pickupAmount = Math.min(p[pickupIndex], currentCap); // 수거 가능한 상자 수
                    
                    p[pickupIndex] -= pickupAmount; // 수거 후 남은 상자
                    currentCap -= pickupAmount; // 트럭의 남은 용량 갱신
                    
                    maxDistance = Math.max(maxDistance, pickupIndex + 1); // 왕복 거리 계산
                    // System.out.println("집 " + pickupIndex + "에서 " + pickupAmount + "개의 상자 수거");
                }
                if (p[pickupIndex] == 0) {
                    pickupIndex--; // 현재 집의 수거가 완료되면 다음 집으로 이동
                }
            }

            // 트럭이 가장 먼 거리까지 왕복한 후 이동 거리 추가
            answer += maxDistance * 2;
            // System.out.println("현재 왕복 거리: " + (maxDistance * 2));
            // System.out.println("배달 인덱스: " + deliveryIndex + ", 수거 인덱스: " + pickupIndex);
            // System.out.println("배달 배열 상태: " + Arrays.toString(d));
            // System.out.println("수거 배열 상태: " + Arrays.toString(p));
            // System.out.println("---------------");
        }
        return answer;
    }
}
