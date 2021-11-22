FROM node:16.13.0-alpine3.14 AS build
WORKDIR /dist/src/app
RUN npm cache clean --force
COPY . .
RUN npm install
RUN npm run build --development
FROM nginx:1.17.1-alpine
RUN apk --no-cache add wget libstdc++
COPY --from=build /dist/src/app/dist/suggestyangular /usr/share/nginx/html
EXPOSE 80