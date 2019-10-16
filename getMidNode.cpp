class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next; // moves x2 as fast 
        } return slow; // @ middle when 'fast' reaches END
    }
};