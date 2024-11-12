from collections import defaultdict

def find_related_events(events, target_event):
    # Create a graph from the events
    graph = defaultdict(list)
    for _, p1, p2 in events:
        graph[p1].append(p2)
        graph[p2].append(p1)

    # Split the target event into participants
    target_p1, target_p2 = target_event

    # Perform DFS from each participant in the target event
    related_events = set()
    visited = set()

    def dfs(participant):
        if participant in visited:
            return

        visited.add(participant)

        for neighbor in graph[participant]:
            if neighbor not in visited:
                related_events.add(tuple([participant, neighbor]))
                dfs(neighbor)

    dfs(target_p1)
    dfs(target_p2)

    return list(related_events)




# {
#     'P1': ['P2', 'P3'],
#     'P2': ['P1', 'P4'],
#     'P3': ['P1'],
#     'P4': ['P2'],
# }


events = [
    [1, 'P1', 'P2'],
    [1, 'PX', 'PY'],
    [1, 'P3', 'P4'],
    [1, 'P4', 'P5'],
    [1, '', 'P5']
]

target_event = ('P2', 'P3')
print(find_related_events(events, target_event))  # Output: [('P1', 'P2'), ('P3', 'P4'), ('P4', 'P5')]