# 🐍 Year Coding — Python Practice

A personal Python learning journal — one script a day, tracked by date.

## 📖 About

This repository documents a year-long Python coding practice journey. Each file is named by date and topic, making it easy to trace progress over time. The scripts cover a wide range of Python concepts, from fundamentals to web automation and data handling.

## 🗂️ Topics Covered

| Area | Description |
|------|-------------|
| **Python Basics** | Core language practice — variables, loops, functions, data structures |
| **Selenium Web Automation** | Browser automation scripts for Chrome and Firefox |
| **Web Scraping** | Extracting data from websites using Python |
| **File System Operations** | Listing and managing files from directories |
| **Excel / Data Handling** | Working with `.xlsx` files using Python (`PracticeExcel.py`) |
| **Data-Driven Testing** | Reading test data from external sources (`DatadrivenTesting.py`) |
| **Zerodha Kite Login** | Automating login to the Kite trading platform via Selenium |
| **NSE Chart Scraping** | Fetching stock chart data from NSE (`02102022_kite_nse_chart.py`) |
| **Language Detection** | Detecting language from text (`05092002_languagedection.py`) |
| **Diagrams** | Python-based diagram generation (`Diagram.py`) |
| **Quizzes** | Practice quiz scripts (`17sepquiz.py`, `QUIZ18OCT.py`) |

## 📁 File Naming Convention

Files follow a `DDMMYYYY_topic_N.py` naming pattern:

```
01092022_practice1.py      → 1st Sep 2022, general practice
05092022_selenium1.py      → 5th Sep 2022, Selenium session 1
01102022_kitelogin.py      → 1st Oct 2022, Kite login automation
```

## 🛠️ Tech Stack

- **Language:** Python 3
- **Key Libraries:**
  - `selenium` — browser automation
  - `openpyxl` / `xlrd` — Excel file handling
  - `requests` / `BeautifulSoup` — web scraping
  - `langdetect` — language detection
  - `pipenv` — dependency management (see `Pipfile`)

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/halovivek/yearcoding.git
   cd yearcoding
   ```

2. **Install dependencies**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

3. **Run any script**
   ```bash
   python 01092022_practice1.py
   ```

> **Note:** Selenium scripts require a compatible WebDriver (ChromeDriver or GeckoDriver) installed and available in your system PATH.

## 📅 Practice Timeline

| Period | Focus |
|--------|-------|
| Aug 2022 | Python fundamentals, file system operations |
| Sep 2022 | Selenium web automation, web scraping |
| Oct 2022 | Kite trading platform automation, NSE data, data-driven testing |

## 🤝 Contributing

This is a personal learning repo, but feel free to fork it and use it as inspiration for your own daily coding practice!

---

*"Consistency beats talent when talent doesn't practice consistently."*
