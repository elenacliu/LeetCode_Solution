#include <vector>
#include <utility>
#include <functional>

using namespace std;


// https://leetcode-cn.com/problems/maximum-path-quality-of-a-graph/

class Solution {
public:
  int maximalPathQuality(vector<int> &values, vector<vector<int>> &edges,
                         int maxTime) {
    int n = values.size();
    // 因为最多也就10条边
    // 如果我们回到了节点 0，就可以对答案进行更新；如果总时间超过了
    // maxTime，我们需要停止搜索，进行回溯.
    vector<vector<pair<int, int>>> g(n);
    for (auto edge : edges) {
      g[edge[0]].push_back({edge[1], edge[2]});
      g[edge[1]].push_back({edge[0], edge[2]});
    }
    vector<bool> visited(n, false);
    visited[0] = true;
    int ans = 0;

    function<void(int, int, int)> dfs = [&](int u, int time, int value) {
      // 如果又回到 0 了，说明是一条有效的路
      if (u == 0) {
        ans = max(ans, value);
      }
      // 遍历该点所有的邻居
      for (const auto &[v, dist] : g[u]) {
        // 如果访问这个邻居的耗时不会超过 maxTime（就访问）
        if (time + dist <= maxTime) {
          // 如果这个邻居之前没去过
          if (!visited[v]) {
            visited[v] = true;
            // 就可以加上它的价值
            dfs(v, time + dist, value + values[v]);
            // 回溯
            visited[v] = false;
          } else {
            // 否则这个邻居去过，不加上它的价值
            dfs(v, time + dist, value);
          }
        }
      }
    };

    // 最初的 value 是 values[0]
    dfs(0, 0, values[0]);
    return ans;
  }
};