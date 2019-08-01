import queue

class Node :
    def __init__(self,rootObj) :
        self.parent = rootObj
        self.left = None
        self.right = None
        self.distance = 0

def traverse(graph,root) :
    q = queue.Queue()
    q.put(root)

    discovery = []
    
    while q.empty() is False :
        u = q.get()
        for v in graph[u] :
            if v not in discovery :
                discovery.append(v)
                q.put(v)
                print(v)

if __name__ == "__main__":
    graph=[]
    graph.append({1,4})
    graph.append({0,4,2,3})
    graph.append({1,3})
    graph.append({1,4,2})
    graph.append({3,0,1})

    traverse(graph,0)
