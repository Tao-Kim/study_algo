import java.util.Scanner;
import java.util.Arrays;

public class Solution{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int m = scan.nextInt();

        int[] coinArray = new int[n];
        for(int i = 0; i < n; i++){
            coinArray[i] = scan.nextInt();
        }

        int[] calArray = new int[m+1];
        Arrays.fill(calArray, 10001);
        calArray[0] = 0;

        for(int i = 0; i < n; i++){
            for(int j = coinArray[i]; j <= m; j++){
                int previousValue = calArray[j-coinArray[i]];
                if(previousValue != 10001 && previousValue + 1 < calArray[j]){
                    calArray[j] = previousValue + 1;
                }
            }
        }
        System.out.print(calArray[m] == 10001 ? -1 : calArray[m]);
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