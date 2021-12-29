class Node():
    def __init__(self, person_id, parent, movie_id):
        self.person_id = person_id
        self.parent = parent
        self.movie_id = movie_id        


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, person_id):
        return any(node.person_id == person_id for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# function for print solution 
def chain_founder(node):
    # init list of tuple(state, action)
    chain = []
    # fill arrays from node 
    while node.parent != None:
        chain.append(tuple((node.movie_id, node.person_id)))
        node = node.parent
    # change chain direction
    for i in range(len(chain) // 2):
        chain[i], chain[len(chain) - 1] = chain[len(chain) - 1], chain[i]
    return chain


