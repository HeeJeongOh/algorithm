import java.util.*;
/*
- 괄호의 짝이 맞지 않는 형태
- () 개수 동일     "균형잡힌"
- () 개수와 짝 동일 "올바른"
*/
class Solution {
    private boolean isMatched(String s){
        int cnt = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                cnt += 1;
            }
            else{
                cnt -= 1;
            }
            if(cnt < 0) { return false;}
        }
        if(cnt == 0){ return true; }
        return false;
    }
    
    private boolean isBalanced(String s){
        int cnt = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                cnt += 1;
            }
            else{
                cnt -= 1;
            }
        }
        if(cnt == 0){ return true; }
        return false;
    }
    private int split(String w){
        int size = w.length();
        for(int i = 2; i < size; i++){
            String tmp = w.substring(0, i);
            if(isBalanced(tmp)){
                return i;
            }
        }
        return size;
    }
    
    private String isCorrectString(String w){
        // 1
        if(w.equals("")) { return ""; }
        
        // 2
        int idx = split(w);
        String u = w.substring(0, idx);
        String v = w.substring(idx, w.length());
        System.out.println("u: " + u + "\t v: " + v);

        // 3
        if(isMatched(u)){
            String tmp = isCorrectString(v);
            // 3.1
            return u + tmp;
        }
        // 4
        else{
            StringBuffer sb = new StringBuffer();
            
            sb.append("(");
            sb.append(isCorrectString(v));
            sb.append(")");
                        
            for(int i = 1; i < u.length()-1; i++){
                if(u.charAt(i) == '('){ sb.append(')'); }
                else { sb.append('('); }
            }
            
            return sb.toString();        
        }
    }
    public String solution(String p) {

        if(p.equals("")){ return ""; }
        if(isMatched(p)){ return p; }
        
        String answer = isCorrectString(p);          

        return answer.toString();
    }
}