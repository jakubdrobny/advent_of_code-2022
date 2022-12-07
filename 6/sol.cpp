#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  const int requireDistinctCount = 14;

  string input;
  cin >> input;
  for (int index = 0; index < (int)input.size() - 4; index++) {
    set<char> markerSet;
    for (int delta = 0; delta < requireDistinctCount; delta++) {
      markerSet.insert(input[index + delta]);
    }
    if ((int)markerSet.size() == requireDistinctCount) {
      cout << index + requireDistinctCount << "\n";
      return 0;
    }
  }

  return 0;
}