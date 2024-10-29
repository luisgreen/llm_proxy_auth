FROM python:3.9.20-alpine3.19
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir 
ENTRYPOINT [ "python", "proxy.py" ]
EXPOSE 5000
