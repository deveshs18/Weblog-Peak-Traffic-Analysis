# Weblog-Peak-Traffic-Analysis
Overview
This project uses MapReduce to analyze website traffic logs and determine peak traffic hours. The goal is to help administrators understand user activity patterns, optimize server loads, and strategically place advertisements.

By processing web logs, we identify which time of the day experiences the highest user engagement

Prerequisites
Ensure you have the following installed:

Hadoop 2.6.5 (HDP Sandbox)
Python 2.7
mrjob (pip install mrjob)

Data Preprocessing
bash scripts/data_cleaning.sh

Upload Data to HDFS
Move the cleaned data to Hadoop's HDFS:
hdfs dfs -mkdir -p /user/root/input
hdfs dfs -put data/cleaned_weblog.csv /user/root/input/

Run MapReduce Job
python scripts/weblog_peak_traffic.py -r hadoop hdfs:///user/root/input/cleaned_weblog.csv > peak_traffic_output.txt

cat peak_traffic_output.txt
cat peak_traffic_output.txt

Raw Log:
10.128.2.1, [29/Nov/2017:06:59:03, GET /home.php HTTP/1.1, 200

Cleaned Log:
10.128.2.1, 29/Nov/2017:06:59:03, GET /home.php, 200

Key Findings
Peak Traffic Time: The highest traffic occurs at 8 PM (20:00 hours) with 5458 requests.
Least Active Hours: Traffic is minimal between 1 AM and 4 AM, indicating user inactivity.
Corrupt Log Entries: Some logs contained incorrect hour values like "51" and "64", which were ignored to prevent computation issues.

Author
👤 Devesh Singh
📧 devesh.singh@sjsu.edu
📌 San Jose State University - Data Analytics
