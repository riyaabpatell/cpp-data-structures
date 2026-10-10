
#include <iostream>
#include <string>
#include <limits>
using namespace std;

struct Node {
    string name;
    double weight;

    Node* namePrev;
    Node* nameNext;
    Node* weightPrev;
    Node* weightNext;

    Node(string n, double w)
        : name(n), weight(w),
          namePrev(nullptr), nameNext(nullptr),
          weightPrev(nullptr), weightNext(nullptr) {}
};

class DualSortedList {
private:
    Node* nameHead = nullptr;
    Node* weightHead = nullptr;

public:
    void insert(const string& name, double weight) {
        Node* node = new Node(name, weight);

        // Insert in alphabetical order
        Node* curr = nameHead;
        Node* prev = nullptr;

        while (curr && curr->name <= name) {
            prev = curr;
            curr = curr->nameNext;
        }

        node->namePrev = prev;
        node->nameNext = curr;

        if (prev)
            prev->nameNext = node;
        else
            nameHead = node;

        if (curr)
            curr->namePrev = node;

        // Insert in ascending weight order
        curr = weightHead;
        prev = nullptr;

        while (curr && curr->weight <= weight) {
            prev = curr;
            curr = curr->weightNext;
        }

        node->weightPrev = prev;
        node->weightNext = curr;

        if (prev)
            prev->weightNext = node;
        else
            weightHead = node;

        if (curr)
            curr->weightPrev = node;
    }

    void printByName() const {
        cout << "Sorted by name:\n";

        Node* curr = nameHead;
        while (curr) {
            cout << curr->name << " - "
                 << curr->weight << '\n';
            curr = curr->nameNext;
        }
    }

    void printByWeight() const {
        cout << "\nSorted by weight:\n";

        Node* curr = weightHead;
        while (curr) {
            cout << curr->name << " - "
                 << curr->weight << '\n';
            curr = curr->weightNext;
        }
    }

    ~DualSortedList() {
        Node* curr = nameHead;

        while (curr) {
            Node* next = curr->nameNext;
            delete curr;
            curr = next;
        }
    }

    // Prevent accidental copying of owning pointers
    DualSortedList() = default;
    DualSortedList(const DualSortedList&) = delete;
    DualSortedList& operator=(const DualSortedList&) = delete;
};

int main() {
    DualSortedList list;

    cout << "Enter 15 names and weights:\n";

    for (int i = 0; i < 15; ++i) {
        string name;
        double weight;

        cout << "Name: ";
        getline(cin, name);

        cout << "Weight: ";
        if (!(cin >> weight)) {
            cerr << "Invalid weight input.\n";
            return 1;
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        list.insert(name, weight);
    }

    cout << '\n';
    list.printByName();
    list.printByWeight();

    return 0;
}
