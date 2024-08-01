class Solution {
    public int solution(int n) {
        int answer = 0;
        String[] strlist = String.valueOf(n).split("");
        for(String str : strlist){
            answer += Integer.parseInt(str);
        }
        return answer;
    }
}