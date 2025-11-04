FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python", "-m", "src.loganalyzer.main"]
