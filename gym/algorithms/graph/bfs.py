# breadth first search'
# BSF traversal from a given source vertex.
# BSF(int s) traverses vertices reachable from s.

from collections import defaultdict

# this class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)
		
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	# function to print a BFS of graph
	def BFS(self, s):
	
		# Mark all the vertices as not visited
		visited = [False] * ( len(self.graph) )
	
		# crate a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s]=True

		while queue:
			#Dequeue a vertex from
			#queue and print it
			s=queue.pop(0)
			print(s, end=' ')
		
			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not visited, then mark it 
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True




g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.BFS(2)


