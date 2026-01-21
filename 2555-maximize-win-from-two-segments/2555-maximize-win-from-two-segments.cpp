class Solution {
public:
    int maximizeWin(vector<int>& pos, int k) {

        int n = pos.size(), w1 = 0, res = 0, prev = 0, next = 0;

        for (int i = 0; i < n; i++){
            while(next < n and pos[next]<=pos[i] + k){
                next++;
            }
            while(pos[prev]<pos[i] -k) prev++;
            res = max(res, w1+next-i);
            w1 = max(w1, i-prev+1);   
        }
    return res;
    }
};