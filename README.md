# AI Newsletter Agent

An autonomous AI agent that researches the latest AI agent news, summarizes articles, generates a newsletter, reviews its own output, and publishes the final newsletter.

---

## Assignment Objective
 
Build a mini autonomous AI agent that receives a plain English goal and completes the entire workflow automatically. 

Example Goal:

> Create a weekly newsletter on latest AI agent news and send it to our subscribers.

---

## Features

* Autonomous execution from one function call
* Multi-step reasoning workflow
* Latest AI news research
* AI-powered summarization
* Newsletter generation (Markdown)
* Self-review and refinement
* Human-in-the-Loop mode
* Streamlit frontend

---

## Workflow

Goal Input
↓
Planning
↓
Research
↓
Summarization
↓
Newsletter Generation
↓
Self Review
↓
Approval (Optional)
↓
Publish Output

---

## Tech Stack

* Python
* LangChain
* Google Gemini API
* Tavily Search
* Streamlit

---

## Project Structure

```plaintext
newsletter-agent/
│
├── app.py
├── agent.py
├── tools.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── output/
│   └── newsletter.md
└── venv/
```

---

## Installation

Clone repository:

```bash
git clone YOUR_GITHUB_REPOSITORY
cd newsletter-agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```env
GOOGLE_API_KEY=YOUR_GEMINI_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

Open browser:

```plaintext
http://localhost:8501
```

---

## Modes

### Fully Autonomous

Runs all stages automatically.

### Human-in-the-Loop

Requires approval before publishing.

---

## Output

Generated newsletter is saved:

```plaintext
output/newsletter.md
```

---

## Example Goal

```plaintext
Create a weekly newsletter on latest AI agent news and send it to subscribers.
```

---

## Assignment Requirements Covered

✔ Multi-step reasoning
✔ Tool usage
✔ Autonomous execution
✔ Self-reflection
✔ Human approval mode
✔ Frontend interface

---

## Author

Deepkamal Gupta
