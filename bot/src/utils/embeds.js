const { EmbedBuilder, ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');

const createPalEmbed = (pal) => {
  const embed = new EmbedBuilder()
    .setColor('#2eff8d')
    .setTitle(pal.name)
    .setURL(pal.wikiUrl)
    .setDescription(pal.description)
    .setImage(pal.imageUrl)
    .addFields(
      { name: "Aptitudes", value: pal.suitability.map((s) => s.type).join(', ')},
      { name: "Drops", value: pal.drops.join(', ')},
      { name: "Aura", value: `${pal.aura.name}\n${pal.aura.description}`}
    )

  const row = new ActionRowBuilder()
    .addComponents(
      new ButtonBuilder()
        .setLabel('Wiki')
        .setStyle(ButtonStyle.Link)
        .setURL(pal.wikiUrl)
        .setEmoji('📖'),
      new ButtonBuilder()
        .setCustomId('skills')
        .setLabel('Attaques')
        .setStyle(ButtonStyle.Secondary)
        .setEmoji('⚔️'),
      new ButtonBuilder()
        .setCustomId('day')
        .setLabel('Spawn de jour')
        .setStyle(ButtonStyle.Secondary)
        .setEmoji('🌞'),
      new ButtonBuilder()
        .setCustomId('night')
        .setLabel('Spawn de nuit')
        .setStyle(ButtonStyle.Secondary)
        .setEmoji('🌙')
    );

  return { embed, row };
}

const createPalSpawnsEmbed = (pal, customId) => {
  const embed = new EmbedBuilder()
    .setColor('#2eff8d')
    .setTitle(pal.name)
    .setDescription(pal.description)
    .setURL(pal.wikiUrl)
    .setThumbnail(pal.imageUrl)
    .setImage(pal.spawns[customId]);

  return { embed };
}

const createPalSkillsEmbed = (pal) => {
  const embed = new EmbedBuilder()
    .setColor('#2eff8d')
    .setTitle(pal.name)
    .setDescription(pal.description)
    .setThumbnail(pal.imageUrl)
    .addFields(
      pal.skills.map((s) => {
        return {
          name: `${s.name}`,
          value: `${s.description}\n__**Type :**__ ${s.type}\n__**Puissance :**__ ${s.power} (${s.cooldown}s de rechargement)\n__**Niveau :**__ ${s.level}\n\n`,
        }
      })
    );

  return { embed };
}

module.exports = {
  createPalEmbed,
  createPalSpawnsEmbed,
  createPalSkillsEmbed,
};