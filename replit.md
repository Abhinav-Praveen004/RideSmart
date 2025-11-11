# RideSmart - Motorcycle Comparison Platform

## Overview

RideSmart is a web-based motorcycle comparison platform that allows users to search for motorcycles and compare their specifications side-by-side. The application provides an intuitive interface for selecting two motorcycles and viewing detailed technical comparisons including engine specs, dimensions, braking systems, suspension, and other key features. The platform loads motorcycle data from a CSV file and stores it in a local database for efficient querying and retrieval.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates served by Flask for server-side rendering
- **UI Components**: Vanilla JavaScript with async/await for API interactions
- **Search Functionality**: Real-time search with debouncing, displaying results in dropdown overlays
- **Comparison View**: Dynamic table generation comparing two selected motorcycles side-by-side
- **Styling**: Custom CSS with gradient backgrounds and card-based layouts for modern UI/UX

### Backend Architecture
- **Web Framework**: Flask (Python) for routing and request handling
- **Application Factory Pattern**: `create_app()` function centralizes app configuration and initialization
- **Blueprint Structure**: Modular route organization using Flask Blueprints (compare_bp for comparison features)
- **API Design**: RESTful JSON endpoints for motorcycle search and retrieval
  - `/api/search` - Search motorcycles by brand or model with query parameters
  - `/api/motorcycle/<id>` - Retrieve detailed motorcycle specifications by ID

### Data Storage
- **Database**: SQLite for local data persistence
- **ORM**: Flask-SQLAlchemy for database operations and model definitions
- **Schema Design**: Single `motorcycles` table with 30+ columns covering comprehensive motorcycle specifications
- **Data Loading Strategy**: CSV import on first run with duplicate prevention check
- **Data Sanitization**: Helper functions (`safe_float`, `safe_int`) handle missing values and type conversions from CSV data

### Key Architectural Decisions

**Problem**: Need to handle incomplete or malformed data from CSV source
**Solution**: Implemented safe type conversion functions that gracefully handle null values, string formatting (comma removal), and type errors
**Rationale**: Prevents application crashes and ensures data integrity during import

**Problem**: Efficient text-based search across motorcycle brands and models
**Solution**: SQLAlchemy's `ilike` operator with OR conditions for case-insensitive partial matching
**Rationale**: Provides user-friendly search experience without requiring exact matches

**Problem**: Session management and security
**Solution**: Flask session secret key with environment variable fallback
**Rationale**: Allows secure production deployment while maintaining development ease

**Problem**: Frontend-backend communication for dynamic search
**Solution**: Async/await JavaScript pattern calling JSON API endpoints
**Rationale**: Non-blocking UI updates and clean separation between frontend and backend logic

## External Dependencies

### Python Packages
- **Flask**: Web application framework
- **Flask-SQLAlchemy**: ORM and database abstraction layer
- **Pandas**: CSV data processing and manipulation during initial data load
- **SQLAlchemy**: Core database toolkit (via Flask-SQLAlchemy)

### Data Sources
- **CSV File**: `data/motorcycles.csv` containing motorcycle specifications
  - Columns include: Brand, Model, Year, Category, Rating, Displacement, Power, Torque, Engine details, Fuel system, Weight, Dimensions, Brakes, Tires, Suspension, Colors

### Database
- **SQLite**: File-based relational database (`motorcycles.db`)
  - No external database server required
  - Database file created automatically on first run

### Frontend Libraries
- **Vanilla JavaScript**: No external JS frameworks or libraries
- **Custom CSS**: No CSS frameworks (Bootstrap, Tailwind, etc.)

### Deployment Considerations
- Application runs on host `0.0.0.0` port `5000` for container/cloud compatibility
- Static files and templates use relative paths for portability
- Environment variable support for `SESSION_SECRET` configuration