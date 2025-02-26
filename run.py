from app import create_app
app = create_app()

if __name__ == "__main__":
    app.secret_key="$uperm@n"
    app.run(host="localhost",debug=True)