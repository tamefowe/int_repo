//
// Created by Trader on 2/20/2021.
//
#include <iostream>
#include <queue>

using namespace std;

struct Node {
    int data;
    Node * left;
    Node * right;
};

Node * make_node(int data) {
    Node * root = new Node;
    root->data = data;
    root->left = root->right = nullptr;
    return root;
}

bool compareTrees(Node *a, Node *b) {
    if (a == nullptr && b == nullptr)
        return true;
    if (a == nullptr) return false;
    if (b == nullptr) return false;

    queue<Node*> q1, q2;
    q1.push(a); q2.push(b);

    while (not q1.empty() && not q2.empty()) {
        Node *x = q1.front();
        Node *y = q2.front();

        if (x->data != y->data) return false;
        q1.pop(); q2.pop();

        if (x->left && y->left) {
            q1.push(x->left);
            q2.push(x->left);
        } else if (x->left || y->left)
            return false;

        if (x->right && y->right) {
            q1.push(x->right);
            q2.push(x->right);
        } else if (x->right || y->right)
            return false;
        return true;
    }
}

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class binary_tree_level_order_traversal {
public:
    int heigth(TreeNode *root) {
        if (root == nullptr)
            return 0;
        return 1 + max(heigth(root->left), heigth(root->right));
    }
    void bsf(TreeNode *root, int depth, vector<vector<int>>& res) {
        if (root == nullptr)
            return;
        res[depth].push_back(root->val);
        bsf(root->left, depth+1, res);
        bsf(root->right, depth+1, res);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        int h = heigth(root);
        vector<vector<int>> res(h);
        bsf(root, 0, res);
        return res;
    }
};

int minDepth(TreeNode* root) {
    if (root == nullptr)
        return 0;

    if(!root->right) return minDepth(root->left) + 1;
    if(!root->left) return minDepth(root->right) + 1;
    return min(minDepth(root->left), minDepth(root->right)) + 1;
}

int main_() {
    Node *x = make_node(1);
    x->left = make_node(2);
    x->right = make_node(3);
    x->left->left = make_node(4);
    x->right->right = make_node(5);

    Node *y = make_node(1);
    y->left = make_node(2);
    y->right = make_node(3);
    y->left->left = make_node(4);
    y->right->right = make_node(5);

    cout << (compareTrees(x, y) ? "YES" : "NO") << endl;

    return 0;
}