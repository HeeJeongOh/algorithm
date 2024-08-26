import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.*;

/*
- 파일명 정렬
- head(문자) - number(숫자) - tail(입력순)

0. head, number, tail 쪼개기
    0.1 구글링 - Pattern, Matcher
    0.2 "(\\D+)(\\d+)(.*)"
        ㄴ 숫자가 아닌 문자 / 숫자 / 임의의 문자 여러개 
        ㄴ () : 캡쳐그룹
1. head 순서로 먼저 정렬
2. head가 같을 때 숫자 비교
3. head, number 같을 때 입력순서 비교 (?)
*/
class Solution {
    public String[] solution(String[] files) {
        
        int filesLength = files.length;
        String[][] fileSplit = new String[filesLength][3];
        
        for(int i = 0; i < filesLength; i++){      
            Pattern pattern = Pattern.compile("(\\D+)(\\d+)(.*)");
            Matcher matcher = pattern.matcher(files[i]);
        
            if (matcher.matches()) {
                String head = matcher.group(1); // foo
                String number = matcher.group(2); // 010
                String tail = matcher.group(3); // bar020.zip

                fileSplit[i] = new String[]{head, number, tail};
            }
            // System.out.println(Arrays.toString(fileSplit[i]));
        }
        
        // 정렬
        Arrays.sort(fileSplit, new Comparator<String[]>() {
            @Override
            public int compare(String[] file1, String[] file2) {                
                // 파일명 비교 (대소문자 무시)

                int nameComparison = file1[0].toLowerCase().compareTo(file2[0].toLowerCase());
                if (nameComparison != 0) {
                    return nameComparison;
                }

                // 숫자값 비교
                int num1 = Integer.parseInt(file1[1]);
                int num2 = Integer.parseInt(file2[1]);
                
                return Integer.compare(num1, num2);
            }
        });        
        
        String[] answer = new String[filesLength];

        for (int i = 0; i < filesLength; i++) {
            answer[i] = String.join("", fileSplit[i]);
        }


        return answer;
    }
}