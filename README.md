# Illumio Technical Assessment

## Overview

A program that can parse a file containing flow log data and maps each row to a tag based on a lookup table. The lookup table is defined as a csv file, and it has 3 columns, dstport,protocol,tag.   The dstport and protocol combination decide what tag can be applied.

## Assumptions

1. **Log Format**: 
   - The program only supports the default log format for flow logs, specifically **version 2** logs.
   - Any custom log formats or other versions of flow logs are **not supported**.
   - The log entries are assumed to be whitespace-separated.

2. **Lookup Table Format**: 
   - The lookup table is provided as a CSV file with **three columns**: `dstport`, `protocol`, and `tag`.
   - Protocol matching is **case-insensitive**.
   - The lookup file can contain up to **10,000 mappings**, and the program will handle them efficiently.

3. **Program Limits**:
   - The program is designed to handle flow log files up to **10 MB** in size.
   - The output includes entries that were **tagged** based on the lookup table and **untagged** entries that did not match any tag.

4. **File Encoding**:
   - Input and output files are assumed to be in plain **ASCII text**.

## Requirements

- Python 3.x
- The following files:
  - **Flow Log File**: A text file containing flow log entries (e.g., `flow_logs.txt`).
  - **Lookup Table File**: A CSV file containing the lookup table with columns `dstport`, `protocol`, and `tag` (e.g., `lookup_table.csv`).


## Usage

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

### 2. Run the Program

