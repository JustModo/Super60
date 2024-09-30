#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    float charge = 0;
    string itemName;

    const vector<string> itemList = {"MILK", "CURD", "BREAD", "MAGGIE", "YOGURT", "ICECREAM", "BANANA", "TOMATO", "OREOS", "SHAMPOO"};
    const vector<float> itemPrice = {45.00, 39.00, 1.99, 9.99, 89.99, 22.50, 10.00, 99.00, 75.00, 125.00};

    while (true) {
        cout << "Enter item name (or 'quit' to exit): ";
        getline(cin, itemName);

        if (itemName == "quit") {
            break;
        }

        transform(itemName.begin(), itemName.end(), itemName.begin(), ::toupper);

        auto it = find(itemList.begin(), itemList.end(), itemName);
        if (it != itemList.end()) {
            int index = distance(itemList.begin(), it);
            charge += itemPrice[index];
            cout << "Total Charge is: " << charge << endl;
        } else {
            cout << "Item not found." << endl;
        }

        system("PAUSE");
        system("CLS");
    }

    cout << "Total Charge is: " << charge << endl;
    system("PAUSE");
    return 0;
}