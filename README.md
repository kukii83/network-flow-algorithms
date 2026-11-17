# ITS Graph Theory class Group 5 Assignment 11

Group 5 Members:

- Maulana Anugra Putra/5025251159 (kukii83)

- I Gusti Agung Candra Nugraha/5025251169 (candranugraha576)

- Hussein Mohammad Mahsun/5025251170 (TheDelightOFice)

---

## Edmonds-Karp Algorithm (Maximum Flow)

### Overview
The **Edmonds-Karp algorithm** is a specialized implementation of the Ford-Fulkerson method used to compute the maximum flow in a directed flow network. Instead of selecting arbitrary augmenting paths (which can lead to inefficient execution on certain graphs), Edmonds-Karp uses **Breadth-First Search (BFS)** to always find the shortest augmenting path—measured by the fewest number of edges—from the source ($S$) to the sink ($T$).

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

---
## AI Usage:
https://claude.ai/share/1c392f5d-92f5-433c-83a6-0220a498328b
