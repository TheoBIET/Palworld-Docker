const { PALDEX } = require('../constants');

const filterJsFiles = (files) => {
  return files.filter((file) => file.endsWith('.js'));
}

const getPalByName = (name) => {
  const pal = PALDEX.find((pal) => pal.name.toLowerCase() === name.toLowerCase());
  if (!pal) return null;
  return pal;
}

const getPalsList = () => {
  return PALDEX.map((pal) => pal.name);
}

module.exports = {
  filterJsFiles,
  getPalByName,
  getPalsList,
};