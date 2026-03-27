# 📰 Auto News Scraper

A Python scraper that fetches the **top HackerNews stories** daily and generates a formatted markdown digest — automated via **GitHub Actions** on a daily cron schedule. Every report is committed back to the repo automatically.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-automated-2088FF?logo=githubactions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Reports

> 📂 **[Browse daily digests in `reports/`](reports/)** — updated automatically every morning at 08:00 UTC.

## ✨ Features

- **Daily top 30 HackerNews stories** — score, author, comment count
- **Markdown digest** saved as `reports/YYYY-MM-DD.md`
- **Automated cron job** — GitHub Actions runs at 08:00 UTC every day
- **Manual trigger** — run from GitHub UI anytime via `workflow_dispatch`
- **Parallel fetching** — ThreadPoolExecutor for fast multi-story retrieval
- **Zero cost** — runs entirely on GitHub Actions free tier (2000 min/month)

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.10+ | Core language |
| `requests` | HTTP client for HN API |
| `ThreadPoolExecutor` | Parallel story fetching |
| GitHub Actions | Cron scheduling & automation |
| HackerNews Firebase API | Data source (public, no auth) |

## 📦 Run Locally

```bash
# Clone the repo
git clone https://github.com/ByteMe-UK/auto-news-scraper.git
cd auto-news-scraper

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python run.py

# Or fetch fewer stories
python run.py --limit 10
```

Report saved to `reports/YYYY-MM-DD.md`.

## 📁 Project Structure

```
auto-news-scraper/
├── run.py                         ← Entry point (CLI)
├── scraper/
│   ├── fetcher.py                 ← HackerNews API client (parallel fetch)
│   └── reporter.py                ← Markdown report generator
├── reports/                       ← Daily digests committed here
│   └── 2026-03-27.md
├── .github/
│   └── workflows/
│       └── daily_scrape.yml       ← GitHub Actions cron job
├── requirements.txt
├── LICENSE
└── README.md
```

## ⚙️ How the Automation Works

```
08:00 UTC every day
    └─▶ GitHub Actions runner spins up (ubuntu-latest)
    └─▶ pip install -r requirements.txt
    └─▶ python run.py --limit 30
            └─▶ GET hacker-news.firebaseio.com/v2/topstories.json
            └─▶ Parallel GET for each story (ThreadPoolExecutor)
            └─▶ Sort by score, format as markdown
            └─▶ Save to reports/YYYY-MM-DD.md
    └─▶ git add reports/ && git commit && git push
```

## 🔧 Customisation

Edit `.github/workflows/daily_scrape.yml` to change:
- **Schedule:** `cron: "0 8 * * *"` → any cron expression
- **Story count:** `--limit 30` → any number up to 500

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Part of the [ByteMe-UK](https://github.com/ByteMe-UK) portfolio collection.**
