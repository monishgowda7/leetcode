class Solution {
public:
    bool isPalindrome(int x) {
        
        int og = x;
        long long reverse =0;

        if (x<0) return false;

        while(og != 0){

            int last = og%10;
            reverse = reverse*10 +last;
            og /=10;
            
        }
        if(x == reverse){
            return true;
        }
        else{
            return false;
        }
    }
};