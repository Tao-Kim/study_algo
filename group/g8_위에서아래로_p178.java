import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Solution {

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        
        Integer[] inputArray = new Integer[n];
        for(int i = 0; i < n; i++){
            inputArray[i] = scan.nextInt();
        }

        Arrays.sort(inputArray, Collections.reverseOrder());

        for(int value : inputArray){
            System.out.printf("%d ", value);
        }
    }
}

/*
문제 : p178_위에서 아래로
시간 : 측정안함

접근 :
파이썬과 동일


다른 사람 풀이 :
========================================================================================
========================================================================================

노트 : 
- Arrays.sort(inputArray, Collections.reverseOrder()); 생각 안났음
 */