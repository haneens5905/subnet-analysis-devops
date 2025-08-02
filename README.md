# Subnet Analysis & Visualization

> DevOps internship task

## About This Project

This repository was part of a hands-on internship task focused on subnet analysis and Docker containerization. The goal? Build a tool that could:
- Analyze IP subnets and calculate usable hosts
- Generate clear, shareable reports across formats (CSV, JSON, XLSX)
- Visualize network distributions with Matplotlib
- Wrap the logic into a Docker container for scalable deployment

### 📘 What I Learned

- **Subnet analysis** turned out to be more insightful than expected. Understanding how IP ranges are calculated and allocated revealed the practical depth behind something I previously viewed as abstract.
- **Python’s `ipaddress` module** turned out to be a hidden gem. It made network slicing feel effortless, and clarified concepts I had only seen in theory.
- **Matplotlib** deepened my appreciation for the role of design in data presentation. A single color or axis label can dramatically shift how insights are interpreted.
- **Docker** reshaped my approach to packaging. Transforming a simple script into a deployable service showed me what real-world scalability looks like.

## Folder Breakdown

- `/Visualize.py` → plots subnet sizes in a bar chart
- `/Report/report.md` → written summary of the analysis
- `/group_sizes.csv` → raw output of subnet sizing
- `/network_plot.png` → visual representation of subnet distribution
- `/README.md` → you’re reading it right now

## Tech Stack

| Tool        | Role                            |
|-------------|----------------------------------|
| Python      | Subnet analysis & visualization |
| Pandas      | Data manipulation               |
| Matplotlib  | Graphing subnet metrics         |
| Docker      | Containerization                |
| Git/GitHub  | Version control & hosting       |

## How to Run Locally (Docker Version)

```bash
docker build -t subnet-analyzer .
docker run subnet-analyzer

