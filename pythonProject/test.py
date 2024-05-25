def check_string_brackets(input_string):
    balance = 0 #счетчик баланса
    for char in input_string:
        if char == '(':
            balance+=1
        elif char == ')':
            balance-=1
            if balance < 0:
                return "no"
    return "yes" if balance == 0 else "no"
print(check_string_brackets("(()())"))
print(check_string_brackets("(()()))"))