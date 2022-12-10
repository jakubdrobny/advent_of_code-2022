#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  string line;
  vector<int> cnt;
  int cur = 0;
  for (int i = 0; i < 2256; i++) {
    getline(cin, line);
    if (line.empty()) {
      cnt.push_back(cur);
      cur = 0;
    } else {
      cur += stoi(line);
    }
  }

  if (cur > 0) cnt.push_back(cur);
  sort(cnt.rbegin(), cnt.rend());
  cout << cnt[0] + cnt[1] + cnt[2] << "\n";

  return 0;
}