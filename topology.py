import networkx as nx
import math

def create_topology():
    G = nx.Graph()
    pos = {}

    # Create 8 hosts in a circular arrangement
    hosts = [f'H{i}' for i in range(8)]
    radius = 8  # Increased radius for better spacing
    for i, h in enumerate(hosts):
        angle = 2 * math.pi * i / len(hosts)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        G.add_node(h, type='host')
        pos[h] = (x, y)

    # Create 13 switches in a spaced-out grid + perimeter
    switches = [f'S{i}' for i in range(13)]
    spacing = 4  # Increased spacing between switch nodes
    grid_positions = [
        (-spacing, spacing), (0, spacing), (spacing, spacing),        # Top row
        (-spacing, 0),     (0, 0),     (spacing, 0),                  # Middle row
        (-spacing, -spacing), (0, -spacing), (spacing, -spacing),    # Bottom row
        (-2 * spacing, spacing // 2), (2 * spacing, spacing // 2),   # Left and right
        (-2 * spacing, -spacing // 2), (2 * spacing, -spacing // 2)  # Left and right lower
    ]
    for sw, p in zip(switches, grid_positions):
        G.add_node(sw, type='switch')
        pos[sw] = p

    # Connect hosts to nearby switches
    G.add_edges_from([
        ('H0', 'S0'), ('H1', 'S2'),
        ('H2', 'S5'), ('H3', 'S8'),
        ('H4', 'S6'), ('H5', 'S3'),
        ('H6', 'S10'), ('H7', 'S9'),
    ])

    # Inter-switch mesh connections
    inter_links = [
        # Horizontal connections
        ('S0', 'S1'), ('S1', 'S2'),
        ('S3', 'S4'), ('S4', 'S5'),
        ('S6', 'S7'), ('S7', 'S8'),
        ('S9', 'S0'), ('S10', 'S2'),
        ('S11', 'S6'), ('S12', 'S8'),

        # Vertical connections
        ('S0', 'S3'), ('S3', 'S6'),
        ('S1', 'S4'), ('S4', 'S7'),
        ('S2', 'S5'), ('S5', 'S8'),

        # Spine from center
        ('S4', 'S9'), ('S4', 'S10'),
        ('S4', 'S11'), ('S4', 'S12')
    ]
    G.add_edges_from(inter_links)

    return G, hosts, pos
