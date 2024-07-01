FROM python
WORKDIR /app
COPY . .
RUN pip install -r req.txt
CMD uvicorn --reload --host 0.0.0.0 --port 8080 main:app
