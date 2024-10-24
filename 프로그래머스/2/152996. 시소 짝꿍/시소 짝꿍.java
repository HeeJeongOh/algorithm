import java.util.*;
/*
- 2m, 3m, 4m 거리의 좌석 존재
- 시소 균형을 이루는 사이 - 시소짝꿍
    ㄴ 무게*중심으로부터 거리 동일
- 시소쌍의 개수 세기

[시도1] 시간초과 9 / 17
1. 완전 탐색
2. 서로 어느거리에 둘지는 곱이니까 최소공배수 ?
    2.1 무게가 같은 경우 - 2 : 2
    2.2 무게가 다른 경우 - 2 : 3, 2 : 4, 3 : 4
        ㄴ 180 360
[시도2]
ㄴ https://mag1c.tistory.com/295
1. map에 주어진 값을 넣기 위해 비율로서 접근
2. 비율대로 나눈 값이 map에 존재한다면 answer에 개수 더하기
3. map<기본 무게, 그 무게의 개수>
*/
class Solution {
    
    public long solution(int[] weights) {
        long answer = 0;
        int len = weights.length; 
        Arrays.sort(weights);
        // System.out.println(Arrays.toString(weights));
        
        Map<Double, Integer> map = new HashMap<>();
        
        for(int w : weights){
            double a = (w * 1.0);
    		double b = (w * 2.0) / 3.0;
    		double c = (w * 1.0) / 2.0;
    		double d = (w * 3.0) / 4.0;
            
    		if(map.containsKey(a)) answer += map.get(a);
    		if(map.containsKey(b)) answer += map.get(b);
    		if(map.containsKey(c)) answer += map.get(c);
    		if(map.containsKey(d)) answer += map.get(d);
            
            // map에 무게의 value를 weights의 개수로 넣게되면, 
            // 중복체크의 경우를 빼준다던가 할 것 없이 한번에 체크될 수 밖에 없다
    		map.put((w * 1.0), map.getOrDefault((w * 1.0), 0)+1);        
            // System.out.println(map);

        }
        return answer;
    }
}
