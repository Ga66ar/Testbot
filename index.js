const { Telegraf } = require('telegraf');
const express = require('express');

// Telegram Bot Token
const BOT_TOKEN = '7530794420:AAHpyI_BZFCUp0kq_UdYaFuLBA0WidFBGTw';
const bot = new Telegraf(BOT_TOKEN);

// Express server for Koyeb health checks
const app = express();
const PORT = process.env.PORT || 3000;

// Default route
app.get('/', (req, res) => {
  res.send('Bot is running!');
});

// Start Express server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Basic bot commands
bot.start((ctx) => ctx.reply('Welcome to my bot!'));
bot.help((ctx) => ctx.reply('Send me a message, and I will reply!'));
bot.on('text', (ctx) => ctx.reply(`You said: ${ctx.message.text}`));

// Start bot polling
bot.launch();

// Graceful stop
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
