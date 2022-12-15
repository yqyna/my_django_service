FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /etc/nginx/html

CMD ["nginx", "-g", "daemon off;"]