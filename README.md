# 📦 Zippy

A Python-based log file management tool that automatically generates sample log files and compresses selected logs into a ZIP archive via a GUI interface.

> ⚠️ **Note:** Real log files are confidential. This project automatically generates sample log files for demonstration purposes, simulating a real-world log management workflow.

---

## 📌 Overview

Zippy simulates a log file management system used in embedded or system-level environments. It automates the process of organizing, filtering, and compressing log files — tasks that are common in real-world QA and system diagnostics workflows.

---

## 🔄 Workflow

```
1. Load configuration (paths.xml, date.xml)
        ↓
2. Auto-generate sample log files
        ↓
3. Launch GUI — user selects a log folder
        ↓
4. Filter and compress selected logs into a .zip file
```

---

## 🗂️ Project Structure

```
zippy/
├── config/
│   ├── paths.xml            # Path configuration
│   └── date.xml             # Date/time configuration
├── utils/
│   ├── makeExampleFiles.py  # Sample log file generator
│   ├── makeGUI.py           # GUI (tkinter)
│   ├── makeZip.py           # ZIP compression
│   └── makeAppLog.py        # Logger setup
├── logs/                    # App execution logs (auto-generated)
├── sampleLogs/              # Generated sample log files (auto-generated)
├── .gitignore
└── main.py                  # Entry point
```

---

## ✨ Features

- **Auto-generates sample log files** — `.log.gz`, `.log`, `.txt` files based on XML config
- **XML-based configuration** — paths and date/time settings managed separately
- **GUI folder selection** — users select a log folder via a tkinter interface
- **ZIP compression** — selected log folder is compressed into a `.zip` file
- **Structured logging** — execution logs saved per run with timestamps (`logs/app_YYYY_MM_DD_HH_MM_SS.log`)
- **OOP design** — each utility is encapsulated in a class

---

## 🛠️ Tech Stack

- **Language:** Python 3.9
- **GUI:** tkinter
- **Libraries:** `gzip`, `zipfile`, `xml.etree.ElementTree`, `logging`, `os`, `shutil`, `datetime`

---

## ⚙️ Configuration

### config/paths.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<paths>
    <path name="mainPath">.</path>
    <path name="output">sampleLogs</path>
</paths>
```

### config/date.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<datetime>
    <year>2026</year>
    <month>5</month>
    <day>1</day>
    <hour>11</hour>
    <minute>0</minute>
    <second>0</second>
</datetime>
```

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/yeajieo/zippy.git
cd zippy
```

**2. Set up config files**
```bash
# Edit config/paths.xml and config/date.xml as needed
```

**3. Run**
```bash
python main.py
```

---

## 📋 Sample Log Files Generated

| Type | Example |
|------|---------|
| `.log.gz` | `1-main.log_2026_5_1_11_1_01.log.gz` |
| `.log` | `bootup.log`, `crash.log`, `system.log` |
| `.txt` | `calibration_values.txt` |
| Directory | `CLU/`, `Cali/`, `Sync/` |

---

## 📝 Logging

Every run generates a timestamped log file under `logs/`:

```
2026-05-02 11:00:00 - INFO - makeExampleFiles.py::load_paths - Config loaded successfully
2026-05-02 11:00:00 - INFO - makeExampleFiles.py::create_allFiles - All files created successfully
2026-05-02 11:00:01 - INFO - makeZip.py::makeZip - ZIP created successfully
```

---

## 🔒 Security

- `config/paths.xml` is excluded from version control via `.gitignore` to prevent local path exposure
- Sample files replace real log data to protect confidential system information
