#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <sstream>
#include <iterator>
#include <fstream>
#include <ctime>
#include <cassert>
#include <cstring>
#include <iomanip>
#include <bitset>
#include <list>
#include <functional>
#include <deque>
#include <complex>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <climits>
#include <tuple>
#include <chrono>

using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {

        if (rooms.size() < 2){
            return true;
        }

        queue<int> mypq;

        set<int> visited;

        mypq.push(0);
        visited.insert(0);

        while( !mypq.empty()){
            auto element = mypq.front();
            mypq.pop();
            
            for (auto room: rooms[element]){
                
                if (!visited.contains(room)){
                    
                    mypq.push(room);
                    visited.insert(room);
            }
        }

        }

        return rooms.size() == visited.size();        
        
    }
};