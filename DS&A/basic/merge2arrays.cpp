class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
                    
        // two pointers
        int i = (m-1 > 0) ? m - 1 : 0;
        int j = (n-1 > 0) ? n - 1 : 0;
        int end= m + n - 1;
        
        // check for NULL lists
        if(!nums2.empty() && !nums1.empty()){
            while(i>=0 && j>=0){
                if(nums1[i] > nums2[j]){
                    nums1[end] = nums1[i];
                    nums1[i] = std::numeric_limits<int>::min();               // assuming theere are no NEGATIVES
                    i--; 
                } else{
                    nums1[end] = nums2[j];
                    j--;
                }
                end--;
            }
            while(i >= 0 && end >= 0){
                nums1[end] = nums1[i];
                i--;
                end--;
            }
            while(j >= 0 && end >= 0){
                nums1[end] = nums2[j];
                j--;
                end--;
            }
        }
    }
};