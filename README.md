# 🎯 Tech Stack Recommender — AI Recommendation Engine

An AI-driven content-based recommendation system that matches a user's technical and creative skillset to the most relevant job roles using **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity**.

Developed as part of **DecodeLabs — Artificial Intelligence Track (Project 03: Personalization & AI Recommendation Logic)**.

---

## 📌 Project Overview

In the modern job market, candidates often face "choice overload" when navigating various career paths. This project bridges raw user profiles and relevant career tracks by replacing naive keyword matching with **vector space angular alignment**.

The repository includes two implementations:
1. **Python CLI Engine:** Uses `pandas` and `scikit-learn` for data handling and vector calculations.
2. **Interactive Web UI:** A standalone, dependency-free HTML/CSS/JavaScript dashboard featuring custom in-browser TF-IDF and cosine similarity algorithms.

---

## ⚙️ How It Works (The 4-Step Pipeline)

The recommendation engine strictly follows the **Input–Process–Output (IPO)** architecture:

```
[ Ingest Skills ] ➔ [ Vectorize & Score (TF-IDF + Cosine) ] ➔ [ Sort (Descending) ] ➔ [ Filter (Top-N) ]
```

1. **Ingestion (Input):** Accepts at least 3 user-selected skills to ensure adequate feature density and bypass the cold-start problem.
2. **Scoring (Process):**
   * **TF-IDF Weighting:** Reduces the mathematical weight of generic, frequent words while emphasizing specialized technical terms.
   * **Cosine Similarity:** Measures the angular orientation between the user's vector and each job role's vector, making it independent of description length.
3. **Sorting:** Ranks all cataloged roles by their calculated match score in descending order.
4. **Filtering (Output):** Truncates the ranked list to return only the **Top 3** most relevant career paths.

---

## 🛠️ Tech Stack & Dependencies

### Python CLI
- **Language:** Python 3.8+
- **Libraries:**
  - `pandas` (Dataset handling)
  - `scikit-learn` (`TfidfVectorizer`, `cosine_similarity`)

### Web Dashboard
- **Frontend:** Pure HTML5, CSS3, and Vanilla JavaScript
- **Typography:** IBM Plex Sans, IBM Plex Mono, Fraunces
- **No external JS libraries or build tools required.**

---

## 📁 Repository Structure

```text
├── index.html                 # Interactive Web UI implementation
├── tech_stack_recommender.py  # Python CLI recommendation script
├── raw skills.csv             # Job roles and required skills dataset
└── README.md                  # Documentation
```

---

## 📊 Dataset Format (`raw skills.csv`)

Programming Languages & Core Tech
Python, SQL, R, Java, C, C++, C#, JavaScript, PHP, Ruby, Go, Rust, Kotlin, Swift, Dart, Scala, MATLAB, Solidity, Apex, ABAP

Frameworks & Libraries
TensorFlow, PyTorch, Pandas, NumPy, Django, Flask, Laravel, Rails, Spring Boot, React, React Native, Node.js, .NET, Xamarin, Flutter, Selenium

Data Science / AI / ML
Machine Learning, Deep Learning, Statistics, Data Visualization, Jupyter, Data Pipelines, MLOps, Research, Research Papers, Mathematics, Linear Algebra, Publications, NLP, Transformers, Text Processing, Linguistics, OpenCV, Image Processing, CNN, Computer Vision, Data Analysis, Probability, Experimental Design, Hypothesis Testing, Bioinformatics Tools, Genomics, Biology, Data Cleaning, Research Methods, Research Methodology, Model Deployment, Analytics

Data Engineering
ETL, Data Pipelines, Cloud Computing, Data Warehousing, DAX, Data Modeling, Databases, Hadoop, Spark, Kafka, Airflow, dbt, Database Design, Indexing, Backup Recovery, Performance Tuning, Oracle, PostgreSQL, SQL Server, Storage Systems, SAN, NAS

Web & Backend Development
HTML, CSS, APIs, REST, GraphQL, System Design, Design Patterns, Scalability, Microservices, API Design, Authentication, Middleware, System Integration, MVC Architecture, Concurrency, Systems Programming, Memory Safety, Performance Optimization, Object Oriented Programming, Data Structures, Algorithms, Testing, Version Control, WordPress, Plugin Development, MySQL, Shopify, Liquid, E-commerce, API Integration, Magento, Odoo, ERP Customization, ERP Systems, ERP, Xcode, Cross Platform Development

