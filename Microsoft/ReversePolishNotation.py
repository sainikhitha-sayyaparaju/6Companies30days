# 150. Evaluate Reverse Polish Notation 
# link: https://leetcode.com/problems/evaluate-reverse-polish-notation/


# Appr 1:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            # print(st)
            if i in {'+', '*', '-', '/'}:
                b = int(st.pop())
                a = int(st.pop())
                if i == '+':
                    st.append(a + b)
                elif i == '-':
                    st.append(a - b)
                elif i == '*':
                    st.append(a * b)
                elif i == '/':
                    st.append(int(a/b))
            else:
                st.append(i)
        return st.pop()

#Appr2:

from operator import add, mul, sub

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        if len(tokens) == 1:
            return int(tokens[0])

        map = {'+':add, '-':sub, '*':mul, '/':lambda a, b: int(a / b)}
        for i in tokens:
            # print(st)
            if i in map:
                b = int(st.pop())
                a = int(st.pop())
                st.append(map[i](a, b))
            else:
                st.append(i)
        return st.pop()
