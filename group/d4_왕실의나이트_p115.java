import java.util.Scanner;

public class Solution {

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        String location = scan.next();
        int x = location.charAt(0) - 96;
        int y = location.charAt(1) - '0';

        int result = 0;
        if(x - 2 >= 1 && y - 1 >= 1) result++;
        if(x - 2 >= 1 && y + 1 <= 8) result++;
        if(x - 1 >= 1 && y - 2 >= 1) result++;
        if(x - 1 >= 1 && y + 2 <= 8) result++;
        if(x + 1 <= 8 && y - 2 >= 1) result++;
        if(x + 1 <= 8 && y + 2 <= 8) result++;
        if(x + 2 <= 8 && y - 1 >= 1) result++;
        if(x + 2 <= 8 && y + 1 <= 8) result++;

        System.out.println(result);

    }
}

/*
문제 : p115_왕실의 나이트
시간 : 측정안함

접근 :
파이썬과 동일


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 : 
- string.charAt() : 문자열의 특정 인데스의 char 구하기
- char - '0' : char to int 
 */