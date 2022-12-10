#include <bits/stdc++.h>

using namespace std;

vector<pair<int, char>> load_moves() {
  vector<pair<int, char>> moves;
  char direction;
  int count;
  while (cin >> direction >> count)
    moves.push_back(make_pair(direction, count));
  return moves;
}

void makeMove(int &x, int &y, char direction, int count) {
  if (direction == 'L') y -= count;
  if (direction == 'R') y += count;
  if (direction == 'U') x += count;
  if (direction == 'D') x -= count;
}

void maxCoordinates(vector<pair<int, char>> &moves) {
  int x = 0, y = 0, mnx = 0, mxx = 0, mny = 0, mxy = 0;
  for (auto m : moves) {
    makeMove(x, y, m.first, m.second);
    mnx = min(mnx, x), mxx = max(mxx, x);
    mny = min(mny, y), mxy = max(mxy, y);
  }
  cout << mnx << " " << mny << "," << mxx << " " << mxy << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  vector<pair<int, char>> moves = load_moves();
  // maxCoordinates(moves);

  int xh = 0, yh = 0, xt = 0, yt = 0;
  set<pair<int, int>> visited;
  visited.insert(make_pair(xt, yt));

  for (auto m : moves) {
    char direction = m.first;
    int count = m.second;
    for (int i = 0; i < count; i++) {
      makeMove(xh, yh, direction, 1);
      // cout << xh << " " << yh << " " << xt << " " << yt << "\n";
      int dx = abs(xh - xt), dy = abs(yh - yt);
      if (dx <= 1 && dy <= 1) continue;

      if (dx == 0) {
        if (yt > yh)
          yt--;
        else
          yt++;
      } else if (dy == 0) {
        if (xt > xh)
          xt--;
        else
          xt++;
      } else if (dx == 1 && dy == 2) {
        xt = xh;
        if (yt > yh)
          yt--;
        else
          yt++;
      } else {
        yt = yh;
        if (xt > xh)
          xt--;
        else
          xt++;
      }

      visited.insert(make_pair(xt, yt));
    }
  }

  cout << (int)visited.size() << "\n";

  return 0;
}