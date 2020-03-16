
class Solution{
public:
	int binSearch(vector<int>arr, int l, int r, int target){
		int c = (l+r)/2;
		if(arr[c]==target)
			return c;
		else if(target < arr[c])
			return binSearch(arr,l,c-1,target);
		else
			return binSearch(arr,c+1,r);
		return -1;
	}
}

// binSearch(arr,0,arr.size()-1,<target>);