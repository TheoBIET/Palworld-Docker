module.exports = async (client, interaction) => {
  if (!interaction.isCommand() && !interaction.isAutocomplete()) return;
  const { commandName: name } = interaction;
  const command = require(`../commands/${name}`);
  if (!command) return;

  if (interaction.isCommand()) {
    try {
      await command.execute(client, interaction, interaction.options);
    } catch (error) {
      console.error(error);
      await interaction.reply({
        content: 'There was an error while executing this command, please try again later.',
        ephemeral: true,
      });
    }
  }

  else if (interaction.isAutocomplete()) {
    try {
      await command.autocomplete(client, interaction);
    } catch (error) {
      console.error(error);
      await interaction.reply({
        content: 'There was an error while executing this command, please try again later.',
        ephemeral: true,
      });
    }
  }
}