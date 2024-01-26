# Albion Dungeon Scanner

This project, named Albion Dungeon Scanner, is a dungeon scanner developed in Python. It is inspired by the NJTools project, which was originally written in C#.

## Installation

Before starting the installation, make sure you have Python 3.10 or a later version installed on your system. Then, follow the steps below:

1. Install PDM by following the instructions available on [the official PDM website](https://pdm-project.org/latest/#recommended-installation-method).

2. Run the following command in the root of the albion-dungeon-scanner folder to install the project's dependencies:

   ```bash
   pdm install
    ```

3. Rename the .env.base file to .env and fill in the necessary information.

    For example **`ao-dir`** is the path to your game, here is an example:

    ```yaml
    "ao-dir": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Albion Online\\game\\" 
    ```


4. After installation is complete, enter a dungeon and execute the following command in the root of the albion-dungeon-scanner folder to start the scanning process:

   ```bash
   pdm run scan
    ```
    If you change floors, you will need to rerun the command to update the information.

## Potential Improvements

- Automatic detection of dungeon entrances and floor changes through Photon events.
- ~~Local extraction of binaries to XML format.~~ Done

## Disclaimer

If someone messes up with this code, I cannot be held responsible for any consequences.

## License

This project is licensed under the MIT License - see the LICENSE file for details
