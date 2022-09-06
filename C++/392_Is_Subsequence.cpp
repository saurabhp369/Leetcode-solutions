#include<string>
using namespace std;
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        int j = 0;
        
        while( i< s.size() and j<t.size())
        {
            if (s[i] == t[j])
            {
                i = i+1;
            }
            j = j+1;
        }
        
        if (i == s.size())
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};