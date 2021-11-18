FROM python:3.7
WORKDIR /tesseract-flask
ENV FLASK_APP=main.py
ENV FLASK_ENV = production
ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN apt-get install -y tesseract-ocr
RUN pip install opencv-python
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "main.py"]