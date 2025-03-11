class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
    def _get_values(self, res): 
        res.append(self.value)
        for child in self.children:
            child._get_values(res)  
        return res
        
    def print_tree(self):
        res = []
        self._get_values(res)  
        print(" -> ".join(res))  
        
    #Bai 2
    def traverse_bfs(self):
        queue = [self]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.value)
            for child in node.children:
                queue.append(child)
        print(" -> ".join(res))

    #Bai 3
    def find_bfs(self, value):
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return node
            for child in node.children:
                queue.append(child)
        return None
    
    #Bai 4
    def height(self):
        if not self.children:
            return 0
        return 1 + max([child.height() for child in self.children])
#Bai 1
tree = Tree("Company")
tree.add_child(Tree("HR"))
tree.add_child(Tree("IT"))
tree.add_child(Tree("Finance")) 
tree.children[0].add_child(Tree("Alice"))
tree.children[0].add_child(Tree("Bob"))
tree.children[1].add_child(Tree("Charlie"))
tree.children[1].add_child(Tree("David"))

tree.print_tree()
tree.traverse_bfs()
search_result = tree.find_bfs("Alice")
print("Found" if search_result else "Not found")
print(tree.height()) 
