from linkedStackQueue import LinkedQueue

class Tree:
    """Abstract base class representing a tree structure."""

    #------------------------- nested Position class ------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)          # opposite of __eq__

    #---------- abstract methods that concrete subclass must support --------

    def root(self):
        """Return Position representing the tree's root (or None if emepty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""

        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    #---------- concrete methods that implemented in this class -----------

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    #----------------------- Traversal methods -------------------------------------
    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():      # use same order as positions()
            yield p.element()           # but yield each element

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):       # start recursion
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                                         # visit p before its subtrees
        for c in self.children(p):                      # for each child c
            for other in self._subtree_preorder(c):     # do preorder of c's subtree
                yield other                             # yielding each to our caller

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()                          # return entire preorder iteration

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):      # start recursion
                yield p

    def _subtree_postorder(self):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):                      # for each child c
            for other in self._subtree_postorder(c):    # do postorder of c's subtree
                yield other                             # yielding each to our caller
        yield p                                         # visit p after its subtrees


    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()                      # known positions not yet yielded
            fringe.enqueue(self.root())                 # starting with the root
            while not fring.is_empty():
                p = fringe.dequeue()                    # remove from front of the queue
                yield p
                for c in self.children(p):
                    fringe.enqueue()                    # add children to back of queue

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:                    # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                                         # visit p between its subtrees
        if self.right(p) is not None:                   # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #----------------------- Additional abstract methods ---------------------------
    def left(self, p):
       """Return a Position representing p's left child.

       Return None if p does not have a left child.
       """
       raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
       """Return a Position representing p's right child.

       Return None if p does not have a right child.
       """
       raise NotImplementedError('must be implemented by subclass')

    #---------- concrete methods that implemented in this class -----------
    def sibling(self, p):
       """Return a Position representing p's sibling (or None if no sibling)."""
       parent = self.parent(p)
       if parent is None:               # p must be the root
           return None                  # root has no sibling
       else:
           if p == self.left(parent):
               return self.right(parent)        # possibly None
           else:
               return self.left(parent)         # possibly None
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    #---------- override inherited method to make inorder the default ------------

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()                   # make inorder the default

    #---------- Applications - Table of contents, Parenthesize, Disk Space -----------

    def preorder_indent(T, p, d):
        """Print preorder representation of subtree of T rooted at p at depth d."""
        print(2*d*' ' + str(p.element()))       # use depth for indentation
        for c in T.children(p):
            preorder_indent(T, T.root(), d+1)   # child depth is d+1

    def preorder_label(T, p, d, path):
        """Print labeled representation of subttree of T rooted at p at depth d."""
        label = '.'.join(str(j+1) for j in path)    # displayed labels are one-indexed
        print(2*d*' ' + label, p.element())
        path.append(0)                              # path entries are zero-indexed
        for c in T.children(p):
            preorder_label(T, c, d+1, path)         # child depth is d+1
            path[-1] += 1
        path.pop()

    def parenthesize(T, p):
        """Print parenthesized representation of subtree of T rooted at p."""
        print(p.element(), end = '')                # use of end avoid trailing newline
        if not T.is_leaf(p):
            first_time = True
            for c in T.children(p):
                sep = ' (' if first_time else ', '  # determine proper separator
                first_time = False                  # any future passes will not be the first
                parenthesize(T, c)                  # recur on child
            print(')', end = '')                    # include closing parenthesis

    def disk_space(T, p):
        """Return total disk space for subtree of T rooted at p."""
        subtotal = p.element().space()              # space used at position p
        for c in T.children(p):
            subtotal += disk_space(T, c)            # add child's space to subtotal
        return subtotal



