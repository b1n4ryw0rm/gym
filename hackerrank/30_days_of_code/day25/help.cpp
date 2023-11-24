#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool isPrime(int value){
    if (value <= 1) {
        return false;
    }
    for (int i = 2; i * i <= value; i++) {
        if (value % i == 0) {
            return false;
        }
    }
    return true; 
}

int main() {
    std::ifstream inputFile("input.txt"); // Replace "example.txt" with the path to your file

    if (!inputFile.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        // Process the line as needed
        //std::cout << line << std::endl; // Print the line to the console
        int dat = stoi(line);
        if (isPrime(dat) == true){
            cout << "Prime" << endl;
        } else {
            cout << "Not prime" << endl;
        }
    }

    inputFile.close(); // Close the file when you're done

    return 0;
}

