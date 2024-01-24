# Palword-SM (Palword Server Manager)

<!-- ![Palworld](/docs/palworld.png) -->

Palword-SM is a set of Docker containers that allow you to easily manage a dedicated server for the Palword game. The aim of this project is to provide a simple UI so that anyone can create their own server with a minimum of knowledge. A simple Docker installation is required.

### 📚 Table of contents
- [🛠️ Installation](#️-installation)  
- [📦 Prerequisites](#-prerequisites)  
- [💻 RCON Commands](#-rcon-commands)  
- [🐛 Report a bug](#-report-a-bug)  
- [📝 License](#-license)  


### 📦 Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)
- [Palworld (Version Steam)](https://store.steampowered.com/app/1623730/Palworld/?l=french)

### 🛠️ Installation

1. Clone the repository
```bash
git clone git@github.com:TheoBIET/Palword-SM.git
```

2. Go to the project folder
```bash
cd Palword-SM
```

3. Create the `config.yml` from the `config.example.yml` file
```bash
cp config.example.yml config.yml
```

4. Edit the `config.yml` file to your liking

5. Start the containers
```bash
docker-compose up -d
```

6. Open Palworld and connect to your server 🌞

### 💻 RCON Commands

You can find the list of RCON commands [here](https://tech.palworldgame.com/server-commands).

### 🐛 Report a bug

If you find a bug, please report it into the [issues](https://github.com/TheoBIET/Palword-SM/issues) section.

### 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
