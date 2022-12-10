#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  string command;
  int V = 0, currentSignalStrength = 1, cycle = 1, sumOfSignalStrengths = 0;
  while (cin >> command) {
    if (command == "noop") {
      if (cycle % 40 == 20)
        sumOfSignalStrengths += currentSignalStrength * cycle;
      cycle++;
    } else {
      cin >> V;
      if (cycle % 40 == 20 || cycle % 40 == 19) {
        int countingCycle = (cycle % 40 == 19 ? cycle + 1 : cycle);
        sumOfSignalStrengths += currentSignalStrength * countingCycle;
      }
      cycle += 2;
      currentSignalStrength += V;
    }
  }
  cout << sumOfSignalStrengths << "\n";

  return 0;
}