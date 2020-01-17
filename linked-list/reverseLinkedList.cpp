class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* next = NULL;
        ListNode* curr = head;
        while(curr != NULL){
            next = curr->next;  // save the Node after Curr
            curr->next = prev;  // reverse pointer from curr->prev to prev->curr
            
            // set pointers to next pair
            prev = curr;
            curr = next;            
        }
        return prev // prev = HEAD after linked-list is reversed
    }
};