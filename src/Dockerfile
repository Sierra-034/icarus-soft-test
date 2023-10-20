FROM python:3.10

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV SQLALCHEMY_DATABASE_URI=postgresql://postgres:somepassword@localhost:5432/icarus_soft
EXPOSE 5000

COPY . .

CMD [ "python3", "main.py"]
