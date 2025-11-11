# RideSmart

A lightweight Flask app to compare motorcycles and explore model data.

Repository: https://github.com/Abhinav-Praveen004/RideSmart

## Overview

RideSmart (local name: RideSmartCompare) loads motorcycle data (CSV), stores it via SQLAlchemy, and provides an interface to compare models.

This repo contains a small Flask app under `backend/`, templates under `templates/`, static files under `static/`, and sample data in `data/motorcycles.csv`.

## Features

- Load motorcycle data from `data/motorcycles.csv` into a local SQLite database
- Compare motorcycle specifications via the web UI
- Simple, extendable Flask code structure using blueprints and SQLAlchemy

## Tech stack

- Python >= 3.11
- Flask
- Flask-SQLAlchemy
- pandas

The project lists dependencies in `pyproject.toml`:

- `flask>=3.1.2`
- `flask-sqlalchemy>=3.1.1`
- `pandas>=2.3.3`

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment

```powershell
cd /d D:\RideSmartCompare
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Install dependencies

You can install the minimum required packages directly:

```powershell
pip install "flask>=3.1.2" "flask-sqlalchemy>=3.1.1" "pandas>=2.3.3"
```

(Alternatively, create a `requirements.txt` and install from it.)

3. (Optional) set a session secret for production

```powershell
$env:SESSION_SECRET = "your-secret-here"
```

4. Run the app

```powershell
python backend/app.py
```

The app listens on port 5000 by default. Open http://localhost:5000/ in your browser.

## Data

- `data/motorcycles.csv` — source CSV used by the app's `load_motorcycles_from_csv()` utility.
- The app will create a SQLite database automatically when started (see `backend/models/motorcycle.py` and `backend/app.py`).

Note: The `SQLALCHEMY_DATABASE_URI` in `backend/app.py` currently points to a URL-like string; if you need a local DB file, edit the configuration to a local sqlite path (for example `sqlite:///D:/RideSmartCompare/instance/motorcycles.db`) or add a configuration/environment override.

## Project structure

- `backend/` — Flask app, models, and routes
	- `app.py` — application factory and run entrypoint
	- `models/` — SQLAlchemy models and data loading logic
	- `routes/` — Flask blueprints (compare)
- `templates/` — Jinja2 templates for the web UI
- `static/` — CSS and JS
- `data/` — source CSV data

## Development notes

- The app already creates DB tables and loads CSV data on startup (see `backend/app.py`).
- If you make code changes, restart the server to pick them up. Consider using a development tool like `watchdog` or running with the Flask reloader.

## Running tests

No tests are included by default. Recommended additions:

- Unit tests for `backend/models` duties (data parsing & DB operations)
- Integration tests for routes

## Contributing

1. Fork the repo and create a branch for your feature/bugfix.
2. Open a pull request with a clear description of changes.

## License

Add a license file (e.g., `LICENSE`) and mention the license here.

## Contact

Repository: https://github.com/Abhinav-Praveen004/RideSmart

If you want, I can also:
- Add a `.gitignore` that excludes `__pycache__/`, `.local/`, and virtual envs
- Create a `requirements.txt` from the `pyproject.toml` dependencies
- Update the app to read the DB URI from an environment variable (if you want runtime flexibility)

----

Created automatically to help document and run your project. Update any sections as needed.
