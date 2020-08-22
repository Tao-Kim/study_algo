import java.util.Scanner;

public class Solution{
    public static int n;
    public static int m;
    public static int[][] maze;

    public static void solveMaze(int x, int y, int weight){
        weight--;
        if(x < 0 || x >= m || y < 0 || y >= n || maze[y][x] == 0 || (maze[y][x] != 1 && maze[y][x] >= weight)) return;
        else {
            maze[y][x] = weight;
            solveMaze(x-1, y, weight);
            solveMaze(x+1, y, weight);
            solveMaze(x, y-1, weight);
            solveMaze(x, y+1, weight);
        }
    }

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        m = scan.nextInt();
        maze = new int[n][m];
        for(int i = 0; i < n; i++){
            String temp = scan.next().trim();
            for(int j = 0; j < m; j++){
                maze[i][j] = temp.charAt(j) - '0';
            }
        }
        solveMaze(0, 0, 0);
        System.out.println(-maze[n-1][m-1]);
    }
}

/*
문제 : p152_미로탈출
시간 : 측정안함

접근 :
파이썬과 동일


다른 사람 풀이 :
========================================================================================
========================================================================================

노트 : 
- 자바에서 큐 다루는법 공부하기

 */