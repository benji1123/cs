
// assuming we get a node-class with value-param & children[] param

int dfs(Node* node){
	// using a stack
	if(node){
		for (Node* child : node->children){		// if we execute "node->children" when node is NULL, we get an error
			dfs(child);
		}
	}
}


int validateBST(Node* node){
	stack<int>s;
	int prev = INT_MIN;
	while(!s.empty() || node){
		while(node){
			s.push(node);
			node=node->left;
		}
		node = s.top();
		s.pop()
		if(node->val < prev)
			return false;
		prev = node->val;
		node = node->right;
	}
	return true;
}