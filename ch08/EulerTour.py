class EulerTour:
    """Abstract base class for performing Euler Tour of a tree.
    _hook_previst and _hook_postvisit maybe overridden by subclasses.
    """

    def __init(self, tree):
        """Prepare an Euler toour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])      # start the recursion

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.
        p       Position of current node being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        """

        self._hook_previsit(p, d, path)                      # "pre visit" p
        results = []
        path.append(0)           # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))         # recur on child's subtree
            path[-1] += 1        # increment index
        path.pop()              # remove extraneous index from end of path
        answer = self._hook_postvisit(p, d, path, results)  # "post visit" p
        return answer

    def _hook_previsit(self, p, d, path):                   # can be overridden
        pass

    def _hook_postvisit(self, p, d, path):                  # can be overridden
        pass

# ---------------------------- Application: inherited class -------------------------------------

class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*' ' + str(p.element()))

class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)            # labels are one-indexed
        print(2*d*' ' + label, p.element())

class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:                           # p follows a sibling
            print(', ', end = '')                           # so preface with comma
        print(p.element(), end = '')                        # then print element
        if not self.tree().is_leaf(p):                      # if p has children
            print(' (', end = '')                           # print opening parenthesis
    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):                      # if p has children
            print(')', end = '')                            # print closing parenthesis

class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        # we simply add space associated with p to that of its subtrees
        return p.element().space() + sum(results)

# ---------------------------- inherited class: Binary Euler Tour -------------------------------

class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler Tour of a binary tree.

    This version includes an additional _hook_invist that called after the tour of the left subtree
    (if any), yet before the tour of the right subtree(if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """

    def _tour(self, p, d, path):
        results = [None, None]              # will update with results of recursions
        self._hook_previsit(p, d, path)     # "pre visit" for p
        if self._tree.left(p) is not None:  # consider left child
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invist(p, d, path)           # "in visit" for p

        if self._tree.right(p) is not None:     # consider right child
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)  # "post visit" p
        return answer
    def _hook_invisit(self, p, d, path):
        pass                                # can be overridden

class BinaryLayout(BinaryEulerTour):
    """CLass for computing (x,y) coordinates for each node of a binary tree."""
    def __init__(self, tree):
        super().__init__(tree)              # must call the parent constructor
        self._count = 0                     # initialize count of processed nodes

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)       # x-coordinate serialized by count
        p.element().setY(d)                 # y-coordinate is depth
        self._count += 1                    # advance count of processed nodes


