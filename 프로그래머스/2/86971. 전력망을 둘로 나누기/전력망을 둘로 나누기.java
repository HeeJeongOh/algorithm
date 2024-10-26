import java.util.*;
/*
- 트리구조(그래프)
- 유사한 크기의 네트워크 2개로 분할하기
[호종]
1. 시작 노드 : 유입이 없는 노드
2. bfs, 각 노드 별 자식 노드 수 저장하기
    3(3)
    1(0)   2(0)   4(3)
                  5(0)   6(0)   7(2)
                                8(0) 9(0)
*/
class Solution {
    
     private int countChilds(List<List<Integer>> tree, boolean[] visited, int[] connectedNodes, int current) {

        int cnt = 1;

        for (int next : tree.get(current)) {

            if (!visited[next]) {
                visited[next] = true;
                cnt += countChilds(tree, visited, connectedNodes, next);
            }
        }

        // 해당 노드의 모든 자식 노드 개수 세기
        connectedNodes[current] = cnt;
         
        return cnt;
    }
    
    public int solution(int n, int[][] wires) {
        
        List<List<Integer>> tree = new ArrayList<>(n);
        boolean[] visited = new boolean[n];
        int[] connectedNodes = new int[n];
        

        for (int i = 0; i < n; i++) {
            tree.add(new ArrayList<>());
        }
        for (int[] wire : wires) {
            tree.get(wire[0] - 1).add(wire[1] - 1);
            tree.get(wire[1] - 1).add(wire[0] - 1);
        }
        
        visited[0] = true;
        countChilds(tree, visited, connectedNodes, 0);
        
        int answer = 1000;

       for (int v : connectedNodes) {
            int subVal = n - v;
            int diff = Math.abs(subVal - (n - subVal));
            if (diff < answer) {
                answer = diff;
            }
        }
        return answer;
    }
}