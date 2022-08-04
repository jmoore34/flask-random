FROM python:3

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV production
ENTRYPOINT [ "python", "app.py" ]