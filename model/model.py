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
        #print(self.lista_nodi)

        self.G.add_nodes_from(self.lista_nodi)  # attenzione a capire cosa fa

        #for node in self.G.nodes:
        #    print(node)

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

        nodi_vicini = []

        #assegno al nodo dato in input dall'utente come intero un effettivo oggetto rifugio, che è un nodo

        #assegno al potenziale nodo vicino che sto cercando (cioè edge[1]) un effettivo oggetto rifugio
        #cosi da poi poter effettuare il controllo sfruttando la sintassi corretta del metodo __eq__ di rifugio

        for edge in self.G.edges(node):
            for nodo in self.G.nodes:

                nodo_vicino = self.associa_id_a_nodo(edge[1])

                if nodo.id == nodo_vicino:
                    nodi_vicini.append(nodo)

        return len(nodi_vicini)

    def associa_id_a_nodo(self,id):

        """Creo una funzione che associa al singolo id del rifugio un effettivo
        oggetto rifugio, scelgo di implementare tale funzione in python perchè la
        query sql sulle connessioni (sentieri) è costruita mediante un join sulle due
        relazioni, altrimenti avrei potuto ottenere subito tutti i dati necessari"""


        for nodo_pot in self.G.nodes:
            if nodo_pot.id == id:
                nodo_vicino = nodo_pot
                return nodo_vicino



    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """

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

        """Tecnica 1 - Metodi NetworkX: `dfs_tree()`, `bfs_tree()`"""

        #start è inteso come vertice, cioè un oggetto di tipo rifugio che è un nodo

        """albero = nx.bfs_tree(self.G, start)

        rifugi_raggiungibili = []
        nodi_totali = list(albero.nodes)[1:None:None]   #suggerito da pycharm con sintassi corretta NetworkX

        for node in nodi_totali:
            nodo_raggiunto = self.associa_id_a_nodo(node)
            rifugi_raggiungibili.append(nodo_raggiunto)

        print(rifugi_raggiungibili)
        return rifugi_raggiungibili"""


        """Tecnica 2 - Algoritmo ricorsivo DFS"""

        self.nodi_visitati = []

        self.get_reachable_recursive_DFS(start,self.nodi_visitati)

        #Dopo aver eseguito la funzione ricorsiva mi assicuro che il nodo di partenza non sia
        #visualizzato come raggiungibile a partire da se stesso:

        if start in self.nodi_visitati:
            self.nodi_visitati.remove(start)

        return self.nodi_visitati


    def get_reachable_recursive_DFS(self,start,nodi_visti):

        """Implementazione dell'algoritmo ricorsivo adattato dalle slide per il Depth First Visit
        dunque sceglo un nodo e da questo ne seleziono uno vicino, faccio lo stesso per quest'ultimo e così via fino
        a che non esaurisco i nodi di un particolare ramo e torno indietro a cercarne altri"""

        archi_start = self.G.edges(start)

        for arco in archi_start:
                nodo_collegato = self.associa_id_a_nodo(arco[1])
                if nodo_collegato in nodi_visti:
                    pass
                else:
                    nodi_visti.append(nodo_collegato)
                    self.get_reachable_recursive_DFS(nodo_collegato,nodi_visti)


        self.nodi_visitati = list(nodi_visti)