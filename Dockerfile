FROM python:3.9
ADD test.py .

RUN python3 -V
CMD ["python", "./test.py"]
