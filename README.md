
# Chrome Homeland FastAPI Backend & Web Application

Chrome Homeland is a property listing and aggregation platform built for searching, buying, and renting land and housing across Kenya.

## Features
- **Authentication & Security:** Role-based signup (`landlord`, `seeker`), JWT access tokens, bcrypt password hashing, CORS security, and production console-log stripping.

- **Property Management:** Protected endpoints for landlord property listings with automatic ORM owner eager-loading (`joinedload`).

- **Search & Filtering:** Real-time search by county, town, property type (`rent`/`sale`), purpose, and availability.

- **Direct Owner Engagement:** Clean, isolated WhatsApp and direct-dial modal triggers populated with owner contact details.

- **Legal & Compliance:** Complete Kenyan statutory compliance (Data Protection Act 2019, Cybercrimes Act 2018) with built-in ReportLab PDF term generator scripts.

- **Interactive API Documentation:** Full OpenAPI / Swagger documentation out of the box.


---

## Tech Stack
- **Backend:** FastAPI, Python 3.10+, SQLAlchemy ORM, Pydantic v2

- **Database:** SQLite (Development) / PostgreSQL (Production)

- **PDF Generation:** ReportLab

- **Frontend:** Vanilla JS (ES6+), Modern HTML5 & CSS3

- **Deployment:** Vercel / Railway / Render


---

## Getting Started

### 1. Environment Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/Njorodev/Chrome-Homeland.git
cd Chrome-Homeland

# Create virtual environment
python -m venv venv

```

**Activate Virtual Environment:**

* **Windows (PowerShell/CMD):**

```powershell
.\venv\Scripts\activate

```

* **Linux/macOS:**

```bash
source venv/bin/activate

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Environment Variables

Set your environment variables before running the application:

```powershell
# Windows PowerShell
$env:SECRET_KEY="your-long-random-secret-key"

```

```bash
# Linux/macOS
export SECRET_KEY="your-long-random-secret-key"

```

### 4. Database Migrations & Initial Setup

Start the server to auto-generate SQLite tables via SQLAlchemy:

```bash
uvicorn app.main:app --reload

```

---

## API Documentation

Once running, access the interactive API docs at:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Frontend Integration & Setup

### HTML & Scripts

Ensure your scripts use the `defer` attribute inside the `<head>` or are placed at the bottom of `<body>` to prevent DOM binding issues:

```html
<script src="frontend-auth.js" defer></script>
<script src="frontend-script.js" defer></script>

```

### Form Attribute Specifications

**Signup Forms:**

```html
<form class="auth-form" data-mode="signup" data-role="landlord">
<!-- or data-role="seeker" -->

```

*Expected fields:* `first_name`, `last_name`, `email`, `phone`, `password`, `confirm_password`

**Login Forms:**

```html
<form class="auth-form" data-mode="login">

```

*Expected fields:* `email`, `password`

**Property Posting Form:**

```html
<form id="property-form">

```

*Expected fields:* `title`, `property_type`, `purpose`, `county`, `town`, `price`, `total_units`, `available_units`, `description`, `image_url`

---

## Deployment (Vercel)

### 1. Git Configuration

Before pushing changes, ensure your Git identity is configured:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

```

### 2. Vercel CLI Deployment

```bash
npm install -g vercel
vercel

```

For automatic builds on push, connect your GitHub repository directly in the [Vercel Dashboard](https://vercel.com).

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

```
