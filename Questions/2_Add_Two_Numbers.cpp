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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode result(0); //aux list result that we will return 
        ListNode* currResultPointer = &result; // aux pointer that we will use to loop over the result list
        int carry = 0;  // carry of each sum we will perform
        while(l1 || l2){    // we will continue traversing until we find the end of both linked lists  
            int sum = carry;    // retrieve carry value from last loop
            if (l1){    // check if current l1 node exists
                sum += l1->val; 
                l1 = l1->next;
            }
            if (l2){    // check if current l2 node exists
                sum += l2->val; 
                l2 = l2->next;
            }
            currResultPointer->next = new ListNode(sum%10);
            currResultPointer = currResultPointer->next;
            carry = sum / 10;   // sum < 10 ? carry will be equal to zero : carry will be the sum's dozens value
        }
        
        if (carry > 0){
            currResultPointer->next = new ListNode(carry);
        }
        
        return result.next;
    }
};