class Solution {
    public String solution(String s) {
        String answer = "";
        
        StringBuilder sb = new StringBuilder();
        boolean isNextUpper = true;
        
        for(char c : s.toCharArray()){
            if(c == ' '){
                sb.append(c);
                isNextUpper = true;
            }
            else {
                if(isNextUpper){
                    sb.append(Character.toUpperCase(c));
                    isNextUpper = false;
                }
                else{
                    sb.append(Character.toLowerCase(c));
                }
            }
        }
        
        return sb.toString();
    }
}