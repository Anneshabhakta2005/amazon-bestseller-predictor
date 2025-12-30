# FSP_Project_Amazon_bestseller_predictor
🚀 Live Demo
👉 https://amazon-bestseller-predictor.streamlit.app

✅ STEP 1: Final files that MUST be in your folder
Before uploading, make sure your project folder looks like this:

amazon-bestseller-predictor/
│
├── app.py

├── amazon_books_model.pkl

├── main_genre_encoder.pkl

├── sub_genre_encoder.pkl

├── requirements.txt

├── README.md

✅ STEP 2: Create .gitignore file (IMPORTANT)

Create a new file named .gitignore and add this:

__pycache__/
*.pyc
.env
.ipynb_checkpoints/


📌 Do NOT ignore .pkl files – they are required for deployment.

✅ STEP 3: Create GitHub Repository

Go to 👉 https://github.com

Click New Repository

Repository name:

amazon-bestseller-predictor


Description:

Amazon Bestseller Prediction using Machine Learning & Streamlit


Set to Public

❌ Do NOT add README (you already have one)

Click Create Repository

✅ STEP 4: Upload using VS Code (EASIEST WAY)
🔹 Open VS Code

Open amazon-bestseller-predictor folder

Click Source Control (Ctrl + Shift + G)

🔹 Initialize Git

Click “Initialize Repository”

🔹 Stage Files

Click + (Stage All Changes)

🔹 Commit

Message:

Initial commit – Amazon Bestseller Predictor


Click ✔ Commit

🔹 Publish to GitHub

Click Publish Branch

Select GitHub

Select Public

🎉 DONE!

✅ STEP 5: Upload using Terminal (Alternative)

If you prefer terminal:

git init
git add .
git commit -m "Initial commit – Amazon Bestseller Predictor"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/amazon-bestseller-predictor.git
git push -u origin main

✅ STEP 6: Check on GitHub

Open:

https://github.com/YOUR_USERNAME/amazon-bestseller-predictor


You should see:

app.py

.pkl files

README.md

requirements.txt

⚠️ VERY IMPORTANT FOR STREAMLIT CLOUD

✔ .pkl files must be pushed
✔ requirements.txt must exist
✔ app.py must be in root
