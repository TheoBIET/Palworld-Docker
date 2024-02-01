const { REST, Routes } = require('discord.js');
const { filterJsFiles } = require('./functions');
const { CONFIG: { TOKEN, CLIENT_ID, REST_VERSION } } = require('../constants');
const fs = require('fs');

const loadDir = (dir) => {
  const loaded = [];

  filterJsFiles(fs.readdirSync(dir)).forEach(async (file) => {
    loaded.push({
      name: file.split('.')[0],
      item: require(`../${dir.split('/')[2]}/${file}`)
    });
  });

  return loaded;
}

const loadCommands = async (client) => {
  const commands = loadDir('./app/commands');

  commands.forEach(async (command) => {
    if (!command.item.data) throw new Error(`Command ${command.name} is missing data`);
  });

  try {
    const rest = new REST({ version: REST_VERSION }).setToken(TOKEN);

    await rest.put(
      Routes.applicationCommands(CLIENT_ID),
      { body: commands.map((command) => command.item.data) },
    );

    const commandsNames = commands.map((command) => command.name);
    console.log(`${commands.length} commands: ${Object.values(commandsNames).join(', ')}`);
  } catch (error) {
    console.error(error);
  }
};

const loadEvents = async (client) => {
  const events = loadDir('./app/events');

  events.forEach(async (event) => {
    if (!event.name) throw new Error(`Event ${event} is missing name`);
    client.on(event.name, event.item.bind(null, client));
  });

  const eventsNames = events.map((event) => event.name);
  console.log(`${events.length} events: ${eventsNames.join(', ')}`);
};

module.exports = {
  loadCommands,
  loadEvents,
}