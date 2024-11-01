import java.util.*;
/*
- 3가지 연산 (+, -, *)으로 이루어진 수식
- 연산자의 우선순위 재정의하여 절댓값이 가장 큰 숫자 제출하기
- 동일한 순위 불가

1. 숫자와 연산자 분리
2. 연산자 우선순위 조합 구하기
    2.1 get_combinations()
3. 각 조합마다 연산결과를 구하고, 절댓값이 큰 경우 찾기
// 독립적인 복사 
// <-> permutations.add(current) : current 리스트의 원본 객체를 perms에 추가하는 것
//     ㄴ current가 변경되면 permutations도 함께 변경됨.
*/
class Solution {
    private static ArrayList<ArrayList<Integer>> permutations;
    
    private static void permute(List<Character> arr, int start, List<List<Character>> result) {
        if (start == arr.size() - 1) {
            result.add(new ArrayList<>(arr));
            return;
        }
        
        for (int i = start; i < arr.size(); i++) {
            Collections.swap(arr, start, i);
            
            permute(arr, start + 1, result);
            
            Collections.swap(arr, start, i); // swap back
        }
    }
    public static long calculate(String expression, List<Character> precedence) {
        // System.out.println(precedence);
        
        List<String> tokens = new ArrayList<>();
        StringBuilder number = new StringBuilder();

        // 숫자와 연산자를 분리하여 토큰화
        for (char ch : expression.toCharArray()) {
            if (ch == '+' || ch == '-' || ch == '*') {
                tokens.add(number.toString());
                tokens.add(String.valueOf(ch));
                number.setLength(0); // Reset the number
                
            } else {
                number.append(ch);
            }
        }
        tokens.add(number.toString()); // 마지막 숫자 추가
        
        // 각 연산자 우선순위에 대해 계산
        for (char op : precedence){
            // System.out.println(tokens);
        
            List<String> newTokens = new ArrayList<>();
            for (int i = 0; i < tokens.size(); i++) {
                
                String token = tokens.get(i);
                
                if (token.charAt(0) == op) {
                    long left = Long.parseLong(newTokens.remove(newTokens.size() - 1));
                    long right = Long.parseLong(tokens.get(i + 1));
                    long result;

                    // 연산 수행
                    switch (op) {
                        case '+':
                            result = left + right;
                            break;
                        case '-':
                            result = left - right;
                            break;
                        case '*':
                            result = left * right;
                            break;
                        default:
                            throw new IllegalArgumentException("Invalid operator: " + op);
                    }

                    newTokens.add(String.valueOf(result));
                    i++; // 다음 토큰으로 이동
                    
                } else {
                    newTokens.add(token);
                }
            }
            tokens = newTokens; // 새로운 토큰 리스트로 업데이트
        }

        return Math.abs(Long.parseLong(tokens.get(0))); // 절댓값 반환
    }
    
    public long solution(String expression) {
        
        Character[] operators = {'+', '-', '*'};
        List<Character> operatorList = Arrays.asList(operators);
        List<List<Character>> permutations = new ArrayList<>();

        // 모든 연산자 우선순위 조합 생성
        permute(operatorList, 0, permutations);

        long maxValue = 0;

        // 모든 조합에 대해 계산
        for (List<Character> precedence : permutations) {
            long value = calculate(expression, precedence);
            maxValue = Math.max(maxValue, value);
        }

        return maxValue;
    }
}