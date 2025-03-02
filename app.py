from dotenv import load_dotenv
# 程序启动第一时间加载环境变量，防止后续使用环境变量时因为加载过晚导致环境变量为 None 问题
load_dotenv()
from learn import create_app

app = create_app()


if __name__ == '__main__':
    app.run()
