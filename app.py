import os
import shutil
import xml.etree.ElementTree as ET
from rich.console import Console
from rich.table import Table

prefab_files = []
dungeon_skip_template = [
    "BACKDROP",
    "MASTER"
]

console = Console()

def main():
    albion_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Albion Online\game\Albion-Online_Data\StreamingAssets\GameData\templates\GREEN"
    second_folder_archiv = r"C:\Program Files (x86)\Steam\steamapps\common\Albion Online\game\Albion-Online_Data\StreamingAssets\GameData\templates\GREEN\NewFolder"

    if not os.path.exists(second_folder_archiv):
        os.makedirs(second_folder_archiv)

    files = [f for f in os.listdir("Template") if os.path.isfile(os.path.join("Template", f))]

    for file in files:
        try:
            new_file = file.replace(".xml", ".bin")
            shutil.move(os.path.join(albion_dir, new_file), os.path.join(second_folder_archiv, new_file))
        except IOError as e:
            prefab_files.append(file)

    for file in files:
        try:
            new_file = file.replace(".xml", ".bin")
            shutil.move(os.path.join(second_folder_archiv, new_file), os.path.join(albion_dir, new_file))
        except IOError as e:
            pass

    check_chest()

def check_chest():
    files = [f for f in os.listdir("Template") if f.endswith(".xml")]
    special_boss = []
    flag7 = False
    chest_and_boss_list = []

    for template in prefab_files:
        if "Uncle" in template:
            special_boss.append("[red]Uncle Frost[/] [blue]( Blue Chest )[/]")

        if "Anniversary" in template:
            special_boss.append("[yellow]Anniversary Titan Boss[/]")

        if not any(skip_template in template for skip_template in dungeon_skip_template):
            if "EXIT" in template:
                flag7 = True

            try:
                file_info = next((f for f in files if template in f), None)
                tree = ET.parse(os.path.join("Template", file_info))
                root = tree.getroot()

                layer_nodes = root.findall(".//layer")
                chest_types = []

                for layer_node in layer_nodes:
                    if "reward_solo" in layer_node.attrib['name'].lower():
                        tile_nodes = layer_node.findall(".//tile")
                        chest_types = [tile.attrib['name'] for tile in tile_nodes]
                        break

                if chest_types:
                    chest_and_boss_list.append(f"({' , '.join(chest_types)})")
            except Exception as e:
                console.print(f"Error : {e}", style="red")

    chest_and_boss_str = ', '.join(chest_and_boss_list)
    console.print("")

    if special_boss:
        special_boss_str = ', '.join(special_boss)
        console.print(f"[blue]   Event Boss      :[/]   {special_boss_str}")

    if not chest_and_boss_list:
        chest_and_boss_str = "[red]No Boss and Chests[/]"

    console.print(f"[blue]   Chest Possibility : [/]   {chest_and_boss_str}")
    console.print("   ")
    console.print("[blue]   Floor           :[/]   Go to Next Floor" if flag7 else "   [blue]   Floor           :[/]   End of Dungeon")

    input()

if __name__ == "__main__":
    main()
