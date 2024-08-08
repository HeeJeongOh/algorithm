import java.util.*;
/*
- 잘린 조각들의 크기와 올려진 토핑의 개수에 상관없이
- 각 조각에 동일한 가짓수의 토핑이 올라가면 공평한 것
- 롤케이크에 올려진 토핑들의 번호가 주어질 때, 공평하게 자르는 방법의 수를 구하라.

[시도1] 시간초과
1. 완전탐색 : 자를 위치를 옮겨가며 공평한가를 판단하기
2. List와 Set을 모두 활용하여 탐색

[시도2] 구글링
1. 왼쪽은 Set, 오른쪽은 Map으로 접근
2. map.size() == key 갯수
3. second.put(topping[i], second.getOrDefault(topping[i], 0) + 1);
*/
class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int size = topping.length;
        
        HashSet<Integer> first = new HashSet<>();
        HashMap<Integer, Integer> second = new HashMap<>();
        
        first.add(topping[0]);
        for (int i = 1;i < size; i++) {
            second.put(topping[i], second.getOrDefault(topping[i], 0) + 1);
        }
        
        
        for (int i = 1;i < size; i++) {
            
//             System.out.println(first);
//             System.out.println(second);
            
            first.add(topping[i]);
            
            second.put(topping[i], second.get(topping[i]) - 1);
            
            if (second.get(topping[i]) == 0) {
                second.remove(topping[i]);
            }
            
            if (first.size() == second.size()) { answer++; }
        }
        
        
        return answer;
    }
}