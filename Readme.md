# **Blog Application Using Flask**

A **full-featured** blog application built with **Flask, PostgreSQL, and SQLAlchemy**, utilizing **HTML, CSS, JavaScript, and Bootstrap** for the frontend.

## **Features**

✅ **Secure Authentication** – Users can **register, log in, and log out** securely.  
✅ **Access Control** –  
   - Logged-out users **cannot access the home page**.  
   - Logged-in users **cannot access login/register pages**.  
✅ **Blog Management** –  
   - Users can **view blogs** posted by others, including the **author’s name** and **time of posting**.  
   - Users can **create, update, and delete** their own blogs.  
✅ **Image Handling** –  
   - Old thumbnails are **deleted from the server** when a blog’s thumbnail is updated.  
   - Blog images are **removed from the server** when a blog is deleted.  

---

## **Prerequisites**  
Before running this project, ensure you have the following installed:  
1️⃣ **Python**  
2️⃣ **Flask**  
3️⃣ **PostgreSQL**  
4️⃣ **SQLAlchemy**  

---

## **💻 Installation & Setup**  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/AmmarTheDeveloper/flask-blog-app.git
   cd flask-blog-app
   ```
2. **Configure database:**  
   - Set up a **PostgreSQL** database.
   - Update the database URI in the application settings.
3. **Run migrations:**  
   ```sh
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. **Start the application:**  
   ```sh
   flask run
   ```
5. Open your browser and go to **http://127.0.0.1:5000**

## **🙌 Contributing**
Feel free to fork this repository and submit pull requests for improvements!

---

## **👨‍💻 Created & Developed By**
**AmmarTheDeveloper** 🚀

