FROM node:lts-alpine

ENV NODE_ENV=production \
    DISCORD_BOT_TOKEN=<YOUR_DISCORD_BOT_TOKEN> \
    DISCORD_BOT_PREFIX=<YOUR_DISCORD_BOT_PREFIX> \
    DISCORD_REST_VERSION=10

WORKDIR /app

COPY package.json package-lock.json ./
COPY app ./app

RUN npm install -g yarn
RUN yarn install --production

VOLUME ["/app", "/node_modules"]
CMD ["yarn", "start"]