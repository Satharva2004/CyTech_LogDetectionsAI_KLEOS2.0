# CyTech KLEOS2.0 <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="30" height="30" />
## AI Powered Log Analysis and Anomaly Detections 
### Overview
This project is part of the Kleos 2.0 hackathon and aims to develop an AI-driven system for real-time log monitoring and anomaly detection. With the exponential growth of digital assets and interconnected systems, the volume and complexity of log data have increased significantly. Traditional methods of manual log analysis and rule-based anomaly detection are no longer sufficient to identify sophisticated threats and abnormal behaviors effectively. This project leverages advanced artificial intelligence (AI) techniques to address these challenges, enhancing cybersecurity measures and ensuring robust data protection.
## Project Features
### Data Processing and Feature Engineering
- Preprocessing: Cleaning and normalizing log data, extracting relevant features such as timestamps, source IP addresses, event types, and log messages.
- Feature Engineering: Transforming raw log data into structured features using techniques like tokenization, one-hot encoding, and dimensionality reduction.
  
![Screenshot (154)](https://github.com/Satharva2004/CyTech_LogDetectionsAI_KLEOS2.0/assets/84018291/c3e704df-8b83-46fa-a346-d5e8b522cb94)
----

### AI and Machine Learning Models
#### Anomaly Detection Models:
- Isolation Forest: Detecting anomalies in high-dimensional data.
- Random Forest: Detecting anomalies also to show difference.
---

#### NLP Models:
- BERT and Vader : Understanding and analyzing log messages using natural language processing.
- Key Files:
  
  1. Data Generation: Generates synthetic log data.
     
  2. Trend Analysis: Analyzes and visualizes trends in the log data.

  3. Clustering: Groups similar log entries together.
  
  4. Correlation Analysis: Identifies relationships between different event types.
  
  5. Sentiment Analysis: Classifies log messages into positive, negative, or neutral sentiments and visualizes the results.
 
![lkjhgfds](https://github.com/Satharva2004/CyTech_LogDetectionsAI_KLEOS2.0/assets/84018291/ff41a1af-239c-485e-a565-8229ba2ed841)
![Screenshot (170)](https://github.com/Satharva2004/CyTech_LogDetectionsAI_KLEOS2.0/assets/84018291/16fd936d-dabe-484d-8f17-42a3e03cf7fc)

---
### Real-Time Monitoring and Alerting
- Streaming Analytics: Using Apache Spark Streaming
- Alert Generation: Triggering alerts based on the output of anomaly detection models.
---
### Visualization and User Interface
#### Web Application:
- Dashboard Overview: Displaying key metrics such as total logs processed, number of anomalies detected, and system status.
- Log Data Visualization: Interactive charts and graphs to explore trends, patterns, and anomalies.
- Alerts Panel: Highlighting real-time alerts with details like anomaly type, severity, timestamp, and affected resources.
---

## Prerequisites
- Python 3.x
- Jupyter Notebook
- ReactJS
- Apache Spark, Kafka
- Libraries: pandas, numpy, sklearn, matplotlib, gzip, os, datetime, nltk etc
