import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int index = 0;
        for(int[] command : commands){
            int[] arraySliced = Arrays.copyOfRange(array, command[0]-1, command[1]);
            Arrays.sort(arraySliced);
            answer[index++] = arraySliced[command[2]-1];
        }
        return answer;
    }
}


/*
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42748?language=java
시간 : 측정안함


다른 사람 풀이 :
========================================================================================
for문 이용 차이

import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }
}
========================================================================================
기타
ArrayList <-> array 한 풀이
직접 array sort 작성한 풀이
========================================================================================

노트 :
- 자바 기본 자료형 다루는 함수명이 기억이 잘 안났음
- util 좀더 공부하면 좋을것 같음
- for문 index 필요할때 기본 for문이 더 편할수도

 */