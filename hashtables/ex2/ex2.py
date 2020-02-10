#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticketHT = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(ticketHT, ticket.source, ticket.destination)

    departure = hash_table_retrieve(ticketHT, "NONE")
    print(departure)
    route[0] = departure

    for i in range(length - 1):
        print(i)
        print(route[i])
        nxt = i + 1 # already added departure
        route[nxt] = hash_table_retrieve(ticketHT, route[i]) # Retrieve the pair where the element in current route[i] is the key of that pair, and add it's value to the route[nxt]

    print(route)
    return route


tickets = [
  Ticket("PIT", "ORD"),
  Ticket("XNA", "CID"),
  Ticket("SFO", "BHM"),
  Ticket("FLG", "XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX", "SFO"),
  Ticket("CID", "SLC"),
  Ticket("ORD", "NONE"),
  Ticket("SLC", "PIT"),
  Ticket("BHM", "FLG")
]

print(reconstruct_trip(tickets, 10))