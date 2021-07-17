class Solution {
public:

    // 7) InOrder Traversal for binary tree
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(root, &res);
        return res;
    }
    
    void helper(TreeNode* root, vector<int>* res) {
        if(root != nullptr){
            // add left 
            if(root->left != nullptr) helper(root->left, res);
            
            // add current
            res->push_back(root->val);
            
            // add right
            if(root->right != nullptr) helper(root->right, res);
        }
    }
};
