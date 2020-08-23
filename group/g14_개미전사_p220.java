import java.util.Scanner;

public class Solution{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] inputArray = new int[n];

        for(int i = 0; i < n; i++){
            inputArray[i] = scan.nextInt();
        }

        int[] calArray = new int[n];
        calArray[0] = inputArray[0];
        calArray[1] = Math.max(inputArray[0], inputArray[1]);

        for(int i = 2; i < n; i++){
            calArray[i] = Math.max(calArray[i-1], calArray[i-2] + inputArray[i]);
        }
        
        System.out.println(calArray[n-1]);
    }
}

/*
문제 : p220_개미전사
시간 : 측정안함

접근 :
파이썬과 동일

다른 사람 풀이 :
========================================================================================
========================================================================================

노트 :
-
 */