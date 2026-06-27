# AI Business Analyst Agent

An AI-powered business analytics backend built with **Python, Pandas, and FastAPI**. The application analyzes structured business datasets and generates key business insights through REST APIs.

## Features

* Business analytics using Pandas
* FastAPI REST API backend
* Automated insight generation
* JSON API responses
* Interactive Swagger documentation (`/docs`)
* Modular backend architecture

## Business Insights Generated

* Total Sales
* Total Profit
* Top Category
* Top Region
* Most Profitable Region

## Tech Stack

* Python
* FastAPI
* Pandas
* Uvicorn

## Project Structure

```text
backend/
 ├── analyzer.py
 └── main.py
```

## Installation

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to access the interactive API documentation.

## Sample Output

```json
{
  "total_sales": 2297200.86,
  "top_category": "Technology",
  "top_region": "West",
  "total_profit": 286397.02,
  "most_profitable_region": "West"
}
```

## Roadmap

* CSV upload support
* React dashboard
* AI-generated business insights
* Natural language querying
* Interactive charts
* Multi-domain dataset analysis
