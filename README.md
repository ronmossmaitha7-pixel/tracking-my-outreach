# Tracking My Outreach

A Python-based outreach analytics and lead tracking tool designed to summarize client outreach performance across multiple acquisition channels. Built to turn raw outreach logs into actionable insights, it automatically calculates response rates, breaks down volume by channel, and highlights scheduled calls and hot leads requiring follow-up.

## Features

* **Key Metrics & Conversion Summary:** Automatically calculates total messages sent, replies received, overall reply percentage rate, and total calls booked.
* **Multi-Channel Breakdown:** Aggregates outreach volume across platforms including LinkedIn, WhatsApp, X (DM), Referral, Upwork, and In-person interactions.
* **Call Follow-Up Reminders:** Filters and lists booked prospects alongside their outreach dates and scheduled call dates so no appointment is missed.
* **Hot Lead Prioritization:** Highlights prospects who have replied, displaying their name, acquisition channel, and specific project notes (e.g., automation, API work, scope documents).
* **Structured Data Processing:** Parses structured dictionary records containing outreach dates, contact names, channels, statuses, and custom notes.

## Tech Stack

* **Language:** Python 3
* **Data Structures:** Native Python Dictionaries & Lists
* **Environment:** Command-Line Interface (CLI)

## Example Output

```text
OUTREACH TRACKER SUMMARY
========================================
Total messages sent:  8
Replies received:     4  (50% reply rate)
Calls booked:         1

By channel:
  LinkedIn      3 sent
  WhatsApp      1 sent
  X (DM)        1 sent
  Referral      1 sent
  Upwork        1 sent
  In person     1 sent

Calls to follow up:
  Ronmoss Maitha (2026-07-10) -- Call on July 16

Hot leads (replied):
  Martin Katana via LinkedIn -- Interested in monthly report automation
  Hilda Katana via Referral -- Friend's contact, needs API work
  Tezzoz Ltd via LinkedIn -- Wants scope document
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd tracking-my-outreach
   ```
2. Run the script:
   ```bash
   python trackingoutreache.py
   ```
