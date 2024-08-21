import java.util.*;
/*
- 1-n번의 택배상자
- 택배기사님이 알려준 순서대로 택배상자 싣기
- 보조 컨테이너벨트 설치 : LIFO(스택)

1. 영재 : 1, 2, 3, 4, 5
   택배 : 4, 3, 1, 2, 5
   
    4   1  []
    4   2  [1]
    4   3  [2, 1]
o   4   4  [3, 2, 1]
o   3   5  [3 , 2, 1]
    1   5  [2, 1]

[힌트 참고]
https://jaehee-kim24.github.io/posts/codingTest_programmers_%ED%83%9D%EB%B0%B0%EC%83%81%EC%9E%90/#2%EC%B0%A8

*/
class Solution {
    public int solution(int[] order) {
        int idx = 0;

        int len = order.length;
        int main = 1;

        Deque<Integer> sub = new ArrayDeque<>();
        while(idx < len){
            // System.out.println(order[idx] + " " + main  + " " + sub);
            if(order[idx] == main){
                main += 1;
                idx += 1;
            }
            else if(sub.size() > 0 && order[idx] == sub.peekLast()){
                sub.pollLast();
                idx += 1;
            }
            else{
                if(order[idx] >= main){
                    sub.add(main);
                    main += 1;
                }
                else{
                    break;
                }
            }
            
        }

        return idx;
    }
}