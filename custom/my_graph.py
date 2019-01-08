from collections import deque


class DFSearch:
    def _person_is_seller(self, name):
        return name[-1] == 'm'

    def have_seller(self):
        graph = {}
        graph["you"] = ["alice", "bob", "claire"]
        graph["bob"] = ["anuj", "peggy"]
        graph["alice"] = ["peggy"]
        graph["claire"] = ["thom", "jonny"]
        graph["anuj"] = []
        graph["peggy"] = []
        graph["thom"] = []
        graph["jonny"] = []
        print(graph)
        search_queue = deque()
        search_queue += graph['you']
        searched = []
        while search_queue:
            person = search_queue.popleft()
            if person not in searched:
                if self._person_is_seller(person):
                    print(person + ' is a seller')
                    return True
                else:
                    search_queue += graph[person]
                    searched.append(person)

        return False


# class Dijkstra:


if __name__ == '__main__':
    # df_search = DFSearch()
    # print(df_search.have_seller())
    # the graph
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    # the costs table
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    # the parents table
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    processed = []


    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        # Go through each node.
        for node in costs:
            cost = costs[node]
            # If it's the lowest cost so far and hasn't been processed yet...
            if cost < lowest_cost and node not in processed:
                # ... set it as the new lowest-cost node.
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node


    # Find the lowest-cost node that you haven't processed yet.
    node = find_lowest_cost_node(costs)
    print(node)
    # If you've processed all the nodes, this while loop is done.
    while node is not None:
        cost = costs[node]
        # Go through all the neighbors of this node.
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[n] > new_cost:
                # ... update the cost for this node.
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[n] = node
        # Mark the node as processed.
        processed.append(node)
        # Find the next node to process, and loop.
        node = find_lowest_cost_node(costs)
