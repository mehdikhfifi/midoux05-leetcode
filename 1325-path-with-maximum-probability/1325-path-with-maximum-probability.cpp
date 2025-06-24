


#include <queue>
#include <vector>
#include <iostream>
#include <utility>
#include <cmath>
#include <unordered_map>
#include <algorithm>
#include <set>
using namespace std;



class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        
        for (auto& prob: succProb){
            prob = -log(prob);
        }

        // first need to build the adjancency 
        vector<vector<pair<float,int>>> adjacency_list(n);

        set<int> visited;

        int i = 0;
        while ( i < edges.size()){

            auto edge = edges[i];
            
            auto first = edge[0];
            auto second = edge[1];
            auto weight = succProb[i];

            adjacency_list[first].push_back({weight, second});
            adjacency_list[second].push_back({weight, first});
            i++;
        }

        unordered_map<int, float> distances;

        // create your priority queue

        priority_queue<pair<float,int>, vector<pair<float,int>>, greater<pair<float,int>>> mypq;

        // enter in all the nodes into the queue

        mypq.push(make_pair(0,start_node));
        distances[start_node] = 0;
            
        // then you run dijkstra

        while (mypq.size() > 0){
            // pop the first element in the queue
            pair<float,int> element = mypq.top();
            auto element_index = element.second;
            auto element_distance = element.first;
            mypq.pop();
           
            if (!visited.contains(element_index)){

            if (element_index == end_node) return exp(-element_distance);


            // relax all the edges

            for (const auto& neighbors: adjacency_list[element_index]){
                auto new_dist =  element_distance + neighbors.first;
                if (distances.find(neighbors.second) == distances.end() or new_dist < distances[neighbors.second]){
                distances[neighbors.second] = new_dist;
                 mypq.push(make_pair(distances[neighbors.second],neighbors.second));}
            
                }
                visited.insert(element_index);
}

        }



        
        

    
        return 0.0;


        
    }
};