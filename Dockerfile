FROM python:3

WORKDIR /urs/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "fastapi", "run", "main.py", "--port", "80" ]