#include <vector>
#include <queue>
using namespace std;

class Node {
  public:
    string name;
    vector<Node*> children;

    Node(string str) {
      name = str;
    }

    vector<string> breadthFirstSearch(vector<string>* array) {
      // Write your code here.
			queue<Node*>q;
			q.push(this);
			while(!q.empty()){
				Node *curr = q.front();
				q.pop();
				array->push_back(curr->name);
				for(Node* child : curr->children)
					q.push(child);
			}
			return *array;
    }

    Node* addChild(string name) {
      Node* child = new Node(name);
      children.push_back(child);
      return this;
    }
};