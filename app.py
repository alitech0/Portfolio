from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

# ---------- EDIT YOUR DETAILS HERE ----------
PROFILE = {
    "name": "Ali",
    "full_name": "Sheikh Ali Aslam",
    "role": "AI Engineer",
    "roles": ["AI Engineer", "Python Developer", "Flutter Developer", "Data Explorer"],
    "tagline": "AI engineer intern at NETSOL Technologies in Lahore. I build machine learning systems and APIs, from data to deployment.",
    "location": "Lahore, Pakistan",
    "email": "aliaslam20041@gmail.com",
    "github": "",  # paste your GitHub profile link here; it stays hidden while empty
    "linkedin": "https://www.linkedin.com/in/sheikhaliaslam/",
    "instagram": "https://www.instagram.com/sheikh_ali893/",
    "whatsapp": "923099818457",          # country code + number, no + or spaces
    # "whatsapp_display": "+92 309 9818457",
    "formspree_id": "xkjjbwer",
}

SKILLS = {
    "AI & ML": ["OpenAI", "Scikit-learn", "MLflow"],
    "Data": ["Pandas", "NumPy", "SQL", "Plotly", "Seaborn", "Matplotlib"],
    "Backend & APIs": ["Python", "Flask", "FastAPI", "Postman", "Swagger", "Docker"],
    "Languages & Web": ["C++", "C", "HTML", "CSS", "JavaScript"],
}

PROJECTS = [
    {
        "title": "Titanic survival: Naive Bayes pipeline",
        "summary": "An end-to-end machine learning pipeline, from raw data to an evaluated Naive Bayes model.",
        "details": "EDA and missing-value analysis, encoding, scaling and power transforms, then GaussianNB evaluated with a confusion matrix, classification report and cross-validation.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=70",
        "stack": ["Pandas", "Seaborn", "Scikit-learn"],
    },
    {
        "title": "SMS spam filter from scratch",
        "summary": "A Multinomial Naive Bayes classifier written as a Python class and trained on about 5,570 real text messages.",
        "details": "Add-1 (Laplace) smoothing, a log-probability version to avoid numeric underflow, and a check against scikit-learn's MultinomialNB on imbalanced data.",
        "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=70",
        "stack": ["Python", "NumPy", "Scikit-learn"],
    },
    {
        "title": "California house price prediction",
        "summary": "Multivariate linear regression implemented from scratch on the California housing dataset.",
        "details": "Batch and mini-batch gradient descent compared with the normal equation, feature scaling, and test RMSE checked against scikit-learn.",
        "image": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=800&q=70",
        "stack": ["NumPy", "Matplotlib", "Scikit-learn"],
    },
    {
        "title": "FIFA 19: what makes a top player?",
        "summary": "Statistical analysis of 18,000+ professional footballers, finished with a scouting brief.",
        "details": "Distributions, normality checks, t-tests and ANOVA with Tukey post-hoc, correlation heatmaps and chi-square tests on categorical features.",
        "image": "https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?auto=format&fit=crop&w=800&q=70",
        "stack": ["Pandas", "SciPy", "Seaborn"],
    },
]

EXPERIENCE = [
    {
        "when": "Sep 2026 - Present",
        "title": "Artificial Intelligence Engineer",
        "org": "NETSOL Technologies Inc. · Internship",
        "place": "Lahore, Punjab, Pakistan · On-site",
        "skills": ["Python", "FastAPI", "OpenAI", "Docker", "MLflow"],
    },
    {
        "when": "Jan 2026 - Mar 2026",
        "title": "Flutter Developer",
        "org": "Techuick · Full-time",
        "place": "Lahore, Punjab, Pakistan · On-site",
        "skills": ["Flutter", "Dart"],
    },
]

EDUCATION = [
    {
        "when": "Dec 2023 - Nov 2027",
        "title": "Bachelor's Degree, Computer Science",
        "org": "Virtual University of Pakistan (VU)",
        "grade": "Grade: 3.67",
        "skills": ["Python", "C++", "C", "SQL", "Pandas", "NumPy", "Scikit-learn",
                   "Matplotlib", "Seaborn", "Plotly"],
    },
    {
        "when": "Nov 2021 - Jul 2023",
        "title": "Bachelor's Degree, Computer Science",
        "org": "Punjab Group Of Colleges",
        "grade": "",
        "skills": [],
    },
]
# Skill logos (Devicon / Simple Icons CDN). Add a skill name + logo URL here to give it an icon.
ICONS = {
    "Python": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
    "C++": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg",
    "C": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg",
    "HTML": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg",
    "CSS": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg",
    "JavaScript": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg",
    "Flask": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg",
    "FastAPI": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg",
    "Docker": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg",
    "Postman": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postman/postman-original.svg",
    "Swagger": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/swagger/swagger-original.svg",
    "Pandas": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg",
    "NumPy": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg",
    "Scikit-learn": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg",
    "Matplotlib": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg",
    "Plotly": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/plotly/plotly-original.svg",
    "SQL": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg",
    "Seaborn": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/seaborn/seaborn-original.svg",
    "Flutter": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flutter/flutter-original.svg",
    "Dart": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/dart/dart-original.svg",
    "OpenAI": "https://cdn.simpleicons.org/openai/412991",
    "MLflow": "https://cdn.simpleicons.org/mlflow/0194E2",
    "SciPy": "https://cdn.simpleicons.org/scipy/8CAAE6",
}

# ---------------------------------------------


@app.context_processor
def common_data():
    return {
        "profile": PROFILE,
        "name": PROFILE["name"],
        "year": datetime.now().year,
        "skills": SKILLS,
        "projects": PROJECTS,
        "experience_items": EXPERIENCE,
        "education_items": EDUCATION,
        "icons": ICONS,
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects_page():
    return render_template("projects.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/contactme")
def contactme():
    return render_template("contactme.html")


if __name__ == "__main__":
    app.run(debug=True)
