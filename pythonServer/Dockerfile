# syntax=docker/dockerfile:1

FROM python:3.11.4-alpine AS backend
WORKDIR /backend
COPY . .
ENV PYTHONUNBUFFERED=1
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install -r requirements.txt

# Expose necessary ports
EXPOSE 5001

# Run the Python server
CMD ["python", "/backend/main.py"]
