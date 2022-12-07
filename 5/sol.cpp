#include <bits/stdc++.h>

using namespace std;

struct instruction {
  int amount, from, to;
};

instruction load_instruction(string input) {
  instruction result;

  int index = input.find(' ', 0) + 1;
  int nextIndex = input.find(' ', index);
  result.amount = stoi(input.substr(index, nextIndex - index));

  index = input.find(' ', nextIndex + 1) + 1;
  nextIndex = input.find(' ', index);
  result.from = stoi(input.substr(index, nextIndex - index));

  index = input.find(' ', nextIndex + 1) + 1;
  nextIndex = input.find(' ', index);
  result.to = stoi(input.substr(index, nextIndex - index));

  return result;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int N = 0, H = 0;

  string input;
  getline(cin, input);

  vector<vector<char>> layers;

  while (!isdigit(input[1])) {
    H++;
    vector<char> currentLayer;

    int index = 0;
    while (index < (int)input.size()) {
      currentLayer.push_back(input[index + 1]);
      index += 4;
    }

    if (!N) N = index / 4;
    layers.push_back(currentLayer);
    getline(cin, input);
  }

  reverse(layers.begin(), layers.end());

  vector<stack<char>> stacks(N);
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < N; j++) {
      if (isalpha(layers[i][j])) {
        stacks[j].push(layers[i][j]);
      }
    }
  }

  // read empty line
  getline(cin, input);

  while (getline(cin, input)) {
    instruction i = load_instruction(input);
    stack<int> helperStack;
    for (int iteration = 0; iteration < i.amount; iteration++) {
      helperStack.push(stacks[i.from - 1].top());
      stacks[i.from - 1].pop();
    }
    for (int iteration = 0; iteration < i.amount; iteration++) {
      stacks[i.to - 1].push(helperStack.top());
      helperStack.pop();
    }
  }

  string answer;
  for (int index = 0; index < N; index++) {
    assert(!stacks[index].empty());
    answer += stacks[index].top();
  }
  cout << answer << "\n";

  return 0;
}