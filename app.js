require('dotenv').config();
const { TelegramBot } = require('bottender');
const { createServer } = require('bottender/express');
const model = require('./model');

const url = process.env.WEBHOOK_URL;
// const url = 'https://stanbot.lmsbothq.com:8443';

const bot = new TelegramBot({
  accessToken: process.env.TELEGRAM_TOKEN
});

bot.onEvent(async context => {
  if (context.event.text == '/start') {

    const wellcome_message = [
      'Добро пожаловать! Я постараюсь помочь вам в выборе вашей будущей профессии.',
      'Для этого мне надо знать твой профиль в какой-нибудь социальной сети (например, вконтакте).',
      'Пришли мне ссылку на твой профиль (будь внимателен, чтобы там была цифра!) и я попробую что-нибудь посоветовать.',
    ];

    context.sendText(wellcome_message.join(' '));
  }
  else {
    model.get_areas(
      context.event.text,
      (err, prediction) => {

        if (err) {
          context.sendText('Данные вашего профиля закрыты, или id не найден :(');
        }
        else {
          context.sendText('Кажется, ты интересуешься областью:' + prediction);
        }
      });
  }

  //await context.sendText('Привет! Я предскажу твое карьерное будущее. Введи VK id');
});

const server = createServer(bot,
  {
    verifyToken: process.env.TELEGRAM_TOKEN
  });

server.listen(process.env.PORT || 4000, () => {
  bot.connector.client.setWebhook(url);
  console.log('url:', url);
  console.log('tgtoekn :', process.env.TELEGRAM_TOKEN);
  console.log('server is running');
});