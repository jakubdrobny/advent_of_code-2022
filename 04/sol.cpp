#include <bits/stdc++.h>

using namespace std;

int convertSubstringToString(int startingPosition, int substringLength,
                             string input) {
  return stoi(input.substr(startingPosition, substringLength));
}

pair<int, int> parseInterval(string input, int &startingIndex) {
  pair<int, int> interval;

  int index = input.find("-", startingIndex);
  interval.first =
      convertSubstringToString(startingIndex, index - startingIndex, input);

  index++;
  startingIndex = index;
  index = input.find(",", startingIndex);

  if (index == string::npos) index = (int)input.size();

  interval.second =
      convertSubstringToString(startingIndex, index - startingIndex, input);

  startingIndex = index + 1;

  return interval;
}

bool isInside(int num, pair<int, int> interval) {
  return interval.first <= num && num <= interval.second;
}

bool isContained(pair<int, int> inside, pair<int, int> outside) {
  return isInside(inside.first, outside) && isInside(inside.second, outside);
}

bool overlaps(pair<int, int> inside, pair<int, int> outside) {
  return isInside(inside.first, outside) || isInside(inside.second, outside);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int overlappingIntervals = 0;

  string input;
  while (cin >> input) {
    int index = 0;

    pair<int, int> firstInterval = parseInterval(input, index);
    pair<int, int> secondInterval = parseInterval(input, index);

    // if (isContained(firstInterval, secondInterval) ||
    //     isContained(secondInterval, firstInterval))
    if (overlaps(firstInterval, secondInterval) ||
        overlaps(secondInterval, firstInterval))
      overlappingIntervals++;
  }

  cout << overlappingIntervals << "\n";

  return 0;
}