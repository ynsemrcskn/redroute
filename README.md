![image](https://github.com/user-attachments/assets/240f7199-bbfd-4813-a4a4-9696fff15075)

<div align="center">
  <h1><b><code>RedRoute</code> Network Shortest Path Finder & Simulator</b></h1>
  <p><strong>RedRoute</strong> is a conceptual network simulation tool designed to visualize and compute the shortest path between two hosts in a complex network topology. Built using Python, NetworkX, Tkinter, and Matplotlib, <strong>RedRoute</strong> helps users better understand network routing by visualizing paths, nodes, and their interconnections.</p>

  <p>
    <a href="https://s-m-quadri.me/projects/redroute">Homepage</a> ·
    <a href="https://github.com/s-m-quadri/redroute">Repository</a> ·
    <a href="https://github.com/s-m-quadri/redroute/releases">Download Executable</a> ·
    <a href="mailto:dev.smq@gmail.com">Contact</a>
  </p>

  <a href="https://github.com/s-m-quadri/redroute/releases">
         <img src="https://custom-icon-badges.demolab.com/github/v/tag/s-m-quadri/redroute?label=Version&labelColor=302d41&color=f2cdcd&logoColor=d9e0ee&logo=tag&style=for-the-badge" alt="Release Version"/>
  </a>
  <a href="https://www.codefactor.io/repository/github/s-m-quadri/redroute"><img src="https://img.shields.io/codefactor/grade/github/s-m-quadri/redroute?label=CodeFactor&labelColor=302d41&color=8bd5ca&logoColor=d9e0ee&logo=codefactor&style=for-the-badge" alt="GitHub Readme Profile Code Quality"/></a>
  <a href="https://github.com/s-m-quadri/redroute/issues">
    <img src="https://custom-icon-badges.demolab.com/github/issues/s-m-quadri/redroute?label=Issues&labelColor=302d41&color=f5a97f&logoColor=d9e0ee&logo=issue&style=for-the-badge" alt="Issues"/>
  </a>
  <a href="https://github.com/s-m-quadri/redroute/pulls">
    <img src="https://custom-icon-badges.demolab.com/github/issues-pr/s-m-quadri/redroute?label=PRs&labelColor=302d41&color=ddb6f2&logoColor=d9e0ee&logo=git-pull-request&style=for-the-badge" alt="Pull Requests"/>
  </a>
  <a href="https://github.com/s-m-quadri/redroute/graphs/contributors">
    <img src="https://custom-icon-badges.demolab.com/github/contributors/s-m-quadri/redroute?label=Contributors&labelColor=302d41&color=c9cbff&logoColor=d9e0ee&logo=people&style=for-the-badge" alt="Contributors"/>
  </a>

  <p>
    <a href="https://github.com/s-m-quadri/redroute/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml">Report Bug</a> · 
    <a href="https://github.com/s-m-quadri/redroute/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml">Request Feature</a> · 
    <a href="https://github.com/s-m-quadri/redroute/discussions/new?category=q-a">Ask Question</a> · 
    <a href="https://github.com/Safouene1/support-palestine-banner/blob/master/Markdown-pages/Support.md">Support 🇵🇸 Palestine<a>
  </p>
</div>


## 📌 **Features**

* **Interactive GUI** built with Tkinter, allowing users to select source and destination hosts.
* **Shortest Path Calculation** using NetworkX's graph algorithms to find the optimal route between any two hosts.
* **Dynamic Visualization** of the network topology with Matplotlib, displaying nodes (hosts and switches) and edges (connections) clearly.
* **Red-themed Design** for an intuitive and aesthetically pleasing user interface.

## 📌 **Installation**

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

## 📌 **Usage**

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

## 📌 **Network Topology**

The network topology is based on a series of interconnected switches with hosts distributed in a circular pattern. Switches are placed in a structured grid layout to ensure a variety of routing possibilities, which allows the app to find meaningful routing paths between any selected hosts.

## 📌 **License**

This project is licensed under the **GNU General Public License (GPL)** - see the [LICENSE](LICENSE) file for details.

## 📌 **Contact Support**

For any issues or support, please contact:
**Email**: [dev.smq@gmail.com](mailto:dev.smq@gmail.com)
