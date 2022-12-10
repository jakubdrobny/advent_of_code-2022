#include <bits/stdc++.h>

using namespace std;

struct file {
  string name;
  string type;
  file *parent;
  vector<file *> kids;
  int size;
};

file *createFile(string name, string type, file *parent, vector<file *> kids,
                 int size) {
  file *res = new file;
  res->name = name;
  res->type = type;
  res->parent = parent;
  res->kids = kids;
  res->size = size;
  return res;
}

void dfs(file *v, vector<file *> &folders) {
  for (int i = 0; i < (int)v->kids.size(); i++) {
    dfs(v->kids[i], folders);
    v->size += v->kids[i]->size;
  }
  if (v->type == "folder") folders.push_back(v);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  const int INF = 1e9;

  string line;
  file *cur = createFile("/", "folder", NULL, vector<file *>(0), 0);
  while (getline(cin, line)) {
    if (line[0] == '$') line = line.substr(2);
    int index = line.find(' ');
    if (index == string::npos) continue;
    string command = line.substr(0, index);
    string filename = line.substr(index + 1);
    if (command == "cd") {
      if (filename == "..") {
        if (cur->name != "/") {
          cur = cur->parent;
        }
      } else {
        for (int i = 0; i < (int)cur->kids.size(); i++) {
          if (cur->kids[i]->name == filename) {
            cur = cur->kids[i];
            break;
          }
        }
      }
    } else if (command == "dir") {
      cur->kids.push_back(
          createFile(filename, "folder", cur, vector<file *>(0), 0));
    } else {
      int fileSize = stoi(command);
      cur->kids.push_back(
          createFile(filename, "file", cur, vector<file *>(0), fileSize));
    }
  }

  while (cur->parent) cur = cur->parent;

  vector<file *> folders;
  dfs(cur, folders);

  int totalDiskSpace = 70000000, requiredFreeDiskSpace = 30000000;
  int usedDiskSpace = cur->size;
  int freeDiskSpace = totalDiskSpace - usedDiskSpace;

  int smallestBigEnoughSize = INF;
  for (auto f : folders) {
    if (freeDiskSpace + f->size >= requiredFreeDiskSpace) {
      smallestBigEnoughSize = min(smallestBigEnoughSize, f->size);
    }
  }
  cout << smallestBigEnoughSize << "\n";

  return 0;
}