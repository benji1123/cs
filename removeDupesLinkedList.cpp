class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        
        if(!head)
            return head; // if we don't check for NULL, the initialization of below vars will kill me
            
        int curr = head->val;    
        ListNode* p1 = head; 
        ListNode* p2 = head; 
        while(p1){
            while(p2){
                p2=p2->next;
                if(!p2 || p2->val != curr){     // account for NULL-pointer otherwise this if-block won't when p2 == NULL (last node of list)
                    p1->next = p2;
                    break;
                }
            }
            p1 = p1->next;
            curr = p1 ? p1->val : curr;
        }
        return head;
    }
};