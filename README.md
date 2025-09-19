# 📊 CORD-19 Data Explorer

This project analyzes the **CORD-19 metadata.csv dataset** (COVID-19 research papers) and provides a simple interactive **Streamlit app** to explore the findings.

---

## 🚀 Features
- Load and clean the dataset (`metadata.csv`)
- Perform basic analysis (publication trends, top journals, word frequencies)
- Generate visualizations with Matplotlib/Seaborn
- Interactive web app built with Streamlit

---

## 📂 Project Structure
Frameworks Assignment/
│
├── data/ # Dataset folder (ignored in Git)
│ └── metadata.csv
├── src/ # Source code
│ ├── init.py
│ ├── data_prep.py # Load & clean dataset
│ ├── analysis.py # Data analysis & plots
│ └── app.py # Streamlit application
├── notebooks/ # Optional Jupyter notebooks
│ └── exploration.ipynb
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files/folders
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation

1. **Clone the repository:**
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment
Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate   # macOS/Linux
Install dependencies:

pip install -r requirements.txt
Place the dataset:
Put metadata.csv inside the data/ folder. For testing, you can use a smaller sample (metadata_sample.csv).

🧑‍💻 Usage
Run analysis script:

python -m src.analysis
Run Streamlit app:

python -m streamlit run src/app.py
Open your browser at http://localhost:8501.

📊 Example Visualizations
Number of publications per year

Top journals publishing COVID-19 research

Word cloud of paper titles

Distribution of papers by source

📝 Notes
The full dataset is large; for quick testing, use a sample CSV.

data/metadata.csv is ignored in Git to prevent pushing large files.

📖 Learning Objectives
By completing this project, I practiced:

Loading and cleaning real-world datasets with Pandas

Creating visualizations with Matplotlib/Seaborn

Building an interactive web app with Streamlit

Using Git/GitHub for project version control
