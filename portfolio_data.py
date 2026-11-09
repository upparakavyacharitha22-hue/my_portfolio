"""
portfolio_data.py - Centralized Data Configuration for Portfolio
================================================================
Contains all personal, academic, skill, project, and certification
information for Uppara Kavya Charitha.
You can easily edit and customize details here.
"""

# Profile Information
PROFILE = {
    "name": "Uppara Kavya Charitha",
    "role": "B.Tech Computer Science Engineering Student",
    "headline": "Aspiring AI & Software Developer",
    "institution": "Anantha Lakshmi Institute of Technology and Sciences",
    "academic_period": "2024–2028",
    "cgpa": "9.22",
    "interests": [
        "Python Development",
        "Artificial Intelligence & Machine Learning",
        "Computer Vision & Deep Learning",
        "Software Engineering",
        "Algorithmic Problem Solving",
    ],
    "bio_short": (
        "Passionate B.Tech Computer Science student with a strong foundation in Python, "
        "Artificial Intelligence, and modern software development. Dedicated to building "
        "impactful applications, intelligent systems, and scalable technological solutions."
    ),
    "bio_extended": (
        "Hello! I am Uppara Kavya Charitha, an enthusiastic Computer Science and Engineering "
        "undergraduate at Anantha Lakshmi Institute of Technology and Sciences (2024–2028), "
        "currently maintaining a 9.22 CGPA.\n\n"
        "My passion lies at the intersection of Artificial Intelligence, Computer Vision, "
        "and Python Software Development. I love solving algorithmic challenges, architecting "
        "intelligent web applications, and experimenting with cutting-edge computer vision "
        "models like YOLOv8.\n\n"
        "I thrive in collaborative, learning-focused environments where I can apply my programming "
        "skills to tackle real-world problems. Whether designing AI-powered health platforms "
        "like Nutri AI or optimizing data algorithms, I strive for clean architecture, "
        "robust logic, and continuous self-improvement."
    ),
    "core_values": [
        ("🎯 Continuous Learning", "Always curious and eager to master new technologies, tools, and methodologies."),
        ("🧠 Problem Solving", "Analytical mindset focused on breaking down complex problems into modular solutions."),
        ("⚡ Clean Architecture", "Writing readable, maintainable, and efficient Python code following best practices."),
        ("🤝 Collaboration", "Active team contributor with strong communication skills and passion for innovation."),
    ],
}

# Contact Details (Easily editable placeholders)
CONTACT_INFO = {
    "email": "kavyacharitha.uppara@email.com",
    "linkedin": "https://linkedin.com/in/uppara-kavya-charitha",
    "linkedin_handle": "linkedin.com/in/uppara-kavya-charitha",
    "github": "https://github.com/kavya-charitha",
    "github_handle": "github.com/kavya-charitha",
    "location": "Andhra Pradesh, India",
    "status": "Available for Internships & Projects",
}

# Technical Skills
SKILLS = [
    {
        "name": "Python",
        "category": "Programming Languages",
        "level": "Advanced",
        "percentage": 92,
        "icon": "🐍",
        "highlights": "Core Python, OOP, Streamlit, Data Handling, Scripting & Automation",
    },
    {
        "name": "Java",
        "category": "Programming Languages",
        "level": "Proficient",
        "percentage": 82,
        "icon": "☕",
        "highlights": "Object-Oriented Programming, Classes & Objects, Collections, Logic Building",
    },
    {
        "name": "C Programming",
        "category": "Programming Languages",
        "level": "Proficient",
        "percentage": 85,
        "icon": "⚙️",
        "highlights": "Procedural Programming, Pointers, Memory Concepts, Data Structures Foundation",
    },
    {
        "name": "HTML",
        "category": "Web Technologies",
        "level": "Proficient",
        "percentage": 88,
        "icon": "🌐",
        "highlights": "Semantic Markup, Document Structuring, Modern Web Elements, Accessibility",
    },
    {
        "name": "CSS",
        "category": "Web Technologies",
        "level": "Proficient",
        "percentage": 80,
        "icon": "🎨",
        "highlights": "Responsive Design, Flexbox, Grid, Layout Principles, Visual Hierarchy",
    },
    {
        "name": "JavaScript",
        "category": "Web Technologies",
        "level": "Intermediate",
        "percentage": 75,
        "icon": "⚡",
        "highlights": "ES6+ Fundamentals, DOM Concepts, Event-Driven Programming, Interactivity",
    },
    {
        "name": "Artificial Intelligence",
        "category": "AI & Machine Learning",
        "level": "Proficient",
        "percentage": 85,
        "icon": "🧠",
        "highlights": "Machine Learning Fundamentals, Neural Networks, Computer Vision, YOLOv8",
    },
    {
        "name": "Problem Solving",
        "category": "Core Competencies",
        "level": "Advanced",
        "percentage": 90,
        "icon": "🧩",
        "highlights": "Algorithmic Thinking, Data Structures, Complexity Analysis, Debugging",
    },
]

