class Solution {
    public int numberOfSteps(int num) {
        boolean isEven;
        int answer = 0;

        while(num > 0) {
            isEven = num % 2 == 0;
            if(isEven) {
                num /= 2;
            } else {
                num--;
            }
            answer++;
        }
        return answer;
    }
}