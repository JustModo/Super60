#include <iostream>
#include<algorithm>
#include <stdlib.h>
#include <string>
using namespace std;

int main(){
    float charge=0;int i;string itemName;
    const string itemList[10] ={"MILK", "CURD", "BREAD", "MAGGIE", "YOGURT", "ICECREAM", "BANANA", "TOMATO", "OREOS", "SHAMPOO"};
    const float itemPrice[]={45.00, 39.00, 1.99, 9.99, 89.99, 22.50, 10.00, 99.00, 75.00, 125.00};
    while(1){
        cout << "Item: " << endl;
        getline(cin, itemName);
        if(itemName=="\n") break;
        transform(itemName.begin(),itemName.end(),itemName.begin(), ::toupper);
        for(i=0; i<11; i++){
            if(itemList[i]==itemName) break;
        }
        charge += itemPrice[i];
        cout << "Total Charge is: " << endl;
        cout << charge << endl;
        system("PAUSE");
        system("CLS");
    }
    cout <<"Total Charge is: "<< charge << endl;
    system("PAUSE");
    return 0;
}