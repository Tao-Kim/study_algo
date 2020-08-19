import java.util.Scanner;

public class Solution {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int result = 0;

        for(int i = 0 ; i < n ; i++){
            int minOfRow = 10001;
            for(int j = 0 ; j < m ; j++){
                 int num = scanner.nextInt();
                 if(num < minOfRow) minOfRow = num;
            }
            if(minOfRow > result) result = minOfRow;
        }
        System.out.println(result);
    }
}


/*
문제 : p97_숫자 카드 게임
시간 : 측정안함

접근 :
scanner.nextInt()를 사용하기 위해 반복문이 사용되야하는 만큼
별도로 리스트화 하지않고 바로 최소 최대 처리함.


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
 */