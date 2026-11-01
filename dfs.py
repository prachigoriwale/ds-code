from collections import deque

locations = ['a','b','c','d']
location_index = {name:idx for idx,name in enumerate(locations)}

adj_matrix = [[0,1,1,0],
              [1,0,0,1],
              [1,0,0,1],
              [0,1,1,0]]

def dfs_matrix(start):
    visited = [False]*len(locations)
    result = []

    def dfs(node):
        visited[node]=True
        result.append(locations[node])

        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor]==1 and not visited[neighbor]:
                dfs(neighbor)

    dfs(location_index[start])
    return result

adj_list = {'a':['b','c'],
            'b':['a','d'],
            'c':['a','d'],
            'd':['b','c']}

def bfs_list(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

def menu():
    while True:
        print("\n===menu===")
        print("1.dfs")
        print("2.bfs")
        print("3.exit")

        choice = int(input("entre the choice:"))

        if choice==1:
            start_location = 'a'
            dfs_result = dfs_matrix(start_location)
            print("DFS(traversal using adjacent matrix:)",dfs_result)

        elif choice==2:
            start_location = 'a'
            bfs_result = bfs_list(start_location)
            print("BFS ( traversal using adjacency list:)",bfs_result)
        elif choice==3:
            print("exiting....")
        else:
            print("invalid choice")

menu()


