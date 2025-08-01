# Subnet Analysis & Visualization

> DevOps internship task

## About This Project

This repository was part of a hands-on internship task focused on subnet analysis and Docker containerization. The goal? Build a tool that could:
- Analyze IP subnets and calculate usable hosts
- Generate clear, shareable reports across formats (CSV, JSON, XLSX)
- Visualize network distributions with Matplotlib
- Wrap the logic into a Docker container for scalable deployment

## What I Learned

- **Subnet math** is more satisfying than I expected. There’s something poetic about counting usable IPs and watching them fit like puzzle pieces.
- **Python’s `ipaddress` module** is underrated — slicing through networks like butter.
- **Matplotlib** taught me that design and data truly go hand in hand. A well-placed color or axis label changes the story entirely.
- **Docker** turned my script into a deployable service — and made me rethink how I package anything going forward.

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
