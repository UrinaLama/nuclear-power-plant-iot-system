# Nuclear Power Plant Monitoring & Accident Detection System

## Overview

Nuclear energy plays a crucial role in meeting world’s growing demand for reliable and low-carbon electricity, but its generation requires safe operation in nuclear power plants. In recent years, Internet of Things (IoT) has been increasingly adopted in industrial systems. In nuclear power plants, IoT technologies can assist plant operators by continuously observing power plant conditions, detecting abnormal behavior early, and improving operational safety.

Our IoT-based nuclear power plant monitoring system simulates data from multiple virtual sensors such as pressure, coolant temperature, water level, reactor power, radiation levels, hydrogen concentration, and radiation dose deployed in a reactor coolant system.  The simulated data is taken from the Nuclear Power Plant Accident Data (NPPAD) dataset to ensure realistic behavior under both normal and abnormal operating conditions.
Each virtual sensor publishes data using the MQTT messaging protocol. The data is collected and processed by a Node-RED, which manages data flows, performs basic processing and forwards the measurements to a time-series database, InfluxDB for storage. Grafana dashboards are used to visualize the data, enabling real-time monitoring as well as historical analysis of reactor conditions. When abnormal conditions are detected such as coolant loss scenario or unusually high radiation levels, the system automatically triggers alerts that are sent to plant operators via Telegram, supporting rapid response and decision-making.

This project was developed as a part of the Software Engineering for Internet of Things (SE4IOT) course at the University of L’Aquila during the Fall Semester 2025–2026.

## System Architecture

<p align="center">
  <img src="images/IOT nuclear power plant system architecture.png" alt="logo" width="90%"/>
</p>

## Built with

[![Docker][Docker.com]][Docker-url][![Python][Python.org]][Python-url][![MQTT][MQTT.com]][MQTT-url][![Nodered][Nodered.org]][Nodered-url][![InfluxDB][InfluxDB.com]][InfluxDB-url][![Grafana][Grafana.com]][Grafana-url][![Telegram][Telegram.org]][Telegram-url]

## Getting Started
### Prerequisites

Ensure that the following software is installed on your system:

* Docker

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/Igli333/nuclear-power-plant-iot-system.git
   ```
2. Run the containers
   ```sh
   docker-compose up
   ```
3. Navigate to http://localhost:3000/, where you can see the dashboard. Use the following credentials: username=admin, password=admin

    To interact with InfluxDB, navigate to http://localhost:8086/. Use the following credentials: username=admin, password=admin1234

    To interact with Node-Red, navigate to http://localhost:1880/. 

## Configuration

The configuration of the system is mainly contained in the docker-compose.yml file. Make sure that all exposed and mapped ports are free on your local environment.

* 1883 for Mosquitto MQTT Broker
* 3000 for Grafana
* 8086 for InfluxDB
* 1886 for Node-RED

### Telegram Configuration

1. Create a Telegram bot
   - Create/open a telegram account 
   - Search for @botfather in the Telegram search bar
   - Start a chat with @BotFather.
   - Type `/newbot` and follow the prompts to set up a new bot. Save the bot token (looks like `5678910:AAC_Xmw...`).
2. Obtain your ChatId
   - One way to get the chat id is to visit the url:
https://api.telegram.org/bot<YourBOTToken>/getUpdates and look for chat id on the returned json. Alternatively, you can
search for “@myidbot” on Telegram, start a conversation, and type `/getid`,
the bot will respond with your chatId. 
3. Configure environment in node-red

         TELEGRAM_BOT_TOKEN=your_bot_token_here
         TELEGRAM_CHAT_ID=your_chat_id_here

4. Restart docker compose for the environment variables to take an effect. If its successful, alert will be sent to Telegram.

## Developed by

- [Urina Lama](https://github.com/UrinaLama/)
- [Igli Balla](https://github.com/Igli333)
- [Mahira Ibnath Joytu](https://github.com/Joytu)

<!-- Markdown Link and images-->
[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[MQTT.com]: https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=eclipsemosquitto&logoColor=white
[Nodered.org]: https://img.shields.io/badge/Node--RED-8F0000?style=for-the-badge&logo=nodered&logoColor=white
[InfluxDB.com]: https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white
[Grafana.com]: https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white
[Telegram.org]: https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white
[Docker-url]: https://www.docker.com/
[Python-url]: https://www.python.org/
[MQTT-url]: https://mqtt.org/
[Nodered-url]: https://nodered.org/
[InfluxDB-url]: https://www.influxdata.com/products/influxdb/
[Grafana-url]: https://grafana.com/
[Telegram-url]: https://telegram.org/