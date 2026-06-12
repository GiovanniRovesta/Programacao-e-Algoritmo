// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int main() 
{
    int n, primo = 2, div = 2, veri;
    cout << "Escreva um numero inteiro: ";
    cin >> n;
    if (n < 2){
        
        cout << "Numero não primo";
    }
    else
    {
        while (primo <= n){
            veri = n % primo;
            if (veri == 0 && n != primo){
                div= div + 1;
            }
            else if (veri == 0 && n == primo && div==2){
                cout << "O numero " <<n<< " é primo";
            }
            primo=primo+1;
        }
        if (div>2){
            cout << "O numero nao é primo, o numero de divisores são " <<div;
        }
    }
    return 0;
}
