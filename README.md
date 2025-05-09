# MQTwister

<div align="center">

***A Tool for Man-in-the-Middle (MitM) Attacks on the MQTT Protocol.***

[![Python](https://img.shields.io/badge/Python-black?logo=python&logoColor=white&labelColor=grey&color=%233776AB)](<#> "Python")
[![License](<https://img.shields.io/github/license/danielfeitopin/mqtwister>)](<LICENSE> "License")
[![GitHub issues](https://img.shields.io/github/issues/danielfeitopin/mqtwister)](<https://github.com/danielfeitopin/mqtwister> "Issues")

[![GitHub stars](https://img.shields.io/github/stars/danielfeitopin/mqtwister)](<https://github.com/danielfeitopin/mqtwister/stargazers> "Stars")
[![GitHub watchers](https://img.shields.io/github/watchers/danielfeitopin/mqtwister)](<https://github.com/danielfeitopin/mqtwister/watchers> "Watchers")
[![GitHub forks](https://img.shields.io/github/forks/danielfeitopin/mqtwister)](<https://github.com/danielfeitopin/mqtwister/forks> "Forks")

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
  - [License](#license)
  - [Contributing](#contributing)
  - [Support this project](#support-this-project)
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

## License

📃 This project is licensed under the [GNU General Public License version 2](<https://opensource.org/license/gpl-2-0>). A copy of this license can be found in the [LICENSE] file, and in the [LICENSES] folder.

<div align="center">

| Permissions      | Conditions                     | Limitations |
| ---------------- | ------------------------------ | ----------- |
| 🟢 Commercial use | 🔵 Disclose source              | 🔴 Liability |
| 🟢 Distribution   | 🔵 License and copyright notice | 🔴 Warranty  |
| 🟢 Modification   | 🔵 Same license                 |             |
| 🟢 Private use    | 🔵 State changes                |             |

_Table based on [choosealicense.com](<https://choosealicense.com/licenses/gpl-2.0/>)_

</div>

<details>
<summary>Why this license?</summary>

___

The initial intention was to license this project under the GNU General Public License version 3 (GPLv3) due to its enhanced legal protections, ethical considerations, and long-term sustainability. However, after reviewing the dependencies, it was determined that one of them is licensed under "GPLv2 only," which is incompatible with GPLv3. 

To ensure compliance and compatibility with all dependencies, the project is licensed under GPLv2. This decision aligns with the licensing terms of the included components while preserving the principles of open-source software. The permissive BSD-3-Clause-licensed components used in the project remain compatible with GPLv2, as their terms allow integration into projects under more restrictive copyleft licenses.

___

</details>

<details>
<summary>Used dependencies and their licenses</summary>

___

<div align="center">

|              Component               |                    License                     |
| :----------------------------------: | :--------------------------------------------: |
|  [![scapy_badge]][scapy_repository]  |  [![scapy_license_badge]][scapy_license_file]  |
| [![psutil_badge]][psutil_repository] | [![psutil_license_badge]][psutil_license_file] |

</div>

<!-- LINKS -->
[scapy_badge]: <https://img.shields.io/github/pipenv/locked/dependency-version/danielfeitopin/mqtwister/scapy>
[scapy_repository]: <https://github.com/secdev/scapy>
[scapy_license_badge]: <https://img.shields.io/github/license/secdev/scapy>
[scapy_license_file]: <https://github.com/secdev/scapy/blob/master/LICENSE>

[psutil_badge]: <https://img.shields.io/github/pipenv/locked/dependency-version/danielfeitopin/mqtwister/psutil>
[psutil_repository]: <https://github.com/giampaolo/psutil>
[psutil_license_badge]: <https://img.shields.io/github/license/giampaolo/psutil>
[psutil_license_file]: <https://github.com/giampaolo/psutil/blob/master/LICENSE>

___

</details>

## Contributing

🤝 Contributions are welcome! If you have improvements or bug fixes, feel free to submit a pull request.

❓ For support, please refer to the [SUPPORT] file for details on how to get help with this project.

📜 Please make sure to review the [CONTRIBUTING] guidelines and the [GOVERNANCE] document before getting started.

✅ By participating in this project, you agree to abide by our [Code of Conduct].

🔒 Security is a top priority for this project. If you discover any vulnerabilities or have concerns regarding the security of this tool, please report them responsibly by following the [SECURITY] guidelines.

## Support this project

⭐ If you find this project useful, please consider giving it a star on [GitHub][repository]. Your support helps to improve and maintain the project!

## Contact

📧 Feel free to get in touch with me!

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-%23181717?style=for-the-badge&logo=github&logoColor=%23181717&color=white)](<https://github.com/danielfeitopin>)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-white?style=for-the-badge&logo=linkedin&logoColor=white&color=%230A66C2)](<https://www.linkedin.com/in/danielfeitopin/>)

</div>

<!-- LINKS -->
[repository]: <https://github.com/danielfeitopin/mqtwister>
[SUPPORT]: <SUPPORT.md>
[CONTRIBUTING]: <CONTRIBUTING.md>
[GOVERNANCE]: <GOVERNANCE.md>
[Code of Conduct]: <CODE_OF_CONDUCT.md>
[SECURITY]: <SECURITY.md>
[LICENSE]: <LICENSE>
[LICENSES]: <./LICENSES/>
