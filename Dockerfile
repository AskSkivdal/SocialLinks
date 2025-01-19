FROM python:3.13-alpine AS builder

RUN pip install jinja2

WORKDIR /usr/server/app/
COPY . .

RUN python3 build.py


FROM rust AS minify

RUN cargo install minhtml

WORKDIR /usr/server/minify/

COPY --from=builder /usr/server/app/build/ .

RUN minhtml --output ./index.html --keep-closing-tags --minify-css ./index.html




FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=minify /usr/server/minify/ /www/data/
RUN gzip -rk /www/data/