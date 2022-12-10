#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  string command;
  int V = 0, horizontalPosition = 1, cycle = 0;
  vector<vector<char>> result(6, vector<char>(40, '.'));

  function<void()> color = [&]() {
    int row = cycle / 40, col = cycle % 40;
    if (col == horizontalPosition - 1 || col == horizontalPosition ||
        col == horizontalPosition + 1)
      result[row][col] = '#';
  };

  while (cin >> command) {
    if (command == "noop") {
      color();
      cycle++;
    } else {
      cin >> V;
      for (int i : {0, 1}) {
        color();
        cycle++;
      }
      horizontalPosition += V;
    }
  }

  for (int i = 0; i < 6; i++) {
    for (int j = 0; j < 40; j++) cout << result[i][j];
    cout << "\n";
  }

  return 0;
}