# Projects
PROJECTS = [
    {
        "title": "Nutri AI",
        "subtitle": "AI-Based Nutrition Management Web Application",
        "badge": "Featured Project",
        "icon": "🥗",
        "category": "Artificial Intelligence & Web App",
        "description": (
            "Nutri AI is an intelligent health and nutrition management web platform designed to "
            "empower users with personalized dietary guidance, automated calorie calculations, and "
            "AI-driven meal recommendations tailored to specific fitness and wellness goals."
        ),
        "key_features": [
            "Smart Caloric & Macronutrient Estimator (Proteins, Carbs, Fats calculation)",
            "AI-Powered Personalized Meal Recommendation Engine based on dietary preferences",
            "Interactive daily nutrition tracker and goal progress visualization",
            "Clean and responsive user experience built natively with Python & Streamlit",
        ],
        "tech_stack": ["Python", "Streamlit", "Machine Learning", "Data Analytics", "Pandas"],
        "status": "Completed / Interactive Prototype",
        "github_url": "https://github.com/kavya-charitha/nutri-ai",
        "demo_url": "https://nutri-ai-demo.streamlit.app",
    },
    {
        "title": "Computer Vision / YOLOv8 Object Detection",
        "subtitle": "Real-Time Object Detection & Tracking System",
        "badge": "Computer Vision",
        "icon": "👁️",
        "category": "Deep Learning & Computer Vision",
        "description": (
            "An advanced real-time computer vision system leveraging the state-of-the-art YOLOv8 deep learning "
            "architecture to accurately detect, classify, and track multiple objects across dynamic video streams "
            "and high-resolution image inputs."
        ),
        "key_features": [
            "Multi-class real-time detection with high bounding-box precision and low latency",
            "Interactive confidence threshold and Non-Maximum Suppression (NMS) sliders",
            "Support for live camera feed processing, recorded videos, and batch image uploads",
            "Statistical detection summary with target counts and class frequency analysis",
        ],
        "tech_stack": ["Python", "YOLOv8 (Ultralytics)", "OpenCV", "PyTorch", "Streamlit"],
        "status": "Active R&D",
        "github_url": "https://github.com/kavya-charitha/yolov8-object-detection",
        "demo_url": "https://yolov8-detection-demo.streamlit.app",
    },
    {
        "title": "Python Projects & Automation Suite",
        "subtitle": "Smart Utility & Data Processing Applications",
        "badge": "Core Python",
        "icon": "🛠️",
        "category": "Software Utilities & Data Tools",
        "description": (
            "A collection of production-ready Python applications and automation scripts created to streamline "
            "file management, analyze tabular datasets, and automate repetitive computational tasks with high efficiency."
        ),
        "key_features": [
            "Automated directory and file organizer based on file types, extensions, and metadata",
            "Interactive data exploration tool for rapid CSV cleaning and descriptive statistics",
            "Cryptographically secure password generator and hash verification utility",
            "Built following clean code principles, modular structure, and PEP-8 conventions",
        ],
        "tech_stack": ["Python 3", "Streamlit", "Pandas", "OS/Sys Modules", "Data Analysis"],
        "status": "Completed / Available on GitHub",
        "github_url": "https://github.com/kavya-charitha/python-projects-suite",
        "demo_url": "https://python-suite-demo.streamlit.app",
    },
]

# Certifications
CERTIFICATIONS = [
    {
        "title": "Artificial Intelligence Internship",
        "issuer": "CodeAlpha",
        "badge": "AI & ML Specialization",
        "icon": "🤖",
        "period": "Virtual Internship Program",
        "description": (
            "Successfully completed an intensive internship focused on Artificial Intelligence and Machine Learning. "
            "Developed practical AI solutions, trained predictive models, and implemented industry-standard machine learning pipelines."
        ),
        "skills_acquired": [
            "Supervised & Unsupervised Machine Learning",
            "Model Training, Tuning & Evaluation",
            "Python AI Libraries & Data Preprocessing",
            "Hands-on Project Development",
        ],
        "status": "Verified / Completed",
    },
    {
        "title": "Full Stack Python Virtual Internship",
        "issuer": "EduSkills (in collaboration with AICTE)",
        "badge": "Full Stack Development",
        "icon": "💻",
        "period": "Virtual Internship Program",
        "description": (
            "Completed comprehensive training in Full Stack Python Development supported by AICTE and EduSkills. "
            "Mastered Python programming, database integration, server architectures, and backend application development workflows."
        ),
        "skills_acquired": [
            "Core & Advanced Python Programming",
            "Database Design & Integration",
            "Web Architecture & API Fundamentals",
            "Full-Stack Development Lifecycle",
        ],
        "status": "Verified / Completed",
    },
]

