/**
 * comparator는 java.util 주로 comparator 자체가 클래스로 구현(혹은 익명 클래스로)되어 정렬할때 선택함
 * comparable은 java.lang 주로 class 자체에 implements되어 하나의 기준으로 정렬하기 위해 사용됨
 * 
**/
import java.util.*;  

class NameComparator implements Comparator<Student>{  
public int compare(Student s1,Student s2){  
return s1.name.compareTo(s2.name);  
}  
}  

class Employee implements Comparable<Employee> {
    private int id;
    private String name;
    private String department;
    private String position;
    private BigInteger sales;
    
    @Override
    public int compareTo(Employee o) {
        return this.name.compareTo(o.name);
    }
}

public class Main{
    public static void main(String args[]){
        List<Employee> list = new ArrayList<>();
        Collections.sort(list);
        Collections.sort(list, Collections.reverseOrder()); 

        Comparator<Employee> salesComparator = new Comparator<Employee>() {
            @Override
            public int compare(Employee o1, Employee o2) {
                return o2.getSales().intValue() - o1.getSales().intValue();
            }
        };

        Collections.sort(list,salesComparator);
        Collections.sort(list,new NameComparator());
    }
}