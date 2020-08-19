import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Solution {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int k = scanner.nextInt();

        Integer[] numbers = new Integer[n];

        for(int i = 0 ; i < n ; i++){
            numbers[i] = scanner.nextInt();
        }
        Arrays.sort(numbers, Collections.reverseOrder());
        System.out.println(m / (k+1) * (k * numbers[0] + numbers[1]) + m % (k+1) * numbers[0]);
    }
}


/*
문제 : p92_큰 수의 법칙
시간 : 측정안함


다른 사람 풀이 :
========================================================================================
========================================================================================

노트 :
- 자바 입력은 처음써봐서 공부 필요
- Arrays.sort(arr, reverse) : reverse 할때는 primitive로 선언하면 안됨
 */