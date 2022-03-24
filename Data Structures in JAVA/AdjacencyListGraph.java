package DataStructure;

import java.util.*;
import java.util.Scanner;
public class AdjacencyListGraph {
    ArrayList<ArrayList<Integer>> graphs;
    //每个ArrayList里再加一个ArrayList代表顶点连向的链表；
    public AdjacencyListGraph(int v){
        /*构建器，针对无向图*/
        graphs = new ArrayList<>(v);//形成多长的顶点列表
        for(int i=0;i<v;i++){
            graphs.add(new ArrayList<>());//每个顶点有个新的ArrayList
        }
    }

    public void addEdge(int start,int end){
        //加一个新的edge
        graphs.get(start).add(end);
        graphs.get(end).add(start);
    }

    public void removeEdge(int start,int end){
        graphs.get(start).remove((Integer)end);
        graphs.get(end).remove((Integer)start);
    }
}
