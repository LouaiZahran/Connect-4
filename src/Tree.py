class Tree():
    successors=[]
    val=0
    def __init__(self,val):
        self.val=val
    def add_child(self,val):
        successors.apppend(Tree(val))
    def get_successors(self):
        return successors