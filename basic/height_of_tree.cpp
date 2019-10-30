#include <bits/stdc++.h>
using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
                }
               return root;
           }
        }

    // my code ......................
    int height(Node* root) {
        
        int leftChildHeight = 0;
        int rightChildHeight = 0;

        // compute heights of left & right children
        if(root->left)
            leftChildHeight = height(root->left);
        if(root->right)
            rightChildHeight = height(root->right);
        
        // terminator
        if(root->left == NULL && root->right == NULL)
            return 0;
        
        // height of each node is the larger-height of its children + 1
        int h = (leftChildHeight>rightChildHeight) ? leftChildHeight:rightChildHeight;
        return 1 + h;
    }
}; 