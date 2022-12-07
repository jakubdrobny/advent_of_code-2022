#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  string line;
  int sum = 0;
  vector<string> lines;
  while (cin >> line) lines.push_back(line);

  for (int i = 0; i < (int)lines.size(); i += 3) {
    map<char, set<int>> oc;
    for (int j = 0; j < 3; j++) {
      int n = (int)lines[i + j].size();
      for (int k = 0; k < n; k++) {
        char c = lines[i + j][k];
        oc[c].insert(j);
      }
    }
    for (int ch = 0; ch < 26; ch++) {
      if ((int)oc[(char)(ch + 'a')].size() == 3) sum += ch + 1;
      if ((int)oc[(char)(ch + 'A')].size() == 3) sum += 27 + ch;
    }
  }
  cout << sum << "\n";

  return 0;
}