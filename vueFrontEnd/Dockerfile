# syntax=docker/dockerfile:1

FROM node:18-alpine AS frontend
WORKDIR /app
COPY . .
RUN npm install -g serve
RUN npm install
RUN npm run build

EXPOSE 3000

# Run the Python server
CMD ["serve", "-s", "dist"]
