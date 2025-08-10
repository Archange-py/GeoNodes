import zipfile
import os, re


ADDON_FOLDER = "Pavage"

def get_addon_version():
    init_path = os.path.join(ADDON_FOLDER, "__init__.py")

    if not os.path.isfile(init_path):
        return "0.0.0"

    with open(init_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r'"version"\s*:\s*\((\d+),\s*(\d+),\s*(\d+)\)', content)

    return ".".join(match.groups()) if match else "0.0.0"

OUTPUT_ZIP = f"addons/{ADDON_FOLDER}-{get_addon_version()}.zip"

def zip_addon():
    if not os.path.isdir(ADDON_FOLDER):
        raise FileNotFoundError(f"Folder '{ADDON_FOLDER}' not found.")

    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(ADDON_FOLDER):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, start=os.path.dirname(ADDON_FOLDER))
                zipf.write(filepath, arcname)

    print(f"[✔️  ] Zipped add-on : {OUTPUT_ZIP}")


if __name__ == '__main__':
    zip_addon()
