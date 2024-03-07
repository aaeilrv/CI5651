#include <bits/stdc++.h>
using namespace std;

int min(int a, int b) { return a < b ? a : b; }

struct Node {
	int val;
	int weight, size;
	Node *left, *right;
	Node(int c) : val(c), weight(rand()), size(1), left(NULL), right(NULL) {}
} *root;

int size(Node *treap) { return treap ? treap->size : 0; }

void split(Node *treap, Node *&left, Node *&right, int val) {
	if (!treap) {
		left = right = NULL;
		return;
	}

	if (size(treap->left) < val) {
		split(treap->right, treap->right, right, val - size(treap->left) - 1);
		left = treap;
	} else {
		split(treap->left, left, treap->left, val);
		right = treap;
	}

	treap->size = 1 + size(treap->left) + size(treap->right);
}

void merge(Node *&treap, Node *left, Node *right) {
	if (left == NULL) {
		treap = right;
		return;
	}
	if (right == NULL) {
		treap = left;
		return;
	}

	if (left->weight < right->weight) {
		merge(left->right, left->right, right);
		treap = left;
	} else {
		merge(right->left, left, right->left);
		treap = right;
	}
	treap->size = 1 + size(treap->left) + size(treap->right);
}

ostream &operator<<(ostream &os, Node *n) {
	if (!n) return os;
	os << n->left;
	os << n->val;
	os << n->right;
	return os;
}

void multiswap(Node *&root_node, int a, int b) {
    Node *node_a, *node_b, *node_c, *node_d, *node_e, *node_f;
    int segment_a = b - a;
    int segment_b = root_node->size - b;

    int minimum = min(segment_a, segment_b);

    if (a + minimum == b) {
        split(root_node, node_a, node_b, b); 
        split(node_a, node_c, node_d, a);
        split(node_b, node_e, node_f, minimum);

        merge(root_node, node_c, node_e);
        merge(node_d, node_d, node_f);
        merge(root_node, root_node, node_d);

    } else if (b + minimum == root_node->size) {
        split(root_node, node_a, node_b, b);
        split(node_a, node_c, node_d, a);
        split(node_d, node_e, node_f, minimum);

        merge(node_c, node_c, node_b);
        merge(node_c, node_c, node_f);
        merge(root_node, node_c, node_e);
    }
}

int main() {
	int N, a, b;

    cout << "Ingrese el tamaño del arreglo: ";
    cin >> N;

    cout << "Ingrese los valores de a y b: ";
    cin >> a >> b;

    for (int i = 0; i < N; i++) {
        merge(root, root, new Node(i));
    }
    
    for (int i = 0; i < N; i++) {
        a = a + 1;
        b = b + 1;
        multiswap(root, a, b);
    }
    cout << root << '\n';
}