#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {

        if (rooms.size() < 2) {
            return true;
        }

        queue<int> mypq;

        set<int> visited;

        mypq.push(0);
        visited.insert(0);

        while (!mypq.empty()) {
            auto element = mypq.front();
            mypq.pop();

            for (auto room : rooms[element]) {

                if (!visited.contains(room)) {

                    mypq.push(room);
                    visited.insert(room);
                }
            }
        }

        return rooms.size() == visited.size();
    }
};