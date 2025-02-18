from Network_Simplex import NetSimplex
from utils import print_structure, draw_graph

def main():
    j=0
    M = NetSimplex(3)

    M.compute_pred_and_thread(M.G)

    draw_graph(M.G, name=str(j), title="Initial Graph")
    j+=1

    M.get_spanning_tree_stucture(M.G)

    draw_graph(M.G, arcs = M.T["arc"], L = M.L, spanning = 1, name=str(j), title="Initial Spanning Tree Structure")
    j+=1

    for node in M.T["node"]:
        M.compute_depth(M.T, node)
        
    M.compute_potentials(M.T)

    M.compute_cost(M.L)

    i = 0
    while(not M.optimal()):

        entering = M.get_entering_arc()
        arc = M.get_arc(M.G, entering["sp"], entering["ep"])
        M.T["arc"].append(arc)
        leaving = M.get_leaving_arc(M.T,entering)

        draw_graph(M.G, L=M.L, arcs=M.T["arc"], entering=entering, leaving=leaving, spanning=1,
                             name=str(j),
                             title="Iteration: " + str(i) + "\nEntering arc (green) and Leaving arc (red)")
        j+=1

        M.T["arc"].remove(leaving)

        M.L.append(leaving)

        M.compute_pred_and_thread(M.T)

        for node in M.T["node"]:
            M.compute_depth(M.T, node)

        M.update_potentials(M.T, entering, leaving)

        draw_graph(M.G, L=M.L, arcs=M.T["arc"], spanning=1,
                             name=str(j),
                             title="Iteration: " + str(i) + "\nUpdated Structure.")
        j+=1

        M.compute_cost(M.L)

        print("*"*100)
        print("ITERATION:", i)

        print("\n")
        print("=" * 100)
        print("ENTERING ARC:", entering)
        print("LEAVING ARC:", leaving)
        print("=" * 100)
        print("\n")

        print_structure(M.T, M.L)
        print("\n")

        print("END OF ITERATION", i)
        print("*" * 100)
        i+=1


    print("\n")
    print("*"*100)
    print("SHORTEST PATH THREE FOUND")
    print("*" * 100)
    print_structure(M.T)
    
    draw_graph(M.T, spanning = 1,
                         name=str(j),
                         title="Shortest Path Tree")

if __name__=="__main__":
    main()