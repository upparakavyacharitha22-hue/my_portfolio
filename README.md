# 🚀 Personal Portfolio Website — Uppara Kavya Charitha

An attractive, modern, and fully responsive **Personal Portfolio Website** built **exclusively using Python and Streamlit**.

> **Zero Frontend Code**: Built **without** HTML, CSS, JavaScript, Bootstrap, or any frontend templates. All layouts, cards, buttons, themes, and interactive components are generated using native Python and Streamlit widgets.

---

## 🌟 Key Highlights & Features

- **💜 Dark & Purple Aesthetic**: Configured with a deep dark-violet and rich purple accent theme via `.streamlit/config.toml`.
- **📱 Fully Responsive**: Automatically adjusts layouts for desktop, tablet, and mobile browsers.
- **🧭 Smooth Sidebar & In-Page Navigation**: Switch smoothly between sections with sidebar controls or interactive call-to-action buttons.
- **📊 Native Metric & Skill Cards**: Clean, Python-generated cards (`st.container(border=True)`) displaying CGPA, proficiencies, and metrics.
- **🧪 Interactive Live Project Simulators**:
  - **Nutri AI Simulator**: Calculate daily caloric requirements and personalized macronutrient breakdown.
  - **YOLOv8 Object Detection Simulator**: Experiment with confidence thresholds, IoU, and simulated object tracking results.
  - **Python Data Analyzer Tool**: Input comma-separated numbers and receive instantaneous statistical summaries.
- **📄 Instant Resume Download**: Download a formatted text CV with one click.
- **📬 Interactive Contact Form**: Full name, email, subject, and message fields with validation and instant feedback.
- **🧩 100% Modular & Beginner-Friendly**: All personal details are stored in a centralized `portfolio_data.py` file, making customization effortless.

---

## 📂 Project Directory Structure

```text
my protfolio/
│
├── .streamlit/
│   └── config.toml             # Dark & purple theme settings (pure Streamlit configuration)
│
├── sections/
│   ├── __init__.py             # Exports all modular section renderers
│   ├── home_section.py         # Welcome banner, headline, key metrics, quick links
│   ├── about_section.py        # Academic background, bio, core engineering values
│   ├── skills_section.py       # 8 technical skill cards with progress indicators & tabs
│   ├── projects_section.py     # Nutri AI, YOLOv8 & Python suite + interactive simulators
│   ├── certifications_section.py # CodeAlpha & EduSkills verified credential cards
│   ├── education_section.py    # Chronological academic timeline with CGPA & highlights
│   └── contact_section.py      # Social links, editable placeholders & contact form
│
├── app.py                      # Main entrypoint, page routing & sidebar navigation
├── portfolio_data.py           # Centralized personal info, skills, projects & contacts
├── requirements.txt            # Project dependencies (streamlit, pandas)
└── README.md                   # Complete documentation and deployment guide
```

---

## 🛠️ Prerequisites

