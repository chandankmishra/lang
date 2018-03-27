#include <iostream>

struct Node
{
    int data;
    Node* left, * right;
};
#if 0
/*You are required to complete below method */
void pathCountsH(Node *root, int count, std::map <int, int> &mymap)
{
    //Your code here
    if (root == nullptr) {
        return;
    }
    
    count += 1;
    if (root->left == nullptr && root->right == nullptr) {
        if (mymap.find(count) == mymap.end()) {
            std::pair<int,int> mpair(count,1);
            mymap.insert(mpair);
        } else {
            mymap[count] = mymap[count] + 1;
        }
    }
    
    pathCountsH(root->left, count, mymap);
    pathCountsH(root->right, count, mymap);
}

void pathCounts(Node *root)
{
    std::map <int, int> mymap;
    pathCountsH(root, 0, mymap);
    for (auto& x: mymap)
        std::cout << x.first << " " << x.second << " $";
}

#endif
