/**
 * String : 불변
 * StringBuffer : 가변, builder에 비해 성능 떨어짐, 멀티스레드 환경에서 동기화 지원
 * StringBuilder : 가변, buffer보다 성능 좋음, 멀티스레드 환경에서 동기화 지원안함
 **/

// 문자열 길이
{
    // 문자열.length() : 공백 포함함
    String a = "test string";
    int lengthOfString = a.length(); 
}

// 문자열 치환
{
    // 문자열.replace()
    String a = "test string";
    String b = a.replace('t', '1'); // 1es1 s1ring
    String c = a.replace("te", "11"); // 11st string

    // 문자열.replaceAll() - 정규식 필요
    // 문자열.replaceFirst() - 정규식 필요
}

// 문자열 대소문자
{
    String a = "test string";
    String b = a.toUpperCase(); // TEST STRING
    String c = a.toLowerCase(); // test string
}

// 문자열 자르기
{
    String a = "test string";

    // 문자열.substring(시작인덱스) : 시작 인덱스를 포함하여 끝까지 문자열
    String b = a.substring(3); // t string

    // 문자열.substring(시작인덱스, 끝인덱스) : 시작 인덱스를 포함하여 끝 인덱스 전까지의 문자열
    String c = a.substring(3, 6); // t s

    // length() 활용
    String d = a.substring(a.length()-3);

    // indexOf 활용
    String e = a.substring(a.indexOf("r"));
}

//문자열 나누기
{
    // 문자열.split("기준문자") 
    String a = "test aaa  ggaehhaeii";

    // " "로 나누기 
    String[] arr = a.split(" "); // test, aaa, ggaehhaeii

    // "ae"로 나누기
    String[] arr2 = a.split("ae"); // test aaa gg, hh, ii

    // ""로 나누기
    String[] arr3 = a.split(""); // t, e, s, t,  , a, a, ....

    String[] split(String regex)
    String[] split(String regex, int limit)
}

// 문자열 비교
{
    String a = "test";
    String b = new String("test");

    // == : 주소를 비교함
    a == b // false 

    // .equals() : 값 비교함
    a.equals(b)

    // .equalsIgnoreCase() : 대소문자 무시하고 값 비교함

    
    // .compareTo() : 사전적 우선순위 비교
    int result = "2019".compareTo("2018");
    if(result > 0) // 2019이 2018 보다 사전적으로 크다
    if(result == 0) // 두 문자열이 사전적으로 같다
    if(result < 0) // 2019이 2018 보다 사전적으로 작다

    // .compareToIgnoreCase() : 대소문자 무시하고 사전적으로 비교함
}

// 문자열 합치기
{
    String a = "test";
    String b = "string";

    String c = a + b; // 1.5이후 내부적으로 StringBuilder를 거침
    String d = a.concat(b); // new String으로 생성함 
}

// 기타 문자열 메소드
{
    char charAt(int index) - 인덱스의 한 문자를 반환함
    boolean contains(CharSequence s) - 문자열 포함 여부 반환
    boolean endsWith(String suffix) - 문자열의 접미사인지 여부 반환
    boolean startsWith(String prefix) - 문자열의 접두사인지 여부 반환
    int indexOf(String) - 문자열의 위치(시작 인덱스) 반환
    int indexOf(String, int) - 특정 인덱스 이후의 문자열의 위치 반환
    int indexOf(int) - 문자(아스키코드)의 위치 반환
    int indexOf(int, int) - 특정 인덱스 이후의 문자의 위치 반환
    int lastIndexOf() - indexOf의 4개의 파라미터 와 사용법 같음, 마지막 인덱스 찾음
    boolean isEmpty() - 빈문자열인지 여부 반환
    int length() - 문자열 길이 반환
    boolean matches(String regex) - 정규식 매치 여부 반환
    String trim() - 문자열 앞, 둣의 공백 제거
    char[] toCharArray() - char 배열로 변환

    String.valueOf(primitive variable) - 원시타입 값 문자열로 반환
    
}

// StringBuffer
{
    // 생성
    StringBuffer sb = new StringBuffer();
    StrinfBuffer sb = new StringBuffer("초기 문자열");
    StringBuilder sb = new StringBuilder();
    StringBuilder sb = new StringBuilder("초기 문자열");

    // 추가
    sb.append("문자열");
    sb.append(149); // 숫자도 가능
    sb.insert(인덱스, 값); // 특정 위치에 추가

    // 삭제
    sb.delete(시작인덱스, 끝인덱스+1)
    sb.deleteCharAt(인덱스)
    
    // 치환
    sb.replace(시작인덱스, 끝인덱스+1, 치환문자열)

    // 문자열 반환
    sb.toString()

    // 반전
    sb.reverse()

    // 기타
    sb.setCharAt(인덱스, 문자) - 특정 인덱스에 문자지정
    sb.substring() // string 동일
    sb.length() // string 동일
    sb.indexOf() // string 동일
    sb.charAt() // string 동일

}