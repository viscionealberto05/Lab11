from model.model import Model

model = Model()
model.get_nodes()
model.build_graph(1980)
numero_vicini = model.get_num_neighbors(16)