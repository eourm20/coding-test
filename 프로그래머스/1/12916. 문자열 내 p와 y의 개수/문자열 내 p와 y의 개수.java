class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        for (int i=0; i<s.length(); i++){
            char a = s.charAt(i);
            if (a=='p' || a=='P'){
                p++;
            }
            if (a=='y' || a=='Y'){
                y++;
            }
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");
        return (p==y) ? true:false;
    }
}