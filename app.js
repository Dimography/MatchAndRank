require('dotenv').config();
const { TelegramBot } = require('bottender');
const { createServer } = require('bottender/express');

const url = process.env.WEBHOOK_URL;

const bot = new TelegramBot({
  accessToken: process.env.TELEGRAM_TOKEN
});

bot.onEvent(async context => {
  await context.sendText('Hello World');
});


const server = createServer(bot, { verifyToken: process.env.TELEGRAM_TOKEN });

server.listen(5050, () => {
    bot.connector.client.setWebhook(url);
    console.log('server is running');
});