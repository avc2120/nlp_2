import matplotlib.pyplot as plt
from providedcode.dataset import *
import networkx as nx
import random

if __name__ == '__main__':
    	swedish = plt.figure(1)
	corpus_swedish = get_swedish_train_corpus()
	dependency_graph_swedish = random.choice(corpus_swedish.parsed_sents())
   	nx_graph_swedish, labels_swedish = dependency_graph_swedish.nx_graph()
 	pos_swedish = nx.spring_layout(nx_graph_swedish)
    	nx.draw_networkx_nodes(nx_graph_swedish, pos_swedish, node_size=1000)
    	nx.draw_networkx_labels(nx_graph_swedish, pos_swedish, labels_swedish)
    	nx.draw_networkx_edges(nx_graph_swedish, pos_swedish, edge_color='k', width=1)
    	swedish.show()
	
	english = plt.figure(2)
	corpus_english = get_english_dev_corpus()
	dependency_graph_english = random.choice(corpus_english.parsed_sents())
   	nx_graph_english, labels_english = dependency_graph_english.nx_graph()
   	pos_english = nx.spring_layout(nx_graph_english)
    	nx.draw_networkx_nodes(nx_graph_english, pos_english, node_size=1000)
    	nx.draw_networkx_labels(nx_graph_english, pos_english, labels_english)
    	nx.draw_networkx_edges(nx_graph_english, pos_english, edge_color='k', width=1)
    	english.show()

	danish = plt.figure(3)
	corpus_danish = get_danish_train_corpus()
	dependency_graph_danish = random.choice(corpus_danish.parsed_sents())
   	nx_graph_danish, labels_danish = dependency_graph_danish.nx_graph()
	pos_danish = nx.spring_layout(nx_graph_danish)
    	nx.draw_networkx_nodes(nx_graph_danish, pos_danish, node_size=1000)
    	nx.draw_networkx_labels(nx_graph_danish, pos_danish, labels_danish)
    	nx.draw_networkx_edges(nx_graph_danish, pos_danish, edge_color='k', width=1)
    	danish.show()

	korean = plt.figure(4)
	corpus_korean = get_korean_train_corpus()
    	dependency_graph_korean = random.choice(corpus_korean.parsed_sents())
   	nx_graph_korean, labels_korean = dependency_graph_korean.nx_graph()
	pos_korean = nx.spring_layout(nx_graph_korean)
   	nx.draw_networkx_nodes(nx_graph_korean, pos_korean, node_size=1000)
    	nx.draw_networkx_labels(nx_graph_korean, pos_korean, labels_korean)
    	nx.draw_networkx_edges(nx_graph_korean, pos_korean, edge_color='k', width=1)
    	korean.show()


	raw_input()
