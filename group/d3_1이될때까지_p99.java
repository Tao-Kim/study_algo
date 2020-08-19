import java.util.Scanner;

public class Solution {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int result = 0;

        while(n != 1){
            int remainder = n % k;
            if(remainder == 0) {
                n /= k;
                result++;
            } else {
                result += remainder;
            }
        }

      System.out.println(result);
    }
}


/*
문제 : p99_1이 될 때까지
시간 : 측정안함

접근 :
파이썬과 동일

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
 */