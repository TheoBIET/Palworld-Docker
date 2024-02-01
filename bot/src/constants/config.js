require('dotenv').config();

module.exports = {
  TOKEN: process.env.DISCORD_TOKEN,
  CLIENT_ID: process.env.DISCORD_CLIENT_ID,
  REST_VERSION: process.env.DISCORD_REST_VERSION,
}