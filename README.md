# Albion Dungeon Scanner

This project, named Albion Dungeon Scanner, is a dungeon scanner developed in Python. It is inspired by the NJTools project, which was originally written in C#.

## Installation

Before starting the installation, make sure you have Python 3.10 or a later version installed on your system. Then, follow the steps below:

1. Install PDM by following the instructions available on [the official PDM website](https://pdm-project.org/latest/#recommended-installation-method).

2. Once PDM is installed, navigate to the project directory and download the contents of the [GREEN](https://github.com/ao-data/ao-bin-dumps/tree/master/templates/GREEN) folder from the [ao-bin-dumps](https://github.com/ao-data/ao-bin-dumps) repository. Create a folder named "Template" at the root of the Albion Dungeon Scanner project.

3. Run the following command to install the project dependencies:

   ```bash
   pdm install
    ```

4. After installation is complete, enter a dungeon and execute the following command to start the scanning process:

   ```bash
   pdm run scan
    ```
    If you change floors, you will need to rerun the command to update the information.

## Potential Improvements

- Automatic detection of dungeon entrances and floor changes through Photon events.
- Local extraction of binaries to XML format.

## Disclaimer

This code is purely for fun, and I am aware that it might not be the best-written code. If someone messes up with this code, I cannot be held responsible for any consequences.

## License

This project is licensed under the MIT License - see the LICENSE file for details