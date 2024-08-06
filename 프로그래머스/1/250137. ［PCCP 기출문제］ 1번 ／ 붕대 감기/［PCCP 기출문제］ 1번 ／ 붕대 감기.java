/*
붕대감기
- t초 동안 붕대를 감으면서 1초마다 x만큼의 체력 회복
- t초 연속으로 붕대를 감는 데 성공한다면 y만큼의 체력을 추가로 회복
- 최대 체력 존재
- 공격을 당하면 기술이 취소되고, 그 순간에 체력 회복 불가
    - 즉시 붕대 사용 - 연속시간=0
- 공격을 받으면 정해진 피해량만큼 체력 감소, 체력=0 ko
- 캐릭터의 생존여부 판단하기

1. t시간 기준으로 탐색
2. int 연속시간 갱신
3. 

*/
class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int max_t = attacks[attacks.length - 1][0] + 1;
        
        int current = health;
        int winding = 0;
        int aidx = 0;
        
        for(int t = 0; t < max_t; t++){            

            if(t == attacks[aidx][0]){
                winding = 0;
                current -= attacks[aidx][1];
                aidx += 1;
                
                if(current <= 0){
                    return -1;
                }
            }
            else{                
                winding += 1;
                current += bandage[1];

                if(winding == bandage[0]){
                    current += bandage[2];
                    winding = 0;
                }
                
                if(current > health){
                    current = health;
                }
            }            
            // System.out.println("t: " + t + " c: " + current + " w: " + winding);

        }
            
            
        return current;
    }
}