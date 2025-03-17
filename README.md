# 🥐 Recipe Maker 

Recipe Maker is a web-based app that helps users find recipes instantly using an AI-powered RAG (Retrieval-Augmented Generation) model. It generates personalized recipes based on the ingredients or dishes you want to cook.


## 📝 About the Project

Recipe Maker is a web-based app that helps users find recipes instantly using an AI-powered RAG (Retrieval-Augmented Generation) model. It generates personalized recipes based on the ingredients or dishes you want to cook.


## ✨ Features

### 🍴 Personalized Recipes:
-Input the natural language prompt get personalised reccomendation with all ingrediants in grams and direction for preparation.

### 🧠 RAG Model: 
-Utilizes AI to fetch the best recipes.

### 👤 User Authentication: 
-Secure login, signup, and password recovery with unique code.


## ⚙️ Tech Stack

### Frontend: HTML, CSS, JavaScript

### Backend: Django, Python

### Model: RAG with google's gemini api

### Database: SQLite

### API Integration: REST API with CSRF protection

### Deployment: Ngrok for testing 

## 🚀 Installation

### 1. Install django framework 
```bash
python -m pip install Django
```
### 2. Clone the repo:
```bash
git clone https://github.com/yourusername/precision-baker.git
cd precision-baker
```
### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```
### 4. Run migrations
```bash
py manage.py migrate
```
### 5. Runserver
```bash
py manage.py runserver
```
## 📌 Usage
#### - Visit: http://127.0.0.1:8000/
#### - Sign up or log in.
#### - Enter the dish, and watch the magic happen! ✨

## 🔑 API Documentation
### Get Recipe:
-GET /get_recipe?query=<recipe_name>
### User Authentication:
-POST /signup

-POST /login

## 🔮 Future Enhancements
#### -Add meal planner.
#### -Integrate voice commands.
#### -Improve recipe recommendations.

