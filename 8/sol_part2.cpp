#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  vector<string> grid;
  string input;
  while (getline(cin, input)) grid.push_back(input);

  int maxScenicScore = 0;

  int N = (int)grid.size() + 2, M = grid[0].size() + 2;

  grid.insert(grid.begin(), string(M, '9'));
  grid.push_back(string(M, '9'));

  for (int i = 1; i < N - 1; i++) grid[i] = "9" + grid[i] + "9";

  for (int i = 1; i < N - 1; i++) {
    for (int j = 1; j < M - 1; j++) {
      int up = 1, down = 1, left = 1, right = 1;
      while (grid[i][j] > grid[i - up][j]) up++;
      while (grid[i][j] > grid[i + down][j]) down++;
      while (grid[i][j] > grid[i][j - left]) left++;
      while (grid[i][j] > grid[i][j + right]) right++;
      if (i - up == 0) up--;
      if (i + down == N - 1) down--;
      if (j - left == 0) left--;
      if (j + right == M - 1) right--;
      maxScenicScore = max(maxScenicScore, up * down * left * right);
    }
  }

  cout << maxScenicScore << "\n";

  return 0;
}