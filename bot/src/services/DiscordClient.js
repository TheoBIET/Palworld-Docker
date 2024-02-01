const { Client, GatewayIntentBits, Partials } = require('discord.js');
const { CONFIG: { TOKEN } } = require('../constants');
const { loadEvents } = require('../utils/loaders');

class DiscordClient {
  constructor() {
    this.client = new Client({
      intents: [
        GatewayIntentBits.Guilds
      ],
      partials: [
        Partials.Channel,
        Partials.GuildMember,
      ],
    });
  }

  init() {
    this.client.login(TOKEN);
    loadEvents(this.client);
  }
}

module.exports = new DiscordClient();