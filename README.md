# Network-and-Port-Scanner

![Python](https://img.shields.io/badge/python-3.x-blue)
![Type](https://img.shields.io/badge/tool-port--scanner-orange)
![Status](https://img.shields.io/badge/status-active-success)

## Description

This project is a simple TCP port scanner written in Python using the socket library. The script scans a target host across a specified port range and reports which ports are open. It also measures the total scan time.

This tool demonstrates practical knowledge of computer networking, socket programming, and basic cybersecurity reconnaissance techniques.

---

## Features

* Accepts target host as user input
* Resolves domain name to IP address
* Scans a configurable TCP port range
* Detects open ports using TCP connect method
* Prints open ports in real time
* Measures total scan duration

---

## Technologies Used

* Python 3
* socket module
* TCP networking
* Basic port scanning logic

---

## How It Works

* User enters a hostname or domain
* Script converts hostname → IP address
* Iterates through ports 50–499
* Attempts TCP connection using `connect_ex`
* If connection succeeds → port is reported OPEN
* Scan time is calculated and displayed

---

## Port Range

Default scan range:

50 → 499

You can modify this line in the code to change range:

for i in range(50, 500):

---

## How to Run

Run from terminal:

python port_scanner.py

Example:

enter the host to be scanned: example.com

---

## Sample Output

starting scan on host: 93.184.216.34
port 80: OPEN
port 443: OPEN
Time taken: 2.31 seconds

---

## Use Cases

* Learning socket programming
* Basic network reconnaissance practice
* Port exposure testing in lab environments
* Cybersecurity fundamentals training

---

## Notes

* Scan speed depends on network latency
* Some hosts block scan attempts
* Use only on systems you are authorized to test

---

## Author

Your Name
