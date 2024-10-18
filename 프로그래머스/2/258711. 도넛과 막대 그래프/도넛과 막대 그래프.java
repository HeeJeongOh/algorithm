import java.util.*;
/*
- 그래프 간선정보에 따라 생성한 정점의번호와 정점을 생성하기 전 도넛,막대, 8자 그래프 수 구하기
- 도넛 : 일방향 순환
- 막대 : 일방향
- 8자 : 양방향 순환

1. 그래프 그룹화
[시도2]
2. 생성된 정점 찾기
    2.1 (힌트) 추가된 정점은 어떤 점으로부터든 화살표를 받지 않는다.
3. 정점을 시작으로 그래프를 탐색하면 되는 거였음
[시도3]
4. 정점과 간선의 개수 활용하기
*/

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
              
        // 1. 그래프 만들기
        int maxNode = 0;
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> fanIn = new HashMap<>();
        
        for(int[] e : edges){
            maxNode = Math.max(maxNode, Math.max(e[0], e[1]));
            
            ArrayList<Integer> tmp =  graph.getOrDefault(e[0], new ArrayList<>());
            tmp.add(e[1]);
            graph.put(e[0], tmp);
            
            fanIn.put(e[1], fanIn.getOrDefault(e[1], 0)+1);
        }
//         System.out.println(graph + " " + maxNode);
//         System.out.println(fanIn);
        
        // 2. 생성된 정점 찾기
        int addedNode = 0;
        for(int i = 1; i <= maxNode; i++){
            if(!fanIn.containsKey(i) && graph.containsKey(i)){
                if(graph.get(i).size() > 1){
                    addedNode = i;
                    break;
                }
            }
        }
        answer[0] = addedNode;
        boolean[] visited = new boolean[maxNode + 1];            
        Deque<Integer> dq = new ArrayDeque<>();
        
        for(int a : graph.get(addedNode)){
            
            int n = 1;
            int e = 0;

            // 2. 그룹화하기 
            visited[a] = true;
            dq.addLast(a);
            
            while(dq.size() > 0){
                
                int b = dq.poll();
                // System.out.println(b);
                
                if(graph.containsKey(b)){
                    e += graph.get(b).size();

                    for(int nxt : graph.get(b)){
                        if(visited[nxt]){ continue; }
                        visited[nxt] = true;
                        dq.addLast(nxt);
                        n++;
                    } 
                }
            }
            
            // 3. 그래프 판별
            if(n == e){             
                // System.out.println("도넛 " + arr);
                answer[1]++;                        
            }
            else if((n - 1) == e){               
                // System.out.println("막대 " + arr);
                answer[2]++;
            }else {        
                // System.out.println("8자 " + arr);
                answer[3]++;   
            }     
        }
        
        return answer;
    }
}