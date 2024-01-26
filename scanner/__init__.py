import glob
import os
import shutil
import xml.etree.ElementTree as ET

from rich.console import Console

from scanner.utils.binary import Binary
from scanner.utils.config import Config


class AlbionDungeonScanner:
    def __init__(self) -> None:
        self.config = Config
        self.console = Console()
        self.used_files = []

    @property
    def albion_dir(self):
        if self.config.get("ao-dir"):
            return (
                self.config.get("ao-dir")
                + r"Albion-Online_Data\StreamingAssets\GameData\templates\GREEN"
            )

        raise "You must enter the path to your game in the .env file."

    def check_file(self, file_path):
        filename = os.path.basename(file_path)

        try:
            shutil.move(
                os.path.join(self.albion_dir, filename),
                os.path.join(self.albion_dir + "\\.temp\\", filename),
            )
        except IOError:
            self.used_files.append(file_path)

    def restore_file(self, file_path):
        filename = os.path.basename(file_path)

        try:
            shutil.move(
                os.path.join(self.albion_dir + "\\.temp\\", filename),
                os.path.join(self.albion_dir, filename),
            )
        except Exception:
            pass

    def run(self):
        temp_path = self.albion_dir + "\\.temp\\"
        if os.path.exists(temp_path):
            shutil.rmtree(temp_path)
        os.mkdir(temp_path)

        files = glob.glob(os.path.join(self.albion_dir, "*.bin"))

        for file in files:
            self.check_file(file)
            self.restore_file(file)

        special_boss = []
        chest_and_boss_list = []
        flag7 = False
        for file in self.used_files:
            filename = os.path.basename(file)

            if "Uncle" in filename:
                special_boss.append("[red]Uncle Frost[/] [blue]( Blue Chest )[/]")

            if "Anniversary" in file:
                special_boss.append("[yellow]Anniversary Titan Boss[/]")

            if not any(
                skip_template in filename for skip_template in ["BACKDROP", "MASTER"]
            ):
                if "EXIT" in filename:
                    flag7 = True

                try:
                    binary = Binary()
                    decrypted_bytes = binary.decrypter.decrypt_binary_file(file)
                    decrypted_str = decrypted_bytes.decode("utf-8")

                    root = ET.fromstring(decrypted_str)

                    layer_nodes = root.findall(".//layer")
                    chest_types = []

                    for layer_node in layer_nodes:
                        if "reward_solo" in layer_node.attrib["name"].lower():
                            tile_nodes = layer_node.findall(".//tile")
                            chest_types = [tile.attrib["name"] for tile in tile_nodes]
                            break

                    if chest_types:
                        chest_and_boss_list.append(f"({' , '.join(chest_types)})")
                except Exception as e:
                    print(e)
                    pass

        chest_and_boss_str = ", ".join(chest_and_boss_list)
        if special_boss:
            special_boss_str = ", ".join(special_boss)
            self.console.print(f"[blue]   Event Boss      :[/]   {special_boss_str}")

        if not chest_and_boss_list:
            chest_and_boss_str = "[red]No Boss and Chests[/]"

        self.console.print(f"[blue]   Chest Possibility : [/]   {chest_and_boss_str}")
        self.console.print("   ")
        self.console.print(
            "[blue]   Floor           :[/]   Go to Next Floor"
            if flag7
            else "   [blue]   Floor           :[/]   End of Dungeon"
        )


def main():
    scanner = AlbionDungeonScanner()
    scanner.run()
