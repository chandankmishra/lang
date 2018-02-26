/*
Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/*  Tree node
struct Node
{
    int data;
    Node* left, * right;
}; */

/*You are required to complete below method */
void pathCountsH(Node *root, int count, std::map <int, int> &mymap)
{
    //Your code here
    if (root == NULL) {
        return;
    }
    
    count += 1;
    if (root->left == NULL && root->right == NULL) {
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
