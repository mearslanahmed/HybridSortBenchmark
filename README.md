# Hybrid MergeSort Benchmark


## Overview

This project implements a **Hybrid MergeSort** algorithm in Java.  
The algorithm switches to **Insertion Sort** when subarray size ≤ threshold `s`.  
It benchmarks performance for various `s` values and plots how runtime changes.

---

## Requirements

- Java 8 or later (JDK)
- Python 3 (only for plotting)
- `matplotlib` (for the graph)

---

## How to Run

### **1. Compile**

```bash
javac HybridSortBenchmark.java
```

### **2. Run**

```bash
java -Xmx4g HybridSortBenchmark <ArraySize> <SamplePoints>
```

- Examples:
- Run with auto-estimated array size

```bash
java -Xmx4g HybridSortBenchmark
```

- Run with fixed array size 20000 and 40 sample points

```bash
java -Xmx4g HybridSortBenchmark 20000 40
```

- This will:

  - Create a random integer array of given size.

  - Run Hybrid MergeSort for multiple s thresholds.

  - Write results in results.csv.

## Setting Up Virtual Environment (Recommended)

To keep dependencies isolated, please create and activate a virtual environment before installing packages.

### For Windows

- Run these command one by one in terminal of vs code

```bash
python -m venv venv
venv\Scripts\activate
```

### For macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

- Once activated, your terminal will show (venv) at the start of the line.

Now move on to the Plotting part...

## Plotting the Graph

1. First install dependecies with this command

```bash
pip install -r requirements.txt
```

2. Then run this command

```bash
python plot_results.py
```

## 📊 Graph Results

Here are the output graphs generated from the Hybrid MergeSort benchmark:

<p align="center">
  <img src="Graphs SS/Figure_1.png" alt="Hybrid Sort Graph 1" width="500"/>
  <br/>
  <img src="Graphs SS/Figure_2.png" alt="Hybrid Sort Graph 2" width="500"/>
</p>


## Author

Developed by Arslan Ahmed

For client academic project submission (Hybrid MergeSort Benchmark)


If you have any other project you want help please feel free to contact me. If you like my service please refer me to other as it will help me grow. Thanks in advance for referring me.

Email: arslanahmednaseem@gmail.com

