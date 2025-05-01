# AI-Powered Intrusion Detection System (IDS)

This project is an AI-powered Intrusion Detection System (IDS) that monitors live network traffic, detects malicious activity using machine learning, and automatically blocks suspicious IP addresses. It integrates backend packet sniffing, ML classification, automatic IP blocking, and an optional Tkinter GUI for local monitoring.

## Features

- Real-time packet sniffing using Scapy
- Machine learning classification for malicious vs. benign traffic
- Automated IP blocking with iptables (Linux only)
- JSON-based logging of all threat events
- Optional Tkinter GUI for local alert monitoring and control

## Tech Stack

- **Language:** Python 3.8+
- **Backend:** Scapy (packet capture), iptables (IP blocking), JSON logger
- **Machine Learning:** scikit-learn, pandas, numpy, joblib
- **Frontend (optional):** Tkinter GUI for live display

## How I Built the ML Model

The ML model was built using a Jupyter notebook (`model_training.ipynb`) with the following steps:

1. **Dataset loading:** Combined multiple CSV files of network traffic data.
2. **Data cleaning:** Removed nulls, infinities, and duplicate rows.
3. **Label encoding:** Converted the target column (`Label`) to numeric values.
4. **Feature preparation:** Selected and organized all feature columns (excluding `Label`).
5. **Train-test split:** Divided the dataset into training and testing sets (typically 70%-30%).
6. **Model training:** Trained a `RandomForestClassifier` to classify packets.
7. **Evaluation:** Calculated precision, recall, f1-score, and accuracy to evaluate performance.
8. **Model saving:** Exported the trained model as `model.pkl` using joblib for runtime use.

The saved `model.pkl` is loaded at runtime by the backend detector module, which classifies live packets.

## System Workflow

- Packets are sniffed in real time using Scapy.
- Extracted packet features are passed to the ML detector.
- If an attack is predicted, the backend automatically:
  - Logs the event to a JSON file.
  - Blocks the source IP using iptables.
  - Sends data to the GUI (if running) for live display.

## Future Improvements

- Replace JSON logs with a database (e.g., SQLite)
- Add a web-based dashboard (Flask, FastAPI)
- Improve feature extraction and normalization
- Add multi-model support (deep learning, anomaly detection)
- Implement Windows/macOS compatibility (no iptables)
- Add automated unit and integration tests
