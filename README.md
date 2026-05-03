# 🗜️ Zippy

A desktop GUI tool that collects and zips log files based on a target datetime.  
Also supports headless CI execution via command-line arguments.

---

## 📌 Overview

Zippy scans a specified folder for log files, filters `.log.gz` files (main logs only) within a **±3~6 minute window** around the given datetime, copies them alongside all `.log` / `.txt` files into a workspace, and packages everything into a single ZIP file.

---

## ✨ Features

- 🖥️ **GUI mode** — Browse folder, enter date/time, and click Run (`main.py`)
- ⚙️ **CI mode** — Run headlessly with `--output_path`, `--date`, `--time` args (`main_ci.py`)
- 🔍 **Time-based filtering** — Collects `.gz` main logs within a ±3~6 min window of the target time
- 📦 **Auto ZIP** — Outputs a `XXXXLogs_YYMMDD_HHMM.zip` file to the target folder
- 🧪 **Sample file generator** — Auto-generates realistic sample log files for testing
- 📝 **App logging** — Timestamped log files written to `logs/` on every run
- 🔄 **GitHub Actions** — CI workflow triggers on push/PR, with manual `workflow_dispatch` support

---

## 🛠️ Tech Stack

| Category | Detail |
|----------|--------|
| Language | Python 3.9 |
| GUI | Tkinter |
| Compression | `zipfile`, `gzip` |
| Config | XML (`paths.xml`, `date.xml`) |
| Logging | Python `logging` module |
| CI/CD | GitHub Actions |

---

## 📂 Project Structure

```
zippy/
├── main.py                  # GUI entry point
├── main_ci.py               # CI/headless entry point
├── requirements.txt
├── config/
│   ├── paths.xml            # Input/output path config
│   └── date.xml             # Default datetime config for sample generation
├── utils/
│   ├── makeGUI.py           # Tkinter GUI (InputGUI class)
│   ├── makeZip.py           # Core logic: filter, copy, zip (zipFileCreator class)
│   ├── makeExampleFiles.py  # Sample log file generator
│   └── makeAppLog.py        # App logger setup
└── .github/
    └── workflows/
        └── main.yml         # GitHub Actions CI workflow
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Tkinter (bundled with standard Python)

### Installation

```bash
git clone https://github.com/yeajieo/zippy.git
cd zippy
pip install -r requirements.txt
```

---

## ▶️ Usage

### GUI mode

```bash
python main.py
```

1. Click **Search** to select the folder containing log files
2. Enter the target **Date** (`YYYY-MM-DD`) and **Time** (`HH:MM`)
3. Click **Run**
4. Find the output `XXXXLogs_YYMMDD_HHMM.zip` in the selected folder

### CI / Headless mode

```bash
python main_ci.py \
  --output_path ./sampleLogs \
  --date 2026-05-02 \
  --time 11-15-00
```

---

## 🔄 GitHub Actions

The workflow runs automatically on push or PR to `master`, and can also be triggered manually via **Actions → Run workflow** with custom inputs.

| Input | Description | Example |
|-------|-------------|---------|
| `output_path` | Target folder path | `./sampleLogs` |
| `date` | Target date | `2026-05-02` |
| `time` | Target time | `11-15-00` |

---

## 🧪 Sample Log Files

On every run, Zippy auto-generates sample files under `./sampleLogs/` so the tool can be tested immediately:

- 30 × `.log.gz` files (main & system logs, 1-min intervals)
- 10 standalone files: `bootup.log`, `crash.log`, `kernel.log`, `main.log`, etc.
- 3 subdirectories: `CLU/`, `Cali/`, `Sync/`

---

## ⚙️ Configuration

**`config/paths.xml`** — Set input/output folder paths

```xml
<paths>
    <path name="main">.</path>
    <path name="output">./sampleLogs</path>
</paths>
```

**`config/date.xml`** — Set default datetime for sample file generation

```xml
<datetime>
    <year>2026</year><month>5</month><day>2</day>
    <hour>11</hour><minute>0</minute><second>0</second>
</datetime>
```

---

## 👩‍💻 Author

**yeajieo** · [@yeajieo](https://github.com/yeajieo)
