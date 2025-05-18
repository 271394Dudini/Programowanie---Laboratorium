import networkx
import matplotlib.pyplot as plt
import random
import imageio

def wideo():
	wideo=[]
	G = networkx.erdos_renyi_graph(15, 0.5)
	pos = networkx.spring_layout(G)
	r = random.choice(list(G.nodes))
	G.nodes[r]['color']='red'
	node_colors = [G.nodes[node].get('color', 'blue') for node in G.nodes]
	networkx.draw(G ,pos , with_labels=True, node_color=node_colors)
	plt.savefig(f"{r"C:\Users\User\Desktop\Programowanie\Lista 4\Zad 4\obraz"}{0}")
	for i in range(50):
		G.nodes[r]['color']='blue'
		r = random.choice(list(G.neighbors(r)))
		G.nodes[r]['color']='red'
		node_colors = [G.nodes[node].get('color', 'blue') for node in G.nodes]
		networkx.draw(G ,pos , with_labels=True, node_color=node_colors)
		plt.savefig(f"{r"C:\Users\User\Desktop\Programowanie\Lista 4\Zad 4\obraz"}{i+1}.png")
		wideo.append(f"{r"C:\Users\User\Desktop\Programowanie\Lista 4\Zad 4\obraz"}{i+1}.png")

	writer=imageio.get_writer(r"C:\Users\User\Desktop\Programowanie\Lista 4\Zad 4\test.mp4", fps=1)
	for i in wideo:
		writer.append_data(imageio.v2.imread(i))
	writer.close()

wideo()

