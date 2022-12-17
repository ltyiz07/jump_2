#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

void vprint(vector<int>& v) {
    for (int val: v) {
        cout << val;
    }
    cout << endl;
}

void vprint(vector<vector<int>>& v) {
    for (vector<int> val: v) {
        vprint(val);
    }
}

void sprint(set<vector<int>>& s) {
    for (vector<int> v: s) {
        vprint(v);
    }   
}

bool sortFunc(vector<int>& v1, vector<int>& v2) {
        return v1[0] > v2[0];
}

int height_from_set(set<vector<int> >& s, int pos) {
     int top, bot;
     int h_top, h_bot;
     vector<int>* popper;
     vector<int> heights;     // even index for bottom, odd index for top
     
     for (vector<int> v: s) {
          if (v[2] == pos) {
               s.erase(v);
               continue;
          } else if (heights.size() == 0) {
               heights.push_back(v[1]);
               heights.push_back(v[3]);
          }
          //TODO: update when popped
          bot = v[1];
          top = v[3];
          for (int i = 0; i < heights.size(); i += 2) {
               h_top = heights[i + 1];
               h_bot = heights[i];
          }
     }
     return 0;
}

long long solution(vector<vector<int> > rectangles)
{
    long long answer = 0;
    int pos = 0;
    set<vector<int>> cs;
    vector<int> vp;

    sort(rectangles.begin(), rectangles.end(), sortFunc);
    while (rectangles.size() > 0 || cs.size() > 0) {
        while (rectangles.back()[0] == pos) {
            vp = rectangles.back();
            rectangles.pop_back();
            cs.insert(vp);
        }
        answer += height_from_set(cs, pos);
        pos++;
    }
    sprint(cs);
    
    return answer;
}

int main(void) {
    //vector<vector<int> > rects = {{0, 1, 4, 4}, {3, 1, 5, 3}};
    vector<vector<int> > rects = {{1, 1, 6, 5}, {2, 0, 4, 2}, {2, 4, 5, 7}, {4, 3, 8, 6}, {7, 5, 9, 7}};

    int ans = solution(rects);
    cout << "answer: " << ans << endl;
}