Before running the project, make sure you have:
1. **Python 3.9 or higher** installed on your system.
   - If not installed, download from [python.org](https://www.python.org/downloads/) (make sure to check the box: *"Add python.exe to PATH"* during installation).
2. **Visual Studio Code (VS Code)** installed.

---

## 💻 How to Run the Project in VS Code (Step-by-Step)

Follow these easy steps to get your portfolio running on your local machine:

### Step 1: Open the Project in VS Code
1. Open **VS Code**.
2. Click **File** > **Open Folder...** (or press `Ctrl + K Ctrl + O`).
3. Select your portfolio folder:
   ```text
   c:\Users\Kavya\OneDrive\Desktop\my protfolio
   ```

### Step 2: Open the Integrated Terminal
- Press `` Ctrl + ` `` (Backtick) or go to the top menu: **Terminal** > **New Terminal**.
- Ensure PowerShell or Command Prompt opens in the terminal pane at the bottom.

### Step 3: (Recommended) Create and Activate a Virtual Environment
Creating a virtual environment keeps your packages clean and isolated:

```powershell
# Create virtual environment named 'venv'
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

> **Note for Windows PowerShell**: If you see an execution policy warning when activating, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> .\venv\Scripts\Activate.ps1
> ```

### Step 4: Install Dependencies
Run the following command to install Streamlit and Pandas:

```powershell
pip install -r requirements.txt
```

### Step 5: Launch the Streamlit App
Run your portfolio website with:

```powershell
streamlit run app.py
```

### Step 6: View in Your Browser
Streamlit will automatically open your default browser. If it doesn't open automatically, hold `Ctrl` and click the local URL in your terminal:
```text
http://localhost:8501
```

To stop the running application at any time, go to the terminal and press `Ctrl + C`.

---

## ✏️ How to Customize Your Personal Details

All your personal information is stored cleanly in **`portfolio_data.py`**! You do **not** need to touch any UI code to update your details:

| Information | Location in `portfolio_data.py` | Description |
| :--- | :--- | :--- |
| **Name & Headline** | `PROFILE["name"]`, `PROFILE["headline"]` | Update name, role, bio |
| **College & CGPA** | `PROFILE["institution"]`, `PROFILE["cgpa"]` | Update college name or CGPA |
| **Contact Links** | `CONTACT_INFO["email"]`, `CONTACT_INFO["linkedin"]`, `CONTACT_INFO["github"]` | Add your real email, LinkedIn URL & GitHub URL |
| **Skills** | `SKILLS` list | Add new skills, adjust percentages or icons |
| **Projects** | `PROJECTS` list | Add descriptions, GitHub repo links, live demo links |
| **Certifications** | `CERTIFICATIONS` list | Add credentials, dates, or issuing bodies |
| **Education** | `EDUCATION_TIMELINE` list | Update dates, school names, and marks |

Any time you save `portfolio_data.py`, Streamlit detects the change and prompts you to **"Rerun"** or **"Always rerun"** in the top-right corner to see updates instantly!

---

## ☁️ How to Deploy on Streamlit Community Cloud (Free & Live Online)

Streamlit Community Cloud lets you host your portfolio online for **100% free** with a custom URL you can share on your resume, LinkedIn, and GitHub profile.

### Step 1: Push Your Code to GitHub
1. Create a free account on [GitHub.com](https://github.com) if you haven't already.
2. Create a new repository (e.g., `kavya-portfolio` or `my-portfolio`) and set it to **Public**.
3. In your VS Code terminal, run:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit of Streamlit portfolio"
   git branch -M main
   git remote add origin https://github.com/<your-username>/kavya-portfolio.git
   git push -u origin main
   ```
   *(Alternatively, you can use GitHub Desktop to publish the folder with a single click).*

### Step 2: Sign In to Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/).
2. Click **"Continue with GitHub"** to log in using your GitHub account.

### Step 3: Deploy the App
1. Click the blue **"Create app"** or **"New app"** button.
2. Select your repository: `<your-username>/kavya-portfolio`.
3. Set **Branch**: `main`.
4. Set **Main file path**: `app.py`.
5. (Optional) Customize your App URL (e.g., `kavya-charitha.streamlit.app`).
6. Click **"Deploy!"**.

### Step 4: Share Your Live Portfolio!
Within 1–2 minutes, your website will be live worldwide. You will receive a permanent HTTPS link (e.g. `https://kavya-charitha.streamlit.app`) that you can add to your LinkedIn bio, email signature, and job applications!

---

## ❓ Frequently Asked Questions & Troubleshooting

### 1. `streamlit : The term 'streamlit' is not recognized`
Ensure your virtual environment is activated (`.\venv\Scripts\Activate.ps1`) or run using Python module syntax:
```powershell
python -m streamlit run app.py
```

### 2. How do I change the theme colors?
The dark and purple gradient theme is defined in `.streamlit/config.toml`:
- `primaryColor`: Accent purple (`#A855F7`)
- `backgroundColor`: Deep dark-violet canvas (`#0D0B14`)
- `secondaryBackgroundColor`: Card & sidebar container color (`#1A1528`)
- `textColor`: Bright clean text (`#F3F4F6`)

You can modify these hexadecimal codes at any time to customize your color scheme!

---

## 📄 License & Credits
- Designed & Developed by **Uppara Kavya Charitha**
- Built with **Python 3** & **Streamlit**