# Education Timeline
EDUCATION_TIMELINE = [
    {
        "degree": "Bachelor of Technology (B.Tech) - Computer Science & Engineering",
        "institution": "Anantha Lakshmi Institute of Technology and Sciences",
        "period": "2024–2028",
        "score": "CGPA: 9.22",
        "status": "Currently Pursuing",
        "icon": "🎓",
        "highlights": [
            "Maintaining an outstanding academic record with 9.22 CGPA",
            "Core focus: Data Structures & Algorithms, Python Programming, Object-Oriented Design",
            "Active participant in technical symposiums, coding hackathons, and AI research projects",
            "Collaborating on departmental projects focusing on AI applications and software systems",
        ],
    },
    {
        "degree": "Intermediate Education (Class XI & XII - MPC)",
        "institution": "Board of Intermediate Education, Andhra Pradesh",
        "period": "2022–2024",
        "score": "First Class with Distinction",
        "status": "Successfully Completed",
        "icon": "📚",
        "highlights": [
            "Majored in Mathematics, Physics, and Chemistry (MPC stream)",
            "Developed strong analytical, problem-solving, and logical reasoning fundamentals",
            "Consistently ranked among top academic performers in college examinations",
        ],
    },
    {
        "degree": "Secondary School Certificate (SSC / Class X)",
        "institution": "State Board of Secondary Education, Andhra Pradesh",
        "period": "Completed 2022",
        "score": "First Class with Distinction",
        "status": "Successfully Completed",
        "icon": "🏫",
        "highlights": [
            "Built a solid foundation in mathematics, physical sciences, and computer basics",
            "Active participant in academic competitions, school science fairs, and seminars",
        ],
    },
]

# Quick Resume Text Representation (for download button)
RESUME_TEXT = f"""===================================================================
UPPARA KAVYA CHARITHA - CURRICULUM VITAE
B.Tech Computer Science Engineering Student | Aspiring AI & Software Developer
===================================================================

CONTACT INFORMATION:
- Email: {CONTACT_INFO['email']}
- LinkedIn: {CONTACT_INFO['linkedin']}
- GitHub: {CONTACT_INFO['github']}
- Location: {CONTACT_INFO['location']}

PROFESSIONAL SUMMARY:
{PROFILE['bio_short']}

ACADEMIC BACKGROUND:
1. Bachelor of Technology (B.Tech) - Computer Science and Engineering
   - Institution: {PROFILE['institution']}
   - Academic Period: {PROFILE['academic_period']}
   - Academic Performance: CGPA {PROFILE['cgpa']}

2. Intermediate Education (MPC)
   - Board of Intermediate Education (2022 - 2024)
   - Status: First Class with Distinction

3. Secondary School Certificate (SSC)
   - State Board of Secondary Education (Completed 2022)
   - Status: First Class with Distinction

TECHNICAL SKILLS:
- Programming Languages: Python, Java, C Programming
- Web Technologies: HTML, CSS, JavaScript
- AI & Data Science: Artificial Intelligence, Machine Learning, Computer Vision, YOLOv8
- Core Competencies: Problem Solving, Algorithmic Thinking, Data Structures

KEY PROJECTS:
1. Nutri AI - AI-Based Nutrition Management Web Application
   - Technologies: Python, Streamlit, Machine Learning, Data Analytics
   - Description: AI-powered dietary planning, caloric intake analysis, and macronutrient tracking.

2. Computer Vision / YOLOv8 Object Detection
   - Technologies: Python, YOLOv8 (Ultralytics), OpenCV, PyTorch, Streamlit
   - Description: Real-time object recognition and boundary box tracking system.

3. Python Projects & Automation Suite
   - Technologies: Python, Pandas, OS/Sys Modules, Streamlit
   - Description: Suite of utilities for file management, CSV analysis, and system automation.

CERTIFICATIONS & INTERNSHIPS:
1. CodeAlpha - Artificial Intelligence Internship
   - Focused on Machine Learning, predictive models, and practical AI implementations.
2. EduSkills (AICTE) - Full Stack Python Virtual Internship
   - Focused on end-to-end Python programming, database integration, and software engineering.

===================================================================
Generated via Streamlit Portfolio
===================================================================
"""

