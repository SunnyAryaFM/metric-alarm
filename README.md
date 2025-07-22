---

## 🚀 Project Setup & Execution Guide

Follow the steps below to set up your Python environment and run the project successfully.

---

### 📁 1. Create a Virtual Environment

Creating a virtual environment ensures project dependencies are isolated from your global Python environment.

#### For Unix/macOS:

```bash
python3 -m venv .venv
```

#### For Windows:

```bash
python -m venv .venv
```

---

### ✅ 2. Activate the Virtual Environment

#### On Unix/macOS:

```bash
source .venv/bin/activate
```

#### On Windows:

```bash
.venv\Scripts\activate
```

> 🔍 **Note:** After activation, your terminal prompt should be prefixed with `(.venv)` indicating the virtual environment is active.

---

### 📦 3. Install Project Dependencies

Use `pip` to install the required libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

### 🏃‍♂️ 4. Run the Project

Once dependencies are installed, you can start the project using:

```bash
python monitor.py
```

---

### 🧹 Deactivating the Virtual Environment

When you're done, deactivate the environment using:

```bash
deactivate
```

---

### 🛠 Troubleshooting Tips

* Ensure you’re using the correct version of Python (`python --version` or `python3 --version`).
* If `pip` isn't recognized, try using `python -m pip install -r requirements.txt`.
* On Unix systems, ensure the `monitor.py` file has executable permissions (`chmod +x monitor.py` if needed).

---
