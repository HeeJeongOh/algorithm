import java.util.*;
/*
- 모든 폭격미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟 값 구하기
- a나라 : x축에 평행한 직선 형태
- b나라 : 특정 x좌표에서 y축에 수평이 되도록 발사

1.끝나는 시점을 기준으로 정렬하기
2. 카운트하기
*/
class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });
        // System.out.println(Arrays.toString(targets));
        int current = 0;
        for(int[] t : targets){
            if(current > t[0]){ continue; }
            current = t[1];
            answer += 1;
        }
        return answer;
    }
}