Cloud, DevOps & Infrastructure
AWS, Azure, Networking, Security, Automation, Terraform, Cost Optimization, Docker, Kubernetes, CI/CD, Linux, Jenkins, Monitoring, Incident Response, Incident Management, SRE Practices, Infrastructure as Code, Scripting, Bash, Server Management, Windows Server, Active Directory, PowerShell, VMware, Hyper-V, Virtualization, Hypervisors, Storage, Build Systems, Deployment, RPA, UiPath, Automation Anywhere, Workflow Design, Process Automation, Process Analysis, Configuration Management, Change Management

Cybersecurity
Network Security, Penetration Testing, Firewalls, Risk Assessment, Cryptography, Cloud Security, SIEM, Threat Detection, Log Analysis, IAM, Encryption, SSO, Authentication Protocols, Cisco, Routing, Switching, Ethical Hacking, Vulnerability Assessment, Kali Linux, Forensics, Evidence Analysis, Threat Analysis, Security Research, Reverse Engineering, Malware Analysis, Assembly, Secure Coding, Code Review, Compliance, Auditing, IT Governance, Strategic Planning

Mobile, Embedded & Hardware
Mobile UI, Android, iOS, Firebase, Microcontrollers, RTOS, Firmware, Embedded Systems, Hardware Debugging, Hardware Interfaces, Circuit Design, PCB Design, Schematics, ROS, Control Systems, Sensors, Mechanical Design, Robotics, IoT, MQTT

Testing/QA
Test Automation, Test Planning, Manual Testing, Test Cases, Bug Tracking, Load Testing, Performance Tuning, JMeter, Quality Assurance, Localization, Internationalization

Design & UX
UI Design, Wireframing, Figma, Adobe XD, User Research, Prototyping, Accessibility, Visual Design, Usability Testing, Surveys, Personas, Interviews, UX Writing, Content Strategy, Microcopy, Interaction Design, User Flows, Usability, Design Systems, Component Libraries

Graphic / Print / Visual Design
Graphic Design, Adobe Photoshop, Illustrator, InDesign, Typography, Color Theory, Branding, Layout Design, Retouching, Compositing, Color Correction, Layer Masking, Print Design, Print Production, Prepress, Vector Graphics, Concept Development, Style Guides, Visual Strategy, Brand Identity, Logo Design, Visual Identity, Packaging Design, Structural Design, Pattern Design, Fabric Knowledge, Repeat Design, Photo Editing, Canva, Content Creation, PowerPoint, Keynote, Line Art, Custom Design, Freehand Drawing, Fine Motor Skills, Cultural Knowledge

Fashion / Costume / Set / Interior
Fashion Design, Sketching, Pattern Making, Textile Knowledge, Trend Research, Sewing, Historical Research, Costume Design, Set Design, Scale Modeling, Model Making, Construction Knowledge, Spatial Planning, Exhibit Design, Fabrication Knowledge, Theme Design, Vendor Coordination, Industrial Design, CAD, Ergonomics, Materials Knowledge, Interior Design, Space Planning, AutoCAD, SketchUp, 3D Rendering, Material Selection, Lighting Design, Furniture Selection, Client Communication, Landscape Design, Plant Knowledge, Site Planning, Sustainability, Jewelry Design, Gemology, Metalwork, Automotive Design, Clay Modeling, Aerodynamics Knowledge, Toy Design, Safety Standards, Ceramic Design, Sculpting, Glazing Techniques

Art / Illustration / Animation
Illustration, Drawing, Digital Painting, Concept Art, Storytelling, Storyboarding, Character Design, Environment Design, Anatomy, Cinematography, Sequential Art, Procreate, 3D Modeling, Texturing, Rendering, Lighting, Blender, Maya, ZBrush, Rigging, Animation, Character Animation, Keyframing, Timing, 2D Animation, 3D Animation, Adobe Animate, World Building, Level Design

Video / Motion / Audio Production
After Effects, Motion Design, Video Editing, Adobe Premiere Pro, Final Cut Pro, Color Grading, Sound Editing, Thumbnail Design, Pacing, Retention Optimization, Short Form Content, Captioning, Trend Awareness, Archival Research, Sound Design, Avid Media Composer, Marketing Awareness, DaVinci Resolve, Visual Effects, Nuke, 3D Tracking, Rotoscoping, Color Matching, Broadcast Graphics, Video Production, Title Design, Audio Editing, Audio Engineering, Mixing, Mastering, Pro Tools, Acoustics, Foley, Field Recording, Audio Recording, Signal Processing, Podcast Production, Adobe Audition, Music Production, DAW Software, Composition, Music Theory, Orchestration, Ableton Live, Sound Effects Creation, Post-Production Workflow, Team Coordination, Quality Control

