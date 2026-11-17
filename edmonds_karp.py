from collections import deque

class EdmondsKarp:
    def __init__(self, vertices, idx_to_name):
        self.V = vertices
        self.idx_to_name = idx_to_name
        self.initial_capacity = [[0] * vertices for _ in range(vertices)]
        self.residual = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, cap):
        self.initial_capacity[u][v] += cap
        self.residual[u][v] += cap

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v in range(self.V):
                if not visited[v] and self.residual[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def max_flow(self, source, sink):
        parent = [-1] * self.V
        total_flow = 0
        step = 1

        print("\n--- Augmenting Paths Found ---")
        while self.bfs(source, sink, parent):
            # Reconstruct path and find bottleneck capacity
            path = []
            path_flow = float("inf")
            s = sink
            while s != source:
                path.append(self.idx_to_name[s])
                path_flow = min(path_flow, self.residual[parent[s]][s])
                s = parent[s]
            path.append(self.idx_to_name[source])
            path.reverse()

            print(f"Step {step}: {' -> '.join(path)} | Flow pushed: {path_flow}")
            total_flow += path_flow
            step += 1

            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                self.residual[u][v] -= path_flow
                self.residual[v][u] += path_flow
                v = parent[v]

        if step == 1:
            print("No augmenting path found.")
        return total_flow

    def print_matrix(self, title, matrix):
        print(f"\n--- {title} ---")
        header = "    " + " ".join(f"{self.idx_to_name[i]:>4}" for i in range(self.V))
        print(header)
        for i in range(self.V):
            row_str = " ".join(f"{matrix[i][j]:>4}" for j in range(self.V))
            print(f"{self.idx_to_name[i]:>3} {row_str}")

    def display_matrices(self):
        # Compute skew-symmetric Flow Matrix: f(u, v) = c(u, v) - cf(u, v)
        flow_matrix = [[0] * self.V for _ in range(self.V)]
        for u in range(self.V):
            for v in range(self.V):
                if self.initial_capacity[u][v] > 0:
                    flow = self.initial_capacity[u][v] - self.residual[u][v]
                    flow_matrix[u][v] = flow
                    flow_matrix[v][u] = -flow  # Skew symmetry

        self.print_matrix("Final Flow Matrix (Skew-Symmetric)", flow_matrix)
        self.print_matrix("Final Residual Capacity Matrix", self.residual)

def main():
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    node_map = {}
    idx_to_name = []

    def get_node_id(name):
        if name not in node_map:
            if len(node_map) >= num_vertices:
                raise ValueError(f"Exceeded declared number of vertices ({num_vertices}).")
            node_map[name] = len(node_map)
            idx_to_name.append(name)
        return node_map[name]

    edges = []
    print("\nEnter each edge as: <from> <to> <capacity>")
    for i in range(num_edges):
        u_name, v_name, cap = input(f"Edge {i + 1}: ").split()
        u = get_node_id(u_name)
        v = get_node_id(v_name)
        edges.append((u, v, int(cap)))

    source_name = input("\nEnter source node: ").strip()
    sink_name = input("Enter sink node: ").strip()
    source = get_node_id(source_name)
    sink = get_node_id(sink_name)

    ek = EdmondsKarp(num_vertices, idx_to_name)
    for u, v, cap in edges:
        ek.add_edge(u, v, cap)

    result = ek.max_flow(source, sink)
    print(f"\nMaximum Flow from {source_name} to {sink_name}: {result}")
    ek.display_matrices()

if __name__ == "__main__":
    main()