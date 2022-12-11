import shutil

from pathlib import Path

from config import steam, env, files, project

tools_dir = steam.COMPAT_TOOLS / project.NAME
link_file = tools_dir / project.SCRIPT_NAME

def add(file: Path = None):

    if not steam.SHARE_ROOT.exists():
        raise FileNotFoundError(f'Steam Home Dir \'{steam.SHARE_ROOT}\' not found!"')
    
    steam.COMPAT_TOOLS.mkdir(exist_ok=True)

    stl_bin = _get_stl_bin(file)

    if not tools_dir.exists():

        try:
            tools_dir.mkdir()
        except:
            print(f'Failed to create the directory \'{tools_dir}\' - check your write privileges on \'{steam.COMPAT_TOOLS}\'')
            raise
        
        (tools_dir / 'compatibilitytool.vdf').write_text(_compat_tools_vdf_text())
        (tools_dir / 'toolmanifest.vdf')     .write_text(_tool_manifest_vdf_text())

        link_file.symlink_to(stl_bin)

    else:
        
        if link_file.resolve() != stl_bin:

            link_file.unlink(missing_ok = True)
            link_file.symlink_to(stl_bin)

def delete():
    link_file.unlink(missing_ok = True)
    shutil.rmtree(str(tools_dir))

# TODO:
def check():
    pass

def _get_stl_bin(file: Path | None):
    if env.check_on_steam_deck():
        stl_bin = file or (files.USR_DIR / project.SCRIPT_NAME)
    else:
        stl_bin = project.SCRIPT_DIR / project.SCRIPT_NAME
    
    return stl_bin.resolve()

def _compat_tools_vdf_text():
    vdf_text = '\n'.join([
        '"compatibilitytools"',
        '{{',
        '  "compat_tools"',
        '  {{',
        '    "Proton-{STL_NAME}" // Internal name of this tool',
        '    {{',
        '      "install_path" "."',
        '      "display_name" "{DISPLAY_NAME}"',
        '',
        '      "from_oslist"  "windows"',
        '      "to_oslist"    "linux"',
        '    }}',
        '  }}',
        '}}',
    ])

    return vdf_text.format(
        STL_NAME     = project.STL_NAME,
        DISPLAY_NAME = project.DISPLAY_NAME
    )

def _tool_manifest_vdf_text():
    vdf_text = '\n'.join([
        '"manifest"',
        '{{',
        '  "commandline" "/{SCRIPT_NAME} run"',
        '  "commandline_{WFEAR}" "/{SCRIPT_NAME} {WFEAR}"',
        '}}',
    ])

    return vdf_text.format(
        SCRIPT_NAME = project.SCRIPT_NAME,
        WFEAR       = project.WAIT_FOR_EXIT_AND_RUN
    )
