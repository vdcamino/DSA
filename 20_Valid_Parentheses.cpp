class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;
        for (int i = 0; i < s.length(); i++){
            if (s[i] == '{' || s[i] == '(' || s[i] == '[')
                myStack.push(s[i]);
            else if (myStack.empty())
                return false;
            else if (s[i] == '}' && myStack.top() != '{')
                return false;
            else if (s[i] == ')' && myStack.top() != '(')
                return false; 
            else if (s[i] == ']' && myStack.top() != '[')
                return false;
            else 
                myStack.pop();
        }
        return myStack.empty();
    }
};