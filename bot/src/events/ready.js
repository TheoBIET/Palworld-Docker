const { ActivityType } = require("discord.js");
const { loadCommands } = require("../utils/loaders");

module.exports = async (client) => {
  const guildsCount = client.guilds.cache.size;
  console.log(`${client.user.tag} is online in ${guildsCount} guilds!`);
  client.user.setStatus('dnd');
  client.user.setActivity({
    name: 'DavDav develop me',
    type: ActivityType.Watching,
  });

  loadCommands(client);
}