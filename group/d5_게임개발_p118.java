import java.util.Scanner;

public class Solution {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int y = scan.nextInt();
        int x = scan.nextInt();
        int direction = scan.nextInt();
        int[][] gameMap = new int[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                gameMap[i][j] = scan.nextInt();
            }
        }

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, -1, 0, 1};

        int result = 1;
        int countDirection = 0;
        while(true){
            if(countDirection == 4){
                int xAfter = x + dy[direction];
                int yAfter = y - dx[direction];
                if(gameMap[yAfter][xAfter] == 1){
                    break;
                } else {
                    x = xAfter;
                    y = yAfter;
                    countDirection = 0;
                }
            } else {
                gameMap[y][x] = 2;
                int xAfter = x + dx[direction];
                int yAfter = y + dy[direction];

                if(gameMap[yAfter][xAfter] == 0){
                    result++;
                    x = xAfter;
                    y = yAfter;
                    countDirection = 0;
                    if(direction == 0) direction = 3;
                    else direction--;
                } else {
                    countDirection++;
                    if(direction == 0) direction = 3;
                    else direction--;
                }
            }
        }
        System.out.println(result);
    }
}

/*
문제 : p118_게임개발
시간 : 측정안함

접근 :
2차원 배열의 인덱스 변화 규칙을 찾아서 처리함


다른 사람 풀이 :
========================================================================================
전역 변수와 함수를 이용한 풀이

   public static int n, m, x, y, direction;
    // 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    public static int[][] d = new int[50][50];
    // 전체 맵 정보
    public static int[][] arr = new int [50][50];

    // 북, 동, 남, 서 방향 정의
    public static int dx[] = {-1, 0, 1, 0};
    public static int dy[] = {0, 1, 0, -1};

    // 왼쪽으로 회전
    public static void turn_left() {
        direction -= 1;
        if (direction == -1) direction = 3;
    }
========================================================================================

노트 : 

 */