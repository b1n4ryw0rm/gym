#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);



int main()
{
    int N;

    cin >> N;

    regex pattern(".+@gmail\\.com$");

    vector<string> users;

    for(int a0 = 0; a0 < N; a0++){

        string firstName;

        string emailID;

        cin >> firstName >> emailID;


        if(regex_match(emailID,pattern)){

            users.push_back(firstName);

        }

    }

    sort(users.begin(),users.end()); 

    for(int i = 0;i < users.size();i++) { 
        cout << users[i] << endl; 
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

