# Torrent Site for Movies - Flask

This project is a Flask-based web application designed to search for movie torrents, fetch torrent data, and manage torrent downloads using the Seedr API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Complexities](#complexities)
- [Solutions](#solutions)
- [Challenges](#challenges)
- [License](#license)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/faisal-fida/Torrent-Site-for-Movies--Flask-.git
cd Torrent-Site-for-Movies--Flask-
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file with the following content:

```
SEEDR_EMAIL=<your_seedr_email>
SEEDR_PASSWORD=<your_seedr_password>
```

4. Run the application:

```sh
python main.py
```

## Usage

The application provides the following functionalities:

1. **Search Torrents**: Use the `/search` endpoint to search for movie torrents.
2. **Add and Manage Torrents**: Use the Seedr API to add torrents, manage downloads, and rename files.

## Features

- **Asynchronous Data Fetching**: The project uses asynchronous requests to fetch torrent data from an external API, ensuring non-blocking operations and better performance.
- **Database Integration**: The project utilizes Seedr API for managing torrent downloads, including adding torrents and renaming files.
- **Flask Integration**: The project integrates Flask for building the web interface, handling user inputs, and rendering templates.
- **Efficient Data Fetching**: Implemented efficient data fetching using asynchronous requests in `get_tor.py`, which allows concurrent fetching of torrent data.
- **Seedr API Integration**: The `main.py` file demonstrates how to integrate and utilize the Seedr API for adding and managing torrents, ensuring smooth operations.
- **Logging**: Comprehensive logging is set up in `app.py` to track user activities and application events, aiding in debugging and monitoring.
- **Error Handling**: Managing errors during data fetching and API interactions required robust error handling mechanisms to ensure smooth user experience.
- **Concurrency Management**: Ensuring that multiple asynchronous operations do not lead to race conditions or data corruption was a key challenge.
- **File Management**: Handling the renaming and organization of downloaded files required careful design and implementation to avoid conflicts and maintain consistency.