Photography
Photography, Photo Editing, Lightroom, Composition, Camera Operation, Editing

Management / Leadership
Team Leadership, Mentoring, Product Strategy, Roadmapping, Stakeholder Management, Agile, Market Research, Communication, Project Planning, Scrum, Budgeting, Program Management, Cross-functional Coordination, Facilitation, Sprint Planning, Team Coaching, Conflict Resolution, Jira, Coaching, Requirements Gathering, Process Mapping, Project Coordination, Scheduling, Release Management, Coordination, Process Improvement, Technical Mentorship, Hiring, Engineering Leadership, Team Management, Technical Strategy, Architecture, Innovation, Technology Strategy, Leadership, Governance, Vendor Management, IT Strategy, Cybersecurity, Legal Knowledge, Policy Development, Policy Writing, GDPR, Data Privacy, Prioritization, Design Leadership, Stakeholder Communication, Consulting, System Analysis

Finance / Legal
Excel, Financial Modeling, Forecasting, Accounting, Valuation, Bookkeeping, Financial Reporting, Tax Preparation, Risk Analysis, Risk Management, Risk Modeling, Insurance Analysis, Actuarial Software, Economics, Econometrics, Legal Research, Contract Law, Negotiation, Case Management, Regulatory Compliance

Marketing / Sales
SEO, SEM, Content Marketing, Social Media, Google Analytics, Email Marketing, Copywriting, Keyword Research, Content Optimization, Link Building, Technical SEO, Editorial Planning, Social Media Strategy, Community Management, Segmentation, A/B Testing, Growth Hacking, Google Search Console, Google Ads, Campaign Management, Content Writing, Creative Writing, Brand Voice, Sales, CRM, Customer Relationship Management, Lead Generation, Technical Sales, Product Knowledge, Solution Design, Presentations, Upselling, Account Planning, Onboarding, Retention Strategies, Problem Solving, Customer Service, Ticketing Systems, E-commerce Platforms, Inventory Management, Digital Marketing, HubSpot

HR
Recruitment, Employee Relations, Performance Management, HR Policy, Sourcing, Interviewing, Employer Branding, Applicant Tracking Systems, Technical Screening, ATS, Curriculum Design, Training Delivery, Needs Assessment

Operations / Supply Chain
Operations Management, Logistics, Supply Chain Management, Supply Chain Coordination, Procurement, Contract Management

Healthcare
Healthcare Systems, Clinical Trials, Data Management, Biomechanics, Medical Devices

Networking / Telecom
VoIP, SIP, Telephony Systems, Video Conferencing, Cabling, Cooling Systems, Maintenance, Hardware, Troubleshooting, Wireless Networking, RF Engineering, Telecom Protocols

---

## 🚀 Getting Started

### Option 1: Run the Python CLI

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/tech-stack-recommender.git](https://github.com/your-username/tech-stack-recommender.git)
   cd tech-stack-recommender
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas scikit-learn
   ```

3. **Run the script:**
   ```bash
   python tech_stack_recommender.py
   ```

4. **Example Terminal Run:**
   ```text
   ============================================================
    TECH STACK RECOMMENDER — DecodeLabs Project 3
   ============================================================

   Enter at least 3 skills, separated by commas.
   Example: Python, Cloud Computing, Automation

   Your skills: Python, Docker, Kubernetes

   ------------------------------------------------------------
    Based on your skills: Python, Docker, Kubernetes
    Top career-path matches:
   ------------------------------------------------------------
   1. DevOps Engineer           match:  52.4%
      skills: AWS Docker Kubernetes CI/CD Automation Linux Terraform Jenkins

   2. Platform Engineer         match:  46.1%
      skills: Kubernetes Docker CI/CD Automation Cloud Computing Terraform Infrastructure as Code

   3. MLOps Engineer            match:  41.8%
      skills: Python Docker Kubernetes CI/CD Machine Learning Model Deployment Monitoring
   ```

---

### Option 2: Run the Web Dashboard

1. Simply double-click `index.html` or open it with any web browser.
2. Enter your skills into the input field (minimum 3).
3. Click **RUN MATCH** to view animated similarity scores, rank breakdowns, and highlighted matching tags.

---

## 💡 Key AI Concepts Applied

- **Content-Based Filtering:** Recommends items based on inherent attributes rather than community interaction history.
- **Cold-Start Handling:** Uses an explicit onboarding intake (requiring ≥3 skills) and defaults to fallback entries when zero overlap occurs.
- **Vector Space Alignment:** Uses cosine similarity ($$ range, normalized to $$ for non-negative TF-IDF) instead of Euclidean distance to prevent text length bias.
