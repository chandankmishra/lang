#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
vector<int> two_sum1(vector<int> A)
{
	map <int, int> nmap;        // empty map container
	int target = 9;
	int n = A.size();
	for (int i=0; i < n; i++) {
		int toFind = target - A[i];
		auto it = nmap.find(toFind);
		if (it != nmap.end()) {
			return vector<int>{it->second, i};
		}
		nmap[A[i]] = i;
	}
	return {};
}

vector<int> two_sum2(vector<int> A)
{
	// set <int, greater<int>> nmap;        // empty map container
	set <int, greater <int> > nmap;
	int target = 9;
	int n = A.size();
	for (int i=0; i < n; i++) {
		int toFind = target - A[i];
		auto it = nmap.find(toFind);
		if (it != nmap.end()) {
			return vector<int>{toFind, A[i]};
		}
		nmap.insert(A[i]);
	}
	return {};
}

int main()
{
	vector<int> A = {15, 7, 11, 1, 2};
	for (auto i:A)
		cout << i << ' ';
	cout << "\n";

	auto ret = two_sum2(A);
	cout << A[ret[0]] << " "<< A[ret[1]] << endl;

	sort(A.begin(), A.end());
	for (auto i:A)
		cout << i << ' ';
	cout << "\n";

	set<int, greater<int>> nset;
	nset.insert(10);
	nset.insert(210);
	nset.insert(30);
	nset.insert(40);
	nset.insert(50);

	for (auto i:nset) {
		cout << i << " ";
	}
}
