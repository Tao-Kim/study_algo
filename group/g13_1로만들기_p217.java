import java.util.Scanner;

public class Solution{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int x = scan.nextInt();
        int[] countArray = new int[x+1];
        countArray[1] = 0;

        for(int i = 2; i <= x; i++){
            countArray[i] = countArray[i-1] + 1;
            
            if (i % 5 == 0){
                countArray[i] = Math.min(countArray[i / 5] + 1, countArray[i]);
            }
            if (i % 3 == 0){
                countArray[i] = Math.min(countArray[i / 3] + 1, countArray[i]);
            } 
            if (i % 2 == 0){
                countArray[i] = Math.min(countArray[i / 2] + 1, countArray[i]);
            } 
        }
        System.out.println(countArray[x]);
    }
}

/*
문제 : p217_1로 만들기
시간 : 측정안함

접근 :
해설과 동일하게 풀이함
특징으로 반복문 내에서 처음에 countArray[i] = countArray[i-1] + 1;로 인해 배열 전체 초기화 없이
풀이가 가능함

다른 사람 풀이 :
========================================================================================
========================================================================================

노트 :
- 자바 클래스 변수로 선언하면 배열 자동 초기화되는 점 염두에 둘 것
 */