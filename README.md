# ITS Graph Theory class Group 5 Assignment 11

Group 5 Members:

- Maulana Anugra Putra/5025251159 (kukii83)

- I Gusti Agung Candra Nugraha/5025251169 (candranugraha576)

- Hussein Mohammad Mahsun/5025251170 (TheDelightOFice)

---

## Edmonds-Karp Algorithm (Maximum Flow)

### Overview
The **Edmonds-Karp algorithm** is a specialized implementation of the Ford-Fulkerson method used to compute the maximum flow in a directed flow network. Instead of selecting arbitrary augmenting paths (which can lead to inefficient execution on certain graphs), Edmonds-Karp uses **Breadth-First Search (BFS)** to always find the shortest augmenting path measured by the fewest number of edges, from the source ($S$) to the sink ($T$).

### Key Concepts Implemented
* **Residual Network & Reverse Edges:** Tracks remaining edge capacities $c_f(u, v) = c(u, v) - f(u, v)$ and maintains reverse edges to allow flow cancellation/redirection when better paths are discovered.
* **Shortest Augmenting Path (BFS):** Guarantees polynomial time complexity of $O(V \cdot E^2)$, independent of the maximum flow value.
* **Skew Symmetry:** Maintains $f(v, u) = -f(u, v)$ across all connected vertices in the final flow matrix.

### Prerequisites
* compiler with python
* python 3.14

### How to Run
1. Copy/download the `edmonds_karp.py` file
2. Open your compiler
3. Run the code
4. Copy the sample inputs, paste it, and enter

### Results
Sample Input 1:
```bash
6
8
S A 5
S B 2
A B 2
A C 2
B D 4
D C 1
C T 3
D T 5
S
T
```

Sample Output 1:

<img width="337" height="409" alt="image" src="https://github.com/user-attachments/assets/8322d0fc-018d-4b1e-b337-3d90c3531052" />

Sample Input 2:
```bash
4
5
S A 10
S B 10
A B 1
A T 10
B T 10
S
T
```

Sample Output 2:

<img width="311" height="325" alt="image" src="https://github.com/user-attachments/assets/11007a33-4b13-40df-9c4a-6f9194dc9461" />


Sample Input 3:
```bash
6
7
S A 10
S B 10
A C 10
B D 10
C D 10
C T 10
D T 10
S
T
```

Sample Output 3:

<img width="314" height="395" alt="image" src="https://github.com/user-attachments/assets/6a6cbf83-ca5a-4a2c-b0ce-873b0edb29c8" />

---

## Dinic’s Algorithm (Maximum Flow)

### Overview

Dinic’s algorithm computes the maximum flow in a directed flow network. Like Edmonds-Karp, it is a specialization of the Ford-Fulkerson method, but it does not augment one path at a time. It works in phases. Each phase uses a Breadth-First Search (BFS) to build a level graph, which assigns every node its shortest distance from the source (S). It then uses a Depth-First Search (DFS) to push a blocking flow through that level graph, which means saturating every shortest path in it at once. The phases repeat until the sink (T) can no longer be reached.

### Key Concepts Implemented

- Residual Network & Reverse Edges: Tracks remaining capacity cf(u,v) = c(u,v) - f(u,v). Every edge is stored together with a reverse partner, so pushing flow along an edge adds the same amount of residual capacity to its reverse. This lets later phases cancel or redirect flow.
- Level Graph (BFS): Each phase, BFS labels every node with its distance from S. Only edges that go from level k to level k+1 with remaining capacity are used, so the DFS only follows shortest paths.
- Blocking Flow (DFS): The DFS keeps a pointer for each node, so a dead-end edge is never checked twice in a phase. Nodes that cannot reach T are pruned. It is written iteratively, so large graphs will not hit Python’s recursion limit.
- Complexity: O(V²E) in general, and O(E√V) on unit-capacity networks such as bipartite matching. This is independent of the maximum flow value.
- Max-Flow Min-Cut: After the last phase, the nodes still reachable from S in the residual network form the minimum cut. The program prints this cut, and its value equals the max flow.

### Prerequisites
- A compiler or IDE with Python
- Python 3.6 or newer (the code uses f-strings)

### How to Run
1. Copy/download the dinic.py file
2. Open your compiler
3. Run the code
4. Copy the sample input below, paste it, and press Enter

### Input format

```bash
N M            (number of nodes, number of edges)
source sink
u v capacity   (M lines, directed edge u -> v)
```

### Sample input
Sample Input 1:

```bash
6 8
S T
S A 5
S B 2
A C 2
A B 2
B D 4
D C 1
C T 3
D T 5
```

Sample Output 1:
<img width="710" height="480" alt="image" src="https://github.com/user-attachments/assets/dfc75326-59af-466e-837f-2f6e59ddf909" />

Sample Input 2:

```bash
6 9
s t
s v1 16
s v2 13
v1 v3 12
v2 v1 4
v2 v4 14
v3 v2 9
v3 t 20
v4 v3 7
v4 t 4
```

Sample Output 2:
<img width="643" height="503" alt="image" src="https://github.com/user-attachments/assets/3ee3ad59-6652-4e80-8fe4-64036e0d622e" />

Sample Input 3:

```bash
8 11
s t
s w1 1
s w2 1
s w3 1
w1 j1 1
w1 j2 1
w2 j1 1
w3 j2 1
w3 j3 1
j1 t 1
j2 t 1
j3 t 1
```

Sample Output 3:
<img width="944" height="557" alt="image" src="https://github.com/user-attachments/assets/e13fa99d-662e-4d71-b7b2-1c4c34fe75d0" />

---
## AI Usage:
https://claude.ai/share/1c392f5d-92f5-433c-83a6-0220a498328b
https://claude.ai/share/f7a62a32-6bb7-431c-8202-5373c2ac71dd
