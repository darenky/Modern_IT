FROM python:3

WORKDIR /usr/src/app/lab4

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "unittest", "discover", "-p", "*Tests.py", "-v"]
