# **RedRoute: Network Shortest Path Finder & Simulator**

**RedRoute** is a conceptual network simulation tool designed to visualize and compute the shortest path between two hosts in a complex network topology. Built using Python, NetworkX, Tkinter, and Matplotlib, **RedRoute** helps users better understand network routing by visualizing paths, nodes, and their interconnections.

## **Features**

* **Interactive GUI** built with Tkinter, allowing users to select source and destination hosts.
* **Shortest Path Calculation** using NetworkX's graph algorithms to find the optimal route between any two hosts.
* **Dynamic Visualization** of the network topology with Matplotlib, displaying nodes (hosts and switches) and edges (connections) clearly.
* **Red-themed Design** for an intuitive and aesthetically pleasing user interface.

## **Installation**

### 1. **Clone the repository**

```bash
git clone https://github.com/s-m-quadri/redroute.git
cd redroute
```

### 2. **Install dependencies**

Make sure Python 3.12.9 is installed. Then, install the necessary packages:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

```txt
networkx
matplotlib
tkinter
```

## **Usage**

1. Launch the application by running `main.py`:

   ```bash
   python main.py
   ```

2. **Select Source and Destination**:

   * Use the dropdown menus to choose the source and destination hosts.

3. **Find the Shortest Path**:

   * Click the "🔍 Find Shortest Path" button to calculate the path.
   * The shortest path will be visualized on the network graph, with red edges highlighting the selected path.

4. **View Status**:

   * The status bar will update to show the progress of the calculation (e.g., "Finding shortest path..." or "Path found: H0 ➜ S0 ➜ S4 ➜ H7").

## **Network Topology**

The network topology is based on a series of interconnected switches with hosts distributed in a circular pattern. Switches are placed in a structured grid layout to ensure a variety of routing possibilities, which allows the app to find meaningful routing paths between any selected hosts.

## **Contributing**

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Submit a pull request for review.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you want to tweak any part of this!


Here's the updated `README.md` with the changes you've requested:

---

# **RedRoute: Network Shortest Path Finder & Simulator**

**RedRoute** is a conceptual network simulation tool designed to visualize and compute the shortest path between two hosts in a complex network topology. Built using Python, NetworkX, Tkinter, and Matplotlib, **RedRoute** helps users better understand network routing by visualizing paths, nodes, and their interconnections.

## **Features**

* **Interactive GUI** built with Tkinter, allowing users to select source and destination hosts.
* **Shortest Path Calculation** using NetworkX's graph algorithms to find the optimal route between any two hosts.
* **Dynamic Visualization** of the network topology with Matplotlib, displaying nodes (hosts and switches) and edges (connections) clearly.
* **Red-themed Design** for an intuitive and aesthetically pleasing user interface.

## **Installation**

### 1. **Clone the repository**

```bash
git clone https://github.com/s-m-quadri/redroute.git
cd redroute
```

### 2. **Install dependencies**

Make sure Python 3.x is installed. Then, install the necessary packages:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

```txt
networkx
matplotlib
tkinter
```

## **Usage**

1. Launch the application by running `main.py`:

   ```bash
   python main.py
   ```

2. **Select Source and Destination**:

   * Use the dropdown menus to choose the source and destination hosts.

3. **Find the Shortest Path**:

   * Click the "🔍 Find Shortest Path" button to calculate the path.
   * The shortest path will be visualized on the network graph, with red edges highlighting the selected path.

4. **View Status**:

   * The status bar will update to show the progress of the calculation (e.g., "Finding shortest path..." or "Path found: H0 ➜ S0 ➜ S4 ➜ H7").

### 📌 **PyInstaller Executable**

You can also download the **RedRoute** executable built with **PyInstaller**. The `.exe` file, packaged using `setup.spec`, is available in the [Releases](https://github.com/s-m-quadri/redroute/releases) section of this repository.

## **Network Topology**

The network topology is based on a series of interconnected switches with hosts distributed in a circular pattern. Switches are placed in a structured grid layout to ensure a variety of routing possibilities, which allows the app to find meaningful routing paths between any selected hosts.

## **License**

This project is licensed under the **GNU General Public License (GPL)** - see the [LICENSE](LICENSE) file for details.

## **Contact Support**

For any issues or support, please contact:
**Email**: [dev.smq@gmail.com](mailto:dev.smq@gmail.com)