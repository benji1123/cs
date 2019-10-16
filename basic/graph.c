
#include <bits/stdc++.h>
using namespace std;


struct Graph {
    int V;
    set<int, greater<int>>* adjList; 
};

// constructor
Graph* createGraph(int V){
    Graph* graph = new Graph;
    graph->V = V;
    graph->adjList = new set<int, greater<int>>[V];
    return graph;
}

// add edge
void addEdge(Graph* graph, int A, int B){
    graph->adjList[A].insert(B);
    graph->adjList[B].insert(A); // edges are bi-directional
}

void printGraph(Graph* graph) 
{ 
    for (int i = 1; i <= graph->V; ++i) { 
        set<int, greater<int> > lst = graph->adjList[i]; 
        cout << endl << "Adjacency list of vertex "
             << i << endl; 
  
        for (auto itr = lst.begin(); itr != lst.end(); itr++) 
            cout << *itr << " "; 
        cout << endl; 
    } 
} 

int main()
{
    struct Graph* g = createGraph(3);
    addEdge(g,1,2);
    addEdge(g,2,3);
    addEdge(g,3,1);
    printGraph(g);
}