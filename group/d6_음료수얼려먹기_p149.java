import java.util.Scanner;

public class Solution {
    public static int n;
    public static int m;
    public static int[][] frame;
    
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        m = scan.nextInt();
        
        frame = new int[n][m];
        for(int i = 0; i < n; i++){
            String temp = scan.next().trim();
            for(int j = 0; j < m; j++){
                frame[i][j] = temp.charAt(j) - '0';
            }
        }

        int result = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(frame[i][j] == 0){
                    result++;
                    checkFrame(i, j);
                }
            }
        }
        System.out.println(result);
    }

    public static void checkFrame(int y, int x){
        if(y < 0 || y >= n || x < 0 || x >= m || frame[y][x] != 0){
            return;
        } else {
            frame[y][x] = 2;
            checkFrame(y-1, x);
            checkFrame(y+1, x);
            checkFrame(y, x-1);
            checkFrame(y, x+1);
        }
    }
}

/*
문제 : p149_게임개발
시간 : 측정안함

접근 :
파이썬과 동일


다른 사람 풀이 :
========================================================================================
========================================================================================

노트 : 
- 1110101 과 같이 붙어 있는 input 을 배열로 담는법 : String 으로 받아서 charAt으로 나누기
- 15줄에 nextLine으로 사용하면 에러 발생함 엔터 관련 버퍼문제 같은데 찾아볼 것

 */