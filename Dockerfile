FROM python:3.7-alpine

COPY /app /app
WORKDIR /app
RUN pip3 install flask
EXPOSE 5010
CMD ["python3","Base_code.py"]
