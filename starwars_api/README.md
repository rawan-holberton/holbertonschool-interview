# Star Wars API

## Description

This project consists of creating a Node.js script that retrieves and displays all characters from a specific **Star Wars movie** using the **Star Wars API (SWAPI)**.

The program receives a movie ID as an argument, requests the corresponding movie data from the API, and prints each character name in the same order as they appear in the movie's `characters` list.

## Requirements

- All files are interpreted on **Ubuntu 14.04 LTS** using **Node.js 10.14.x**
- Allowed editors:
  - vi
  - vim
  - emacs
- All files must:
  - Start with the shebang:
    ```javascript
    #!/usr/bin/node
    ```
  - End with a new line
  - Be executable
  - Follow **semistandard** style rules:
    - Standard JavaScript style
    - Semicolons required
    - Airbnb style as reference
- A `README.md` file is mandatory at the root of the project
- The use of `var` is forbidden
- File length will be tested using `wc`

## Installation

### Install Node.js 10

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
````

### Install semistandard

```bash
sudo npm install semistandard --global
```

### Install request module

```bash
sudo npm install request --global
```

Set the Node module path:

```bash
export NODE_PATH=/usr/lib/node_modules
```

## Project Structure

```
starwars_api/
│
├── 0-starwars_characters.js   # Script to retrieve Star Wars characters
└── README.md                  # Project documentation
```

## Task

### 0. Star Wars Characters

Create a script that prints all characters of a Star Wars movie.

The program must:

* Take the movie ID as the first positional argument
* Use the Star Wars API
* Use the `request` module
* Display one character name per line
* Keep the same order as the `characters` list returned by the API

## Usage

Run the program with:

```bash
./0-starwars_characters.js <Movie_ID>
```

Example:

```bash
./0-starwars_characters.js 3
```

Output:

```text
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## How It Works

The script:

1. Receives a movie ID from the command line.
2. Sends a request to the Star Wars API.
3. Retrieves the movie information.
4. Extracts the character URLs.
5. Requests each character information.
6. Prints each character name in the original order.

## API

The project uses:

**Star Wars API (SWAPI)**

Endpoint example:

```
https://swapi-api.hbtn.io/api/films/<movie_id>
```

## Repository

GitHub repository:

`holbertonschool-interview`

Directory:

`starwars_api`

File:

`0-starwars_characters.js`

## Author

By Rawan for Holberton School project Star Wars API
