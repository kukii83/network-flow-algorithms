"""
Dinic's Algorithm - Maximum Flow (interactive)

Input format for one test case:
    N M            <- number of nodes, number of edges
    S T            <- source name, sink name
    u v c          <- (M lines) directed edge u -> v with capacity c

Node names can be anything without spaces (S, A, 1, city, ...).
Example (the network from the Network Flow slides, max flow = 6):
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
"""

from collections import deque

class Dinic:
    def __init__(self):
        self.names = []          # index -> name
        self.index = {}          # name  -> index
        self.adj = []            # adjacency: list of edge ids per node
        self.to = []             # edge id -> head node
        self.cap = []            # edge id -> residual capacity
        self.orig = []           # edge id -> original capacity (0 for reverse edges)

    def _node(self, name):
        if name not in self.index:
            self.index[name] = len(self.names)
            self.names.append(name)
            self.adj.append([])
        return self.index[name]

    def add_edge(self, u, v, c):
        a, b = self._node(u), self._node(v)
        # forward edge has an even id, its reverse partner is id ^ 1
        self.adj[a].append(len(self.to))
        self.to.append(b)
        self.cap.append(c)
        self.orig.append(c)
        self.adj[b].append(len(self.to))
        self.to.append(a)
        self.cap.append(0)
        self.orig.append(0)

    def _bfs(self, s, t):
        """Build the level graph. Returns True if the sink is reachable."""
        self.level = [-1] * len(self.names)
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                v = self.to[e]
                if self.cap[e] > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def _blocking_flow(self, s, t):
        """Iterative DFS that saturates the level graph (no recursion limit issues)."""
        total = 0
        while True:
            path = []
            u = s
            while u != t:
                advanced = False
                while self.ptr[u] < len(self.adj[u]):
                    e = self.adj[u][self.ptr[u]]
                    v = self.to[e]
                    if self.cap[e] > 0 and self.level[v] == self.level[u] + 1:
                        path.append(e)
                        u = v
                        advanced = True
                        break
                    self.ptr[u] += 1
                if not advanced:
                    if u == s:
                        return total
                    self.level[u] = -1          # dead end, prune it
                    e = path.pop()
                    u = self.to[e ^ 1]
                    self.ptr[u] += 1
            f = min(self.cap[e] for e in path)
            for e in path:
                self.cap[e] -= f
                self.cap[e ^ 1] += f
            total += f

    def max_flow(self, source, sink, verbose=True):
        if source not in self.index or sink not in self.index:
            raise ValueError("Source or sink does not appear in any edge.")
        s, t = self.index[source], self.index[sink]
        if s == t:
            raise ValueError("Source and sink must be different nodes.")

        flow, phase = 0, 0
        while self._bfs(s, t):
            phase += 1
            self.ptr = [0] * len(self.names)
            pushed = self._blocking_flow(s, t)
            flow += pushed
            if verbose:
                levels = ", ".join(
                    f"{self.names[i]}={l}" for i, l in enumerate(self.level) if l >= 0
                )
                print(f"  Phase {phase}: levels [{levels}] -> blocking flow {pushed}")
        self.source, self.sink = s, t
        return flow

    def edge_flows(self):
        """Yield (u, v, flow, capacity) for every original edge."""
        for e in range(0, len(self.to), 2):
            u, v = self.names[self.to[e ^ 1]], self.names[self.to[e]]
            yield u, v, self.orig[e] - self.cap[e], self.orig[e]

    def min_cut(self):
        """Nodes reachable from the source in the residual graph, and the cut edges."""
        seen = {self.source}
        q = deque([self.source])
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                v = self.to[e]
                if self.cap[e] > 0 and v not in seen:
                    seen.add(v)
                    q.append(v)
        cut_edges = []
        for e in range(0, len(self.to), 2):
            u, v = self.to[e ^ 1], self.to[e]
            if u in seen and v not in seen and self.orig[e] > 0:
                cut_edges.append((self.names[u], self.names[v], self.orig[e]))
        return [self.names[i] for i in sorted(seen)], cut_edges


def parse_case(lines):
    """Turn a list of non-empty lines into (Dinic, source, sink)."""
    n, m = map(int, lines[0].split())
    source, sink = lines[1].split()
    if len(lines) - 2 != m:
        raise ValueError(f"Expected {m} edge lines but got {len(lines) - 2}.")
    g = Dinic()
    for line in lines[2:]:
        parts = line.split()
        if len(parts) != 3:
            raise ValueError(f"Bad edge line: '{line}' (expected: u v capacity)")
        u, v, c = parts
        c = int(c)
        if c < 0:
            raise ValueError(f"Negative capacity in line: '{line}'")
        g.add_edge(u, v, c)
    if len(g.names) != n:
        print(f"  (note: you said {n} nodes, but {len(g.names)} distinct names were used)")
    return g, source, sink


def solve(lines):
    g, source, sink = parse_case(lines)
    print("\nRunning Dinic's algorithm...")
    flow = g.max_flow(source, sink)
    print(f"\nMaximum flow {source} -> {sink} = {flow}\n")
    print("Flow on each edge (flow/capacity):")
    for u, v, f, c in g.edge_flows():
        print(f"  {u} -> {v}: {f}/{c}")
    side, cut = g.min_cut()
    print(f"\nMin cut: P = {{{', '.join(side)}}}")
    print("Cut edges: " + ", ".join(f"{u}->{v} ({c})" for u, v, c in cut))
    print(f"Cut value = {sum(c for _, _, c in cut)}  (equals max flow, per Max-Flow Min-Cut)")


def main():
    print("Enter: N M, then source and sink, then M lines of 'u v capacity'")
    try:
        n, m = input("N M: ").split()
        lines = [f"{n} {m}", input("source sink: ")]
        for i in range(int(m)):
            lines.append(input(f"edge {i + 1}/{m} (u v capacity): "))
        solve([ln.strip() for ln in lines if ln.strip()])
    except (ValueError, IndexError) as err:
        print(f"Input error: {err}")


if __name__ == "__main__":
    main()