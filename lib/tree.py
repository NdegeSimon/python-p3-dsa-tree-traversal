class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        """
        Recursive depth-first search implementation.
        """
        if self.root is None:
            return None
        return self._dfs_recursive(self.root, target_id)
    
    def _dfs_recursive(self, node, target_id):
        """
        Helper method for recursive DFS.
        """
        # Check current node first (pre-order traversal)
        if node.get('id') == target_id:
            return node
        
        # Recursively search through children
        for child in node.get('children', []):
            result = self._dfs_recursive(child, target_id)
            if result is not None:
                return result
        
        return None