package DataStructure;

import DataStructure.*;
import java.util.*;
public class GraphTraversal {
    DataStructure.AdjacencyListGraph graph;
    boolean[] visited;//记录哪些点已经访问过了，未访问为false

    public GraphTraversal(DataStructure.AdjacencyListGraph listGraph){
        this.graph=listGraph;
        visited = new boolean[listGraph.graphs.size()];
    }

    public void DFSTraversal(int v){
        if(visited[v]) return;
        visited[v] = true;
        System.out.println(v+" -> ");
        Iterator<Integer> neighbors=this.graph.graphs.get(v).listIterator();
        while(neighbors.hasNext()){
            int nextNode = neighbors.next();
            if(!visited[nextNode]){
                DFSTraversal(nextNode);
            }
        }
    }
    public void DFS(){
        for(int i=0;i<graph.graphs.size();i++){
            if(!visited[i]){
                DFSTraversal(i);
            }
        }
    }

    public void BFSTraversal(int v){
        Deque<Integer> queue=new ArrayDeque<>();
        visited[v]=true;
        queue.offerFirst(v);
        while(queue.size()!=0){
            Integer cur = queue.pollFirst();
            System.out.println(cur+" -> ");
            Iterator<Integer> neighbors = graph.graphs.get(cur).listIterator();
            while(neighbors.hasNext()){
                int nextNode = neighbors.next();
                if(!visited[nextNode]){
                    queue.offerLast(nextNode);
                    visited[nextNode]=true;
                }
            }
        }
    }
    public void BFS(){
        for(int i=0;i<graph.graphs.size();i++){
            if(!visited[i]){
                BFSTraversal(i);
            }
        }
    }
}
