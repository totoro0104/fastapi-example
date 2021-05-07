# fastapi-example
基于fastapi+tortoise-orm+fastapi-login的后端搭建

项目目前仅集成了异步ORM、迁移和用户认证，只作为学习fastapi框架搭建的案例

## 环境要求
>  Python3.7+

>  fastapi

>  tortoise-orm (支持PostgreSQL>=9.4、MySQL/MariaDB、SQLite)

>  fastapi-login (也可以选择功能更全面的fastapi-users)

>  aerich

## 项目运行
```
# Initialize the config file and migrations location
aerich init -t config.TORTOISE_ORM

# Init db
aerich init-db

# Make migrate and upgrade
aerich migrate

aerich upgrade

# Run project
uvicorn manage:app
```
