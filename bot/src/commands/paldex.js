const { COMMANDS } = require('../constants');
const { getPalByName, getPalsList } = require('../utils/functions');
const { createPalEmbed, createPalSpawnsEmbed, createPalSkillsEmbed } = require('../utils/embeds');

module.exports = {
  data: COMMANDS.PALDEX,
  async execute(_, interaction, opts) {
    const palOpt = opts.getString('pal');
    const pal = getPalByName(palOpt);
    if (!pal) return interaction.reply(`Le pal ${palOpt} n'existe pas.`);
    const { embed, row } = createPalEmbed(pal);

    interaction.reply({
      embeds: [embed],
      components: [row],
    });

    const filter = (i) => i.user.id === interaction.user.id;
    const collector = interaction.channel.createMessageComponentCollector({ filter });

    collector.on('collect', async (i) => {
      if (i.customId === 'day' || i.customId === 'night') {
        const { embed } = createPalSpawnsEmbed(pal, i.customId);

        await i.update({
          embeds: [embed],
          components: [row],
        });
      }

      if (i.customId === 'skills') {
        const { embed } = createPalSkillsEmbed(pal);

        await i.update({
          embeds: [embed],
          components: [row],
        });
      }
    });
  },
  async autocomplete(_, interaction) {
    const value = interaction.options.getFocused().toLowerCase();
    const choices = getPalsList().filter(choice => choice.toLowerCase().includes(value));
    await interaction.respond(
      choices.map(choice => ({ name: choice, value: choice })).slice(0, 25),
    );
  },
}