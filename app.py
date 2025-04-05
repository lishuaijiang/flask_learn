from dotenv import load_dotenv
load_dotenv()
from learn import create_app

app = create_app()


if __name__ == '__main__':
    app.run()
