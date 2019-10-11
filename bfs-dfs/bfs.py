
graph = {
    "A": ["B","C"],
    "B": ["A","C","D"],
    "C": ["A","B","D","E"],
    "D": ["B","C","E","F"],
    "E": ["C","D"],
    "F": ["D"]
}

def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    while(len(queue)>0):
        vertex = queue.pop(0)
        seen.add(vertex);
        print(vertex) 
        nodes = graph[vertex]
        for w in nodes:
           if w not in seen:
              queue.append(w)
              seen.add(w)
    
BFS(graph,"E")