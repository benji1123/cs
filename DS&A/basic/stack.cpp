#include <bits/stdc++.h> 
using namespace std;

#define MAX 1000

class Stack {
	int top;

public:
	int a[MAX];
	// functions
	Stack() { top = -1; } // constructor?
	bool push(int x);
	int pop();
	int peek();
	bool isEmpty();
};

bool Stack::push(int x)
{
	if(top >= (MAX - 1)) {
		cout << "Stack Overflow";
		return false;
	}
	else {
		a[++top] = x;
		cout << x << " pushed into stack\n";
	}
}

int Stack::pop(){
	if(top<0){
		cout << "Stack Underflow";
		return false;
	} else {
		int x = a[top--]; // a will equal top; then, top will decrement
		return x; // so we don't delete top, we just overwrite it later if necessary
	}
}

int Stack::peek(){
	if (top<0){
		cout << "Stack is empty";
		return 0;
	}
	else
		return a[top];
}

bool Stack::isEmpty(){
	return (top < 0);
}

// Driver program to test above functions 
int main() 
{ 
    class Stack s; 
    s.push(10); 
    s.push(20); 
    s.push(30); 
    cout << s.pop() << " Popped from stack\n"; 
    return 0; 
} 
