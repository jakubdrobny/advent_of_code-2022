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

void printSnake(vector<pair<int, int>> snake) {
  int mnx = 1000, mny = 1000;
  for (auto p : snake) mnx = min(mnx, p.first), mny = min(mny, p.second);
  for (auto &p : snake) p.first -= mnx, p.second -= mny;
  vector<string> grid(15, string(15, '.'));
  for (int i = 9; i; i--)
    grid[snake[i].first][snake[i].second] = (char)(i + '0');
  grid[snake[0].first][snake[0].second] = 'H';
  cout << "grid:\n";
  for (auto l : grid) cout << l << "\n";
  cout << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  vector<pair<int, char>> moves = load_moves();
  maxCoordinates(moves);

  vector<pair<int, int>> snake(10, {0, 0});
  set<pair<int, int>> visited;
  visited.insert({0, 0});

  for (auto m : moves) {
    char direction = m.first;
    int count = m.second;
    for (int i = 0; i < count; i++) {
      makeMove(snake[0].first, snake[0].second, direction, 1);
      for (int j = 1; j < 10; j++) {
        int &xh = snake[j - 1].first, &xt = snake[j].first,
            &yh = snake[j - 1].second, &yt = snake[j].second;
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
      }
      visited.insert(snake.back());
      // printSnake(snake);
    }
  }

  // cout << (int)visited.size() << "\n";

  return 0;
}