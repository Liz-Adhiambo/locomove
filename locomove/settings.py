from dotenv import dotenv_values


config = dotenv_values(".env")

"""
"""

EXPIRES_IN = config["EXPIRES_IN"]
JWT_SECRET_KEY = config["JWT_SECRET_KEY"]
JWT_REFRESH_SECRET_KEY = config["JWT_REFRESH_SECRET_KEY"]
ALGORITHM = config["JWT_ALGORITHM"]
REFRESH_TOKEN_EXPIRE_MINUTES = config["REFRESH_TOKEN_EXPIRE_MINUTES"]
