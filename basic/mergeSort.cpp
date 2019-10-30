#include <vector>
using namespace std;
vector<int> mergeSort(vector<int> array);
vector<int> merge(vector<int> arr1, vector<int> arr2);

vector<int> mergeSort(vector<int> array) {
	if(array.size()<=1)
		return array;
	int midIndex = array.size()/2;
	vector<int>left(array.begin(), array.begin()+midIndex);
	vector<int>right(array.begin()+midIndex, array.end());
	return merge(mergeSort(left), mergeSort(right));
}

vector<int> merge(vector<int> arr1, vector<int> arr2){
	int p1=0;
	int p2=0;
	int p3=0;
	vector<int>arr3 (arr1.size() + arr2.size(), 0); //make sure this is double the size
	
	while(p1<arr1.size() && p2<arr2.size()){
		if(arr1[p1]<arr2[p2])
			arr3[p3++] = arr1[p1++];
		else
			arr3[p3++] = arr2[p2++];
	}
	while(p1<arr1.size())
		arr3[p3++] = arr1[p1++];
	while(p2<arr2.size())
		arr3[p3++] = arr2[p2++]; 
	return arr3;
}