#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  vector<string> grid;
  string input;
  while (getline(cin, input)) grid.push_back(input);

  int maxScenicScore = 0;

  int N = (int)grid.size(), M = grid[0].size();

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      int up = 1, down = 1, left = 1, right = 1;
      while (i - up >= 0 && grid[i][j] > grid[i - up][j]) up++;
      while (i + down < N && grid[i][j] > grid[i + down][j]) down++;
      while (j - left >= 0 && grid[i][j] > grid[i][j - left]) left++;
      while (j + right < M && grid[i][j] > grid[i][j + right]) right++;
      if (i - up < 0) up--;
      if (i + down > N - 1) down--;
      if (j - left < 0) left--;
      if (j + right > M - 1) right--;
      maxScenicScore = max(maxScenicScore, up * down * left * right);
    }
  }

  cout << maxScenicScore << "\n";

  return 0;
}