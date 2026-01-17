class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        int sum1 = a + b + c;
        int sum2 = sum1 * (a*a + b*b + c*c);
        int sum3 = sum2 * (a*a*a + b*b*b + c*c*c);
        if (a != b && a != c && b != c){
            answer = sum1;
        }
        if (a == b || b == c || a == c){
            answer = sum2;
        }
        if (a == b && b == c){
            answer = sum3;
        }
        
        return answer;
    }
}