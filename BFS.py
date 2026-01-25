# BFS tells you if there is a path from A to B, if there is a patth, finds the shortest one

from collections import deque

# graph is a hash table mapping every node to its neighbors
# in this case we map a person to its friends
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    """
    This function is created solely for the mango seller example in the textbook.
    By this function, if someone's name ends with 'm' they are a mango seller.
    """
    return name[-1] == "m"


def BFS(name):
    # double-ended queue
    # in python, queue.Queue uses mutex locks therefore it is slower
    # for BFS implementation deque is used providing much better performance for the task
    search_queue = deque()
    search_queue += graph["you"]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller.")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


print(BFS("you"))
