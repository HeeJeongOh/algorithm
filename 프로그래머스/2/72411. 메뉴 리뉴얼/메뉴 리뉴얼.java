import java.util.*;
/*
- 단품 메뉴들을 조합해서 코스요리로 구성하기
- 가장 많이 함께 주문한 단품 메뉴로
- 최소 2명 이상의 손님인 경우, 2가지 이상의 단품 메뉴로

1. 각 주문에 대해 길이가 메뉴 수에 따라 조합을 생성해서 기록하기
    course = 2, 3, 5
    "ABCDE" - 2 : ab ac ad ae bc bd be cd ce de
            - 3 : abc abd abe acd ace ade bcd bce cde
            - 5 : abcde
*/

class Solution {
    List<String> combs;
    private void combination(String[] menus, boolean[] visited, int n, int r, int current){
        if(r == 0){
            StringBuffer sb = new StringBuffer();
            for(int i = 0; i < n; i++){
                if(visited[i] == true){
                    sb.append(menus[i]);
                }
            }
            combs.add(sb.toString());
        }
        
        for(int i = current; i < n; i++) {
            visited[i] = true;
            combination(menus, visited, n, r-1, i+1);
            visited[i] = false;
        }        
    }
    
    public String[] solution(String[] orders, int[] course) {
        
        Map<String, Integer> mapp = new HashMap<>();
    
        for(String order : orders){
            for(int cnt : course){
                int size = order.length();
                String[] menus = order.split("");
                
                Arrays.sort(menus);
                
                if(size < cnt){ continue; }
                combs = new ArrayList<>();
                combination(menus, new boolean[size], size, cnt, 0);
                
                
                for(String comb : combs){
                    mapp.put(comb, mapp.getOrDefault(comb, 0) + 1);
                }
            }
        }
        // System.out.println(mapp);
        
        ArrayList<String> answerList = new ArrayList<>();

        for(int cnt : course){
            ArrayList<String> list = new ArrayList<>();
            int max = 0;
            
            for(Map.Entry<String, Integer> entry : mapp.entrySet()){
                if(entry.getKey().length() == cnt && entry.getValue() > 1){
                    if(entry.getValue() > max){
                        max = entry.getValue();
                        list = new ArrayList<>();
                        list.add(entry.getKey());
                    }
                    else if(entry.getValue() == max){
                        list.add(entry.getKey());
                    }
                }
            }
            // System.out.println(list);
            answerList.addAll(list);
        }
        String[] answer = new String[answerList.size()];
        int i = 0;
        for(String ans : answerList){
            answer[i++] = ans;
        }
        Arrays.sort(answer);
        return answer;
    }
}