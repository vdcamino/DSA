/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode(-1);  // Temporary head to be deleted at the end
        ListNode* curr = result;
        // Traverse both linked lists comparing them to see if the next value of result list will be from l1 or l2
        while (l1 && l2) {
            if (l1-> val < l2->val) {
                curr->next = l1;
                l1 = l1->next;
            } else {
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;
        }
        if (l1)
            curr->next = l1;
        else 
            curr->next = l2;
        // Delete head node and return result ("new head")
        ListNode* head = result;
        result = head->next;
        head->next = NULL;
        delete head;
        
        return result;
    }
};