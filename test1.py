def find_related_events(events, target_event):
    
    graph = {}
    for _, p1, p2 in events:
        if p1 in graph:
            graph[p1].append(p2)
        else:
            graph[p1] = [p2]
        if p2 in graph:
            graph[p2].append(p1)
        else:
            graph[p2] = [p1]


    
    path = []
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                path.append((node, neighbor))
                dfs(neighbor)

    dfs(target_event[0])
    dfs(target_event[1])

    print(path)

    
    output = []
    for event in events:
        if tuple(event[1:]) in path or tuple(reversed(event[1:])) in path:
            output.append(event)

    return output

# events = [
#     [1, 'xxxusyyjs', 'jsjgsjdsyu'],
#     [1, 'PX', 'PY'],
#     [1, 'jacdajcndk', 'P4'],
#     [1, 'P4', 'uuuuusds'],
#     [1, '', 'uuuuusds']
# ]


events = [
    [1, 'P1', 'P2'],
    [1, 'PX', 'PY'],
    [1, 'P3', 'P4'],
    [1, 'P4', 'P5'],
    [1, 'P5', '']
]




target_event = 1 ('P2', 'P3')
print(find_related_events(events, target_event))