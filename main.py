

def main():
    arg = {
        'str1' : '{(a+b)/[(c-d)*f]}',
        'str' : '((a-c)+([b-(c/a)]*(d/f)))',
        'a' : 12,
        'b' : 27,
        'c' : 47,
        'd' : 39,
        'f' : 2
        }
    return calculate(arg)

def display(a , i):
    print('stack state (',i,'):',end=' ')
    for ch in a:
        print(ch,end=' ')
    print()

def calculate(arg):
    s = arg['str']
    opList = ['+','-','/','*']
    result = {}
    st = []
    i = -1
    for item in arg:
        print(item, ':',arg[item])
    print('=================================')
    for e in s:
        i += 1
        result = report(i,result,st)
        display(st , i)
        if e == ' ' or e == '\t' or e == '\n':
            continue
        elif e == ')' or e == ']' or e == '}':
            st.append(e)
            display(st , i + 0.5)
            st = st[:len(st)-1]
            st = cal(st,opList)
        else:
            if e == '(' or e == '[' or e == '{' or e in opList:
                st.append(e)
            else:
                st.append(arg[e])
    display(st , i+1)
    return result

def report(stateIndex, result, stack):
    result[stateIndex] = {'stack' : stack}
    return result

def cal(st , opList):
    operand2 = st[len(st)-1]
    op = st[len(st)-2]
    operand1 = st[len(st)-3]
    st = st[:len(st)-4]
    
    if op == '+':
        st.append(operand1 + operand2)
        return st
    if op == '-':
        st.append(operand1 - operand2)
        return st
    if op == '*':
        st.append(operand1 * operand2)
        return st
    if op == '/':
        st.append(operand1 / operand2)
        return st
    return st
            
        
