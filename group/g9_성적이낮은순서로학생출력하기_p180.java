import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Student implements Comparable<Student>{
    public String name;
    public int score;

    public Student(String name, int score){
        this.name = name;
        this.score = score;
    }

    @Override
    public int compareTo(Student otherStudent){
        return this.score - otherStudent.score;
    }    
}


public class Solution{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        ArrayList<Student> studentList = new ArrayList<>();

        for(int i = 0; i < n; i++){
            Student student = new Student(scan.next(), scan.nextInt());
            studentList.add(student);
        }

        Collections.sort(studentList);

        for(int i = 0; i < n; i++){
            System.out.print(studentList.get(i).name+" ");
        }
    }
}


/*
문제 : p180_성적이 낮은 순서로 학생 출력하기
시간 : 측정안함


다른 사람 풀이 :
========================================================================================
========================================================================================

노트 :
- comparable, comparator 비교 해보기
 */