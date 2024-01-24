# https://github.com/thijsvanloef/palworld-server-docker/blob/main/docker-compose.yml

FROM cm2network/steamcmd:root
LABEL maintainer="dev.theobiet@gmail.com"

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    xdg-user-dirs=0.17-2 \
    procps=2:3.3.17-5 \
    wget=1.21-1+deb11u1 \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN python -m pip install --no-cache-dir \
    pyyaml

# Install RCON
RUN wget -q https://github.com/itzg/rcon-cli/releases/download/1.6.4/rcon-cli_1.6.4_linux_amd64.tar.gz -O - | tar -xz
RUN mv rcon-cli /usr/bin/rcon-cli

# Environment variables
ENV PUID=1000 \
    PGID=1000 \
    MULTITHREADING=false \
    UPDATE_ON_BOOT=true

# Copy files
COPY ./bin/* /home/steam/server/
RUN chmod +x /home/steam/server/*.sh

COPY ./scripts/* /home/steam/server/scripts/

COPY ./config.yml /home/steam/server/config.yml

WORKDIR /home/steam/server

# Healthcheck
HEALTHCHECK --start-period=5m \
    CMD pgrep "PalServer-Linux" > /dev/null || exit 1

EXPOSE ${PORT} ${RCON_PORT}
ENTRYPOINT ["/home/steam/server/run.sh"]