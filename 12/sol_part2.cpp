#include <bits/stdc++.h>

using namespace std;

const int dx[4] = {0, 0, -1, 1}, dy[4] = {1, -1, 0, 0};

pair<int, int> findPosition(vector<string> &grid, int n, int m, char position) {
  int resi = -1, resj = -1;
  for (int i = 0; i < n && resi == -1; i++)
    for (int j = 0; j < m && resj == -1; j++)
      if (grid[i][j] == position) resi = i, resj = j;
  return {resi, resj};
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  vector<string> grid;
  string line;
  while (cin >> line) grid.push_back(line);

  int n = (int)grid.size(), m = (int)grid[0].size();
  int ei, ej;
  tie(ei, ej) = findPosition(grid, n, m, 'E');
  grid[ei][ej] = 'z';

  vector<vector<int>> dist(n, vector<int>(m, -1));
  dist[ei][ej] = 0;
  queue<pair<int, int>> q;
  q.push({ei, ej});
  while (!q.empty()) {
    int ci = q.front().first, cj = q.front().second;
    q.pop();
    for (int ind = 0; ind < 4; ind++) {
      int x = ci + dx[ind], y = cj + dy[ind];
      if (x >= 0 && y >= 0 && x < n && y < m && dist[x][y] == -1 &&
          (int)(grid[x][y]) - (int)(grid[ci][cj]) >= -1) {
        q.push({x, y});
        dist[x][y] = dist[ci][cj] + 1;
      }
    }
  }

  int minDist = 1e9;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      if (dist[i][j] != -1 && grid[i][j] == 'a')
        minDist = min(minDist, dist[i][j]);
  cout << minDist << "\n";

  return 0;
}