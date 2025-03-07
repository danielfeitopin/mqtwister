# MQTwister

<div align="center">

***A Tool for Man-in-the-Middle (MitM) Attacks on the MQTT Protocol.***

[![Python](https://img.shields.io/badge/Python-black?logo=python&logoColor=white&labelColor=grey&color=%233776AB)](<#> "Python")
[![License](<https://img.shields.io/github/license/danielfeitopin/mqtwister>)](<LICENSE> "License")
[![GitHub issues](https://img.shields.io/github/issues/danielfeitopin/mqtwister)](<https://github.com/danielfeitopin/mqtwister> "Issues")
[![GitHub stars](https://img.shields.io/github/stars/danielfeitopin/mqtwister)](<https://github.com/danielfeitopin/mqtwister/stargazers> "Stars")

<div align="center" width="90%">

![Usage Example](./docs/img/readme-terminal.gif)

</div>

</div>

## Table of Contents

- [MQTwister](#mqtwister)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [Using `requirements.txt`](#using-requirementstxt)
    - [Using `Pipenv`](#using-pipenv)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Contact](#contact)

## Setup

### Using `requirements.txt`

For a classic installation, the file [`requirements.txt`](requirements.txt) is provided.

1. Clone the repository:
    ```sh
    git clone https://github.com/danielfeitopin/mqtwister.git
    cd mqtwister
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

> [!NOTE]
> On Windows run `.venv\Scripts\activate` instead of `source .venv/bin/activate`.

### Using `Pipenv`

For added convenience, the files [`Pipfile`](Pipfile) and [`Pipfile.lock`](Pipfile.lock) are also provided.

1. Clone the repository:
    ```sh
    git clone https://github.com/danielfeitopin/mqtwister.git
    cd mqtwister
    ```

2. Install dependencies:
    ```sh
    pipenv install
    ```

## Usage

1. Configure the tool by editing the [`mqtwister/config.py`](mqtwister/config.py) file:

    ```python
    INTERFACE_NAME = '' # E.g. 'eth0' (Debian), 'Ethernet' (Windows), 'Wi-Fi' (Windows)
    TARGET_IP = ''
    ```

<!-- 1. Use `etterfilter` to compile the filter script:

    ```sh
    etterfilter filter.ecf -o filter.ef
    ``` -->

2. Run the tool using the package as a module:

    ```sh
    python -m mqtwister
    ```

> [!IMPORTANT]
> - Be sure to execute the command inside the virtual environment (if used).
> - Ensure you have the necessary permissions to run network sniffing tools.

> [!TIP]
>
> There is a useful function in [`mqtwister/utils/network.py`](mqtwister/utils/network.py) to get a list of the available network interfaces: `get_interfaces()`.
>
> ```sh
> python -c "import mqtwister.utils.network as net; print(net.get_interfaces())"
> ```

## Contributing

Contributions are welcome! If you have improvements, or bug fixes, feel free to submit a pull request.

## Contact

Feel free to get in touch with me!

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-%23181717?style=for-the-badge&logo=github&logoColor=%23181717&color=white)](<https://github.com/danielfeitopin>)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-white?style=for-the-badge&logo=linkedin&logoColor=white&color=%230A66C2)](<https://www.linkedin.com/in/danielfeitopin/>)

</div>
