import shutil

from pathlib import Path

from config import shm, project, env, files, steam
import utils
import compat_tool

def main():

    init_shm_stl()
    restore_gtk_css()
    delete_old_logs()
    set_flatpak()

    # compat_tool.add()



def init_shm_stl():
    shm.STL_SHM.mkdir(exist_ok=True, parents=True)

    if not shm.VERSION_FILE.exists():
        shm.VERSION_FILE.touch()
    
    shm_version = shm.VERSION_FILE.read_text().strip()

    # make backup of old config
    if shm_version != project.VERSION:

        if shm.STL_SHM_BAK.exists():
            shutil.rmtree(shm.STL_SHM_BAK)
        
        shm.STL_SHM.rename(shm.STL_SHM_BAK)
        shm.STL_SHM.mkdir()

        shm.VERSION_FILE.write_text(project.VERSION)

def restore_gtk_css():
    if env.check_on_steam_deck():
        file     = Path.home() / '.config/gtk-3.0/gtk.css'
        file_bak = utils.subscript(file, '.original')

        if file_bak.exists():

            # writelog "INFO" "${FUNCNAME[0]} - recovering original gtk.css from '${GTKCSSFILE}_ORIGNAL'"
            
            file.unlink()
            file_bak.rename(file)

#TODO: use an official logging library
def delete_old_logs():
    pass

def set_flatpak():
    if env.check_flatpak():
        # writelog "INFO" "${FUNCNAME[0]} - seems like flatpak is used, because variable 'FLATPAK_ID' exists and points to 'com.valvesoftware.Steam'"
        
        compat_tool.add(files.FLATPAK_BIN / project.SCRIPT_NAME)

if __name__ == '__main__':
    main()