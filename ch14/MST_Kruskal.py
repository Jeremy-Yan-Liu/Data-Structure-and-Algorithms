class Partition:
    """Union-find structure for maintaining disjoint sets."""

   #------------------- nested Position class ------------------
   class Position:
       __slots__ = '_container', '_element', '_size', '_parent'

       def __init__(self, container, e):
           """Create a new position that is the leader of its own group."""
           self._container = container          # reference to Partition instance
           self._element = e
           self._size = 1
           self._parent = self                  # convention for a group leader

        def element(self):
            """Return element stored at this position."""
            return self._element

#--------------------- public Partition class ---------------
    def make_group(self, e):
        """Makes a new group containing element e, and returns its Position."""
        return self.Position(self, e)

    def find(self, p):
        """Finds the group coontaining p and return the position of its leader."""
        if p._parent != p:
            p._parent = self.find(p._parent)   # overwrite p._parent after recursion
        return p._parent

    def union(self, p, q):
        """Merges the groups containing elements p and q (if distinct)."""
        a = self.find(p)
        b = self.find(q)
        if a is not b:                          # only merge if different groups
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size

def MST_Kruskal(g):
    """Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.

    The elements of the graph's edges are assumed to be weights.
    """

    tree = []                           # list of edges in spanning tree
    pq = HeapPriorityQueue()            # entries are edges in G, with weights as key
    forest = Parition()                 # keeps track of forest clusters
    position = {}                       # map each node to its Partition entry

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)          # edge's element is assumed to be its weight

    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        wegith, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position(u))
        b = forest.find(position(v))
        if a != b:
            tree.append(edge)
            forest.union(a,b)

    return tree
