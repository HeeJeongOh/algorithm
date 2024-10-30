import java.util.*;
/*
- 튜플 순서 존재
- n개의 원소, 중복되는 원소가 없는 튜플 제공
- 튜플 집합을 기반으로 튜플 찾기

0. "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    0.1 },{ 를 기준으로 스플릿
1. 길이 기준으로 정렬
2. 그리고 다음 집합에 속해 있지 않은 애가 다음 순서
*/
class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        String[] slist = s.split("\\},\\{");
        int len = slist.length;
        
        slist[0] = slist[0].replace("{","");
        slist[len-1] = slist[len-1].replace("}","");
        
        Arrays.sort(slist, new Comparator<String>(){
            @Override
            public int compare(String s1, String s2){
                return s1.length() - s2.length();
            }
        });
        // System.out.println(Arrays.toString(slist));

        ArrayList<String> arr = new ArrayList<>();
        for(String str : slist){
            String[] tmp = str.split(",");
            for(String stmp : tmp){
                if(!arr.contains(stmp)){
                    arr.add(stmp);
                    break;
                }
            }
        }            
        // System.out.println(arr);
        answer = arr.stream()
            .mapToInt(Integer::parseInt)
            .toArray();
        
        return answer;
    }
}