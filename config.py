import os


class DevConfig:
    # 从 .env 加载敏感信息
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('DATABASE_URI')

    # 应用逻辑配置
    # 分页大小
    PER_PAGE = 20
    # 文件上传大小限制（10MB）
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024


class ProdConfig:
    pass
