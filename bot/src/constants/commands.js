const paldex = require("./paldex")

const OptionsTypes = {
  SUB_COMMAND: 1,
  SUB_COMMAND_GROUP: 2,
  STRING: 3,
  INTEGER: 4,
  BOOLEAN: 5,
  USER: 6,
  CHANNEL: 7,
  ROLE: 8,
  MENTIONABLE: 9,
  NUMBER: 10,
  ATTACHMENT: 11,
}

module.exports = {
  PALDEX: {
    name: 'paldex',
    description: 'Récupère les informations du Paldex à propos d\'un Pal',
    options: [
      {
        name: 'pal',
        description: 'Le nom du Pal',
        type: OptionsTypes.STRING,
        required: true,
        autocomplete: true,
      },
    ],
  }
}