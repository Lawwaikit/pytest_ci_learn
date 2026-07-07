# 使用官方 Python 轻量镜像
FROM python:3.12-slim as builder

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 默认入口点改为 Python
ENTRYPOINT ["python", "-m", "main"]