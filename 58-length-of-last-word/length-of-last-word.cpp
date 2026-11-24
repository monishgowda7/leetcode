class Solution {
public:
    string strip(const string& s){
            size_t start = s.find_first_not_of(" \t\n\r");
            if(start == string::npos) return "";
            size_t end = s.find_last_not_of(" \t\n\r");
            return s.substr(start , end-start+1);
        }

    int lengthOfLastWord(string s) {
        
        
        

        int count =0;
        s = strip(s);
        for(int i=s.size()-1; i>=0;  i--){
            if(s[i] == ' ')  return count; 
            count++;

        }
        return count;
    }
};