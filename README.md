# Search Engine with Filtering

Brief overview of the project.

---

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Local Setup](#local-setup)
  - [Other Setup](#other-setup)
  - [Other Files](#other-files)
  - [Run](#run)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

A search engine built using Python and Flask that utilizes Google Custom Search API to retrieve results and applies filtering techniques to reorder the results based on defined criteria.

### Built With

- Python
- Flask
- Google Custom Search API

---

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.9+
- [Required Python packages](requirements.txt)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Yashp-5/Engine.git
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

---



## Project Structure

- `app.py` - Web interface
- `filter.py` - Code to filter results
- `search.py` - Code to fetch search results
- `settings.py` - Settings needed by other files
- `storage.py` - Code to save results to a database

---

## Local Setup

### Other Setup

1. Create a programmable search engine and obtain an API key [here](https://developers.google.com/custom-search/v1/overview).
2. Save the API key and other settings in `settings.py`.
3. Download a list of ad and tracker URLs from [here](blacklist.txt) and save it as `block_sites.txt`.

### Other Files

- `block_sites.txt` - List of ad and tracker URLs
- `storage.py` - Save results to a database

### Run

Run the project with:

```sh
flask --debug run --port 5001
```

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

Your Name - yash.purohit2610@gmail.com

Project Link: [https://github.com/Yashp-5/Engine](https://github.com/Yashp-5/Engine)



