#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  vector<string> grid;
  string input;
  while (getline(cin, input)) grid.push_back(input);

  int visibleTreeCount = 0;

  int N = (int)grid.size(), M = grid[0].size();
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      bool visible = true;
      for (int ni = i - 1; ni >= 0; ni--) visible &= grid[i][j] > grid[ni][j];
      if (visible) {
        visibleTreeCount++;
        continue;
      }

      visible = true;
      for (int ni = i + 1; ni < N; ni++) visible &= grid[i][j] > grid[ni][j];
      if (visible) {
        visibleTreeCount++;
        continue;
      }

      visible = true;
      for (int nj = j - 1; nj >= 0; nj--) visible &= grid[i][j] > grid[i][nj];
      if (visible) {
        visibleTreeCount++;
        continue;
      }

      visible = true;
      for (int nj = j + 1; nj < M; nj++) visible &= grid[i][j] > grid[i][nj];
      if (visible) {
        visibleTreeCount++;
        continue;
      }
    }
  }

  cout << visibleTreeCount << "\n";

  return 0;
}