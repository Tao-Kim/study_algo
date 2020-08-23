import java.util.Scanner;

public class Solution{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();

        int[] calArray = new int[n+1];
        calArray[1] = 1;
        calArray[2] = 3;

        for(int i = 3; i <= n; i++){
            calArray[i] = calArray[i-2] * 2 + calArray[i-1];
        }
        System.out.println(calArray[n]);
    }
}

/*
문제 : p223_바닥공사
시간 : 측정안함

접근 :
책의 해설 접근법으로 품

다른 사람 풀이 :
========================================================================================
========================================================================================

노트 :
-
 */