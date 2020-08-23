import java.util.Scanner;
import java.util.Arrays;

public class Solution{
    public static int[] storeItems;
    public static boolean binaryContains(int startIndex, int endIndex, int targetValue){
        if(startIndex > endIndex){
            return false;
        }

        int middleIndex = (startIndex + endIndex) / 2;
        int currentValue = storeItems[middleIndex];

        if(currentValue == targetValue){
            return true;
        } else if(currentValue < targetValue){
            return binaryContains(middleIndex + 1, endIndex, targetValue);
        } else {
            return binaryContains(startIndex, middleIndex - 1, targetValue);
        }
    }

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        storeItems = new int[n];
        for(int i = 0; i < n; i++){
            storeItems[i] = scan.nextInt();
        }
        Arrays.sort(storeItems);

        int m = scan.nextInt();
        int[] requestItems = new int[m];
        for(int i = 0; i < m; i++){
            requestItems[i] = scan.nextInt();
        }

        for(int requestItem : requestItems){
            if(binaryContains(0, n, requestItem)){
                System.out.print("yes "); 
            } else {
                System.out.print("no ");
            }
        }
    }
}

/*
문제 : p197_부품찾기
시간 : 측정안함

접근 :
파이썬과 동일

다른 사람 풀이 :
========================================================================================
해설 : 반복문 이진탐색 

    // 이진 탐색 소스코드 구현(반복문)
    public static int binarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = (start + end) / 2;
            // 찾은 경우 중간점 인덱스 반환
            if (arr[mid] == target) return mid;
            // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            else if (arr[mid] > target) end = mid - 1;
            // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else start = mid + 1; 
        }
        return -1;
    }
========================================================================================

노트 :
 */
