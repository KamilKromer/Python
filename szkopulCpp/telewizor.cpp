#include<iostream>
#define str string
#define unsinged long long unsigned int64
#include<algorithm>
using namespace std;


int gcd(unsigned long long f, unsigned long long s) {
    unsigned long long temp = s;

    while (f % temp != 0) {
        if
    }
    unsigned long long div = f % s;
    if (div == 0) {
        return s;
    }
    else {
        return gcd(s, div);
    }
}

int main() {
    str input;
    getline(cin, input);
    unsigned long long max_x, max_y, x, y;

    int ind = 0;
    str temp;
    
    for(int i = 0; i < input.size(); i++) {
        if (  input[i] == ' '  or input.size() - i == 1) {
            if (ind == 0) {
                ind++;
                max_x = stoull(temp);
                temp = "";
            }
            else if (ind == 1) {
                ind++;
                max_y = stoull(temp);
                temp = "";
            }
            else if (ind == 2) {
                ind++;
                x = stoull(temp);
                temp = "";
            }
            else if (ind == 3) {
                ind++;
                temp = temp + input[i];
                y = stoull(temp);
                temp = "";
            }
            else {return 1;} // Błąd w indexie
        }
        else {
            temp = temp + input[i];
        }
    }
    
    // Mamy wartości, teraz dzielimy żeby uzyskać finalną proporcję
    cout << "Wartosci " << max_x << " " << max_y << " " << x << " " << y << endl; 
    int divisor = gcd(x, y);
    cout << "Divisor " << divisor << endl;
    cout << "Divisor inbuilt " << __gcd(x, y);
    x /= divisor;
    y /= divisor; // Te wartości nigdy nie będą ułamkowe

    // Obliczamy
    int multiplier = 1;
    int ilosc = 0;

    while (true) {
        if (x * multiplier <= max_x     &&      y * multiplier <= max_y) {
            multiplier++;
            ilosc++;
        }
        else {break;}
    }

    // Koniec

    cout << ilosc;
    main();
    return 0;
}