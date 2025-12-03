import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """

        self.lista_nodi = DAO.getRifugi()
        print(self.lista_nodi)

        self.G.add_nodes_from(self.lista_nodi)  # attenzione a capire cosa fa
        for node in self.G.nodes:
            print(node)


        self.lista_sentieri = DAO.getSentieri(year)
        for sentiero in self.lista_sentieri:
            self.G.add_edge(sentiero.id_rifugio1, sentiero.id_rifugio2)

    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """

        return self.G.nodes


    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO

        nodi_vicini = []

        #assegno al nodo dato in input dall'utente come intero un effettivo oggetto rifugio, che è un nodo
        """for oggetto_nodo in self.G.nodes:
            if oggetto_nodo.id == node:
                node = oggetto_nodo
                break

        for edge in self.G.edges(node):
            #print(edge[1])

            #assegno al potenziale nodo vicino che sto cercando (cioè edge[1]) un effettivo oggetto rifugio
            #cosi da poi poter effettuare il controllo sfruttando la sintassi corretta del metodo __eq__ di rifugio
            for oggetto_nodo in self.G.nodes:
                if oggetto_nodo.id == edge[1]:
                    potenziale_nodo_vicino = oggetto_nodo
                    break


            for nodo in self.G.nodes:
                #print(nodo)
                #print(edge)
                #if nodo.id == edge[1].id:
                if nodo.id == potenziale_nodo_vicino:
                    nodi_vicini.append(potenziale_nodo_vicino)

        for element in nodi_vicini:
            print(element)

        return len(nodi_vicini)"""


        for edge in self.G.edges(node):
            for nodo in self.G.nodes:

                for nodo_pot in self.G.nodes:
                    # print(nodo)
                    # print(edge)
                    # if nodo.id == edge[1].id:
                    if nodo_pot.id == edge[1]:
                        nodo_vicino = nodo_pot
                        break

                if nodo.id == nodo_vicino:
                    nodi_vicini.append(nodo)

        return len(nodi_vicini)


    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO

        num_cc = nx.number_connected_components(self.G)
        return num_cc

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO
