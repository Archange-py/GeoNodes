bl_info = {
    "name": "Pavage",
    "author": "Solange <archange_paradise@proton.me>",
    "version": (0, 1, 0),
    "blender": (4, 5, 0),
    "description": "Automatically loads node groups from an included .blend file",
    "category": "Geometry",
}

import bpy
import os

# Name of the .blend file in the add-on's assets folder
ASSETS_BLEND = os.path.join(os.path.dirname(__file__), "assets", "pavage.blend")

print(ASSETS_BLEND)

def load_all_node_groups_from_blend():
    """Loads all node groups contained in the .blend file."""
    if not os.path.exists(ASSETS_BLEND):
        print(f"[GeoNodes Loader] File not found : {ASSETS_BLEND}")
        return
    
    with bpy.data.libraries.load(ASSETS_BLEND, link=False) as (data_from, data_to): # type: ignore
        if not data_from.node_groups:
            print("[GeoNodes Loader] No node group found in the .blend file..")
            return

        data_to.node_groups = data_from.node_groups
        print(f"[GeoNodes Loader] Loaded node groups : {data_from.node_groups}")

def register():
    load_all_node_groups_from_blend()

def unregister():
    pass

if __name__ == "__main__":
    register()
