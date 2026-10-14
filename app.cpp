// #include <iostream>
// #include <cstring>
// using namespace std;

// int main() {
//     int n;
//     cout << "enter number of contacts: ";
//     cin >> n;

//     char** contacts = new char*[n];
//     for (int i = 0; i <n ; i ++) {
//         char temp[100];

//         cout << "enter name " << i +1 << ": ";
//         cin >>temp;

//         contacts[i] = new char[strlen(temp) + 1];
//         strcpy(contacts[i], temp);

//     }

//     for (int i = 0;i<n-1;i++) {
//         for (int j =0;j<n-i-1;j++) {
//             if (strcmp(contacts[j], contacts[j+1]) > 0) {
//                 char* temp = contacts[j];
//                 contacts[j] = contacts[j+1];
//                 contacts[j+1] = temp;
//             }
//         }
//     }

//     cout << "contacts in alphabetical order: ";
//     for (int i =0;i<n;i++) {
//         delete[] contacts[i];
//     }

//     delete[] contacts;
//     return 0;
// }


































