# FastAPI Interview Boilerplate

## 🚀 Setup Project

```bash
cd fastapi-interview

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
# Create requirements file
touch requirements.txt
```

Add the following inside `requirements.txt`:

```
fastapi[standard]
pytest
```

Now install:

```bash
pip install -r requirements.txt
```

---

## 📝 Create App File

```bash
touch main.py
```

---

## ▶️ Run Server

```bash
fastapi dev lru_cache_main.py
```

> Alternatively (more common in interviews):

```bash
uvicorn main:app --reload
```

---

## 🧪 Run Test Cases

```bash
pytest test_cache.py
```

To run a specific test file:

```bash
pytest test_rate_limiter.py -v
```

---

## 📌 Notes

* Make sure your FastAPI app instance is named `app`
* Keep endpoint paths consistent (e.g., `/rate-limit` vs `/rate_limit`)
* Always validate inputs using Pydantic models
* Use `TestClient` from `fastapi.testclient` for testing

---

## 🧠 Interview Tip

You can explain this setup as:

> "I quickly bootstrap a FastAPI project with a virtual environment, dependency file, and basic endpoints, then validate functionality using pytest and FastAPI’s TestClient."

---

