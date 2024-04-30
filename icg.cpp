#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
vector<vector<string>> quadrupleTable;
int precedence(char op) {
if (op == '+' || op == '-')
return 1;
if (op == '*' || op == '/')
return 2;
return 0;
}
string infix_to_postfix(string expression) {
stack<char> op_stack;
string postfix = "";
for (char& c : expression) {
if (isdigit(c)) {
postfix += c;
} else if (c == '(') {
op_stack.push(c);
} else if (c == ')') {
while (!op_stack.empty() &&
op_stack.top() != '(') {
postfix += op_stack.top();
op_stack.pop();
}
op_stack.pop();
} else {
while (!op_stack.empty() &&
precedence(op_stack.top()) >= precedence(c)) {
postfix += op_stack.top();
op_stack.pop();
}
op_stack.push(c);
}
}
while (!op_stack.empty()) {
postfix += op_stack.top();
op_stack.pop();
}
return postfix;
}
string evaluate_postfix(string expression) {
stack<string> operand_stack;
int i = 1;
string t;
for (char& c : expression) {
if (isdigit(c)) {
operand_stack.push(string(1, c));
} else {
string operand2 = operand_stack.top();
operand_stack.pop();
string operand1 = operand_stack.top();
operand_stack.pop();
string temp = "t" + to_string(i);
i++;
t += temp + " = " + operand1 + c +
operand2 + "\n";
quadrupleTable.push_back({operand1,
string(1, c), operand2, temp});
operand_stack.push(temp);
}
}
return t;
}
void generate_intermediate_code(string expression)
{
string postfix = infix_to_postfix(expression);
cout << "Postfix Expression: " << postfix <<
endl;
string intermediate_code =
evaluate_postfix(postfix);
cout << "Intermediate Code:" << endl;
cout << intermediate_code << endl;
}
void print_quadruple_table() {
cout << "Quadruple Table:" << endl;
for (const auto& quadruple : quadrupleTable) {
for (const auto& item : quadruple) {
cout << item << "\t";
}
cout << endl;
}
}
int main() {
string infix_expression;
cin >> infix_expression;
generate_intermediate_code(infix_expression);
print_quadruple_table();
return 0;
}
