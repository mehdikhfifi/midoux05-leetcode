

#include <vector>
#include <unordered_map>
#include <unordered_set>





using namespace std;







// we basically want the dfs to make sure the branch of the tree is good, otherwise return false
class Solution {
public:
    bool dfs(vector<vector<int> >& graph, unordered_set<int>& visited,  unordered_map<int, bool>& mymap, bool state, int node ){
        
        bool current_state = state;
        visited.insert(node);

        for (int neighbor : graph[node]){

            if (visited.find(neighbor) == visited.end()){
            // if it hasn't been visited, then set it equal to the opposite and explore further
            mymap[neighbor] = !current_state;
            if (!dfs(graph, visited, mymap, !current_state, neighbor)) {
    return false;
}

            }
            else {
                if (mymap[neighbor] == current_state){
                    return false;
                }
            }

        }
        return true;
    };

    bool isBipartite(vector<vector<int> >& graph) {

        unordered_set<int> visited; 
        unordered_map<int, bool> mymap;

        int N = graph.size();



        for (int i = 0; i < N; i++ ){
            if (visited.find(i) == visited.end()){
                if (!dfs(graph, visited, mymap, false, i)){
                    return false;
                }

            }
        }


        return true;
        
    }
};