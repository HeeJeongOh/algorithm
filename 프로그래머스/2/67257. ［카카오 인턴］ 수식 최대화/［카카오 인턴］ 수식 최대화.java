import java.util.*;
/*
[다른사람풀이] 경우의수가 어차피 6가지라는 점 활용
*/
class Solution {

    public long cal(long a, long b, char op){
        if(op == '+')
            return a + b;
        else if(op == '-')
            return a - b;
        else
            return a * b;
    }

    public void calc(ArrayList<Long> numbers, ArrayList<Character> ops, char op){
        for(int i = 0; i < ops.size(); i++){
            
            if(ops.get(i) == op){
                
                long num1 = numbers.get(i);
                long num2 = numbers.get(i + 1);
                
                long result = cal(num1, num2, op);
                numbers.remove(i);
                numbers.remove(i);
                
                numbers.add(i, result);
                ops.remove(i);
                i--;
            }
        }
    }

    public long operation(ArrayList<Long> nums, ArrayList<Character> opers, char op1, char op2, char op3){
        ArrayList<Long> numbers = new ArrayList<>(nums);
        ArrayList<Character> ops = new ArrayList<>(opers);

        calc(numbers, ops, op1);
        calc(numbers, ops, op2);
        calc(numbers, ops, op3);

        return numbers.get(0);
    }

    public long solution(String expression) {
        long answer = 0;
        ArrayList<Long> numbers = new ArrayList<>();    
        ArrayList<Character> operators = new ArrayList<>();

        String num = "";

        for(int i = 0; i < expression.length(); i++){
            if(expression.charAt(i) == '-' || expression.charAt(i) == '+' || expression.charAt(i) == '*'){
                operators.add(expression.charAt(i));
                numbers.add(Long.parseLong(num));
                num = "";
            }

            else{
                num += expression.charAt(i);
            }
        }
        numbers.add(Long.parseLong(num));

        long[] result = new long[6];

        result[0] = operation(numbers, operators, '+', '-', '*');
        result[1] = operation(numbers, operators, '+', '*', '-');
        result[2] = operation(numbers, operators, '-', '+', '*');
        result[3] = operation(numbers, operators, '-', '*', '+');
        result[4] = operation(numbers, operators, '*', '-', '+');
        result[5] = operation(numbers, operators, '*', '+', '-');

        for(int i = 0; i < 6; i++){
            if(answer < Math.abs(result[i]))
                answer = Math.abs(result[i]);
        }

        return answer;
    }
}