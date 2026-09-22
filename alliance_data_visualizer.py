import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import xgi

def show_hypergraph(path):
    H = xgi.read_hif(path)

    labels = {node: str(int(node.removeprefix("player-0"))) for node in H.nodes}

    fig, ax = plt.subplots(figsize=(12, 8))
    #pos = xgi.circular_layout(H)
    pos = xgi.barycenter_spring_layout(H, seed=42, k=0.3)
    xgi.draw(
        H,
        ax=ax,
        pos=pos,
        node_labels=labels,
        hyperedge_labels=False,
        node_size=20,
        hull=True
    )

    legend_items = [
        Line2D([], [], linestyle="none", label=f"{labels[node]}  {H.nodes[node]['name']}")
        for node in sorted(H.nodes, key=lambda node: int(node.split("-")[-1]))
    ]
    ax.legend(
        handles=legend_items,
        title="Players",
        loc="upper right",
        bbox_to_anchor=(0, 1),
        frameon=False,
    )

    fig.tight_layout()
    plt.show()
    
show_hypergraph("data/season_19/r1_alliances.json")