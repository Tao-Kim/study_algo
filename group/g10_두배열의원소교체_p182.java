import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Solution{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int k = scan.nextInt();
        Integer[] listA = new Integer[n];
        Integer[] listB = new Integer[n+k];

        for(int i = 0; i < n; i++) listA[i] = scan.nextInt();
        Arrays.sort(listA, Collections.reverseOrder());

        for(int i = 0; i < n; i++) listB[i] = scan.nextInt();
        
        for(int i = n; i < n+k; i++) listB[i] = listA[i-k];
        Arrays.sort(listB);

        int sum = 0;
        for(int i = 0; i < k-1; i++) sum += listA[i];
        for(int i = n; i < n+k; i++) sum += listB[i];

        System.out.println(sum);
    }
}


/*
문제 : p182
시간 : 측정안함

접근 :
파이썬과 동일

다른 사람 풀이 :
========================================================================================
========================================================================================

노트 :
- 자바에서는 배열 여러개 조작하는 문제 정직하게 푸는게 더 편할 것 같음.
 */