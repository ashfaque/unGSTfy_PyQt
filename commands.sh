#!/bin/bash

### Importing custom commands specified in the file.
source "$PWD/aliases.sh"    # Write: USERNAME="USERNAME_HERE"
# . "$PWD/aliases.sh"


### Custom commands
export gitpush=$(echo -e "git add --all && git commit -m 'updated' && git pull origin HEAD && git push origin HEAD")
export designer=$(echo -e 'C:/Users/${USERNAME}/.conda/envs/gstenv/Lib/site-packages/qt6_applications/Qt/bin/designer.exe &')    # macOS: Users/USERNAME/miniconda3/envs/gstenv/lib/python3.11/site-packages/qt6_applications/Qt/bin/Designer.app
export ui2py=$(echo -e 'pyuic6 -x _ui_archives/untitled.ui -o _ui_archives/untitled.py')    # * Just save .ui file in ui/ dir of this project and run this command in the terminal.
export py2exe=$(echo -e 'pyinstaller --noconfirm --onefile --windowed --clean --name "unGSTfy" --icon "assets/icons/gst_logo.ico" --log-level "INFO" --add-data "assets;assets/" main.py')    # ? --add-data "assets;assets/" for macos and install Pillow to auto convert .ico files to .icns files.
export py2direxe=$(echo -e 'pyinstaller --noconfirm --onedir --windowed --clean --name "unGSTfy" --icon "assets/icons/gst_logo.ico" --log-level "INFO" --add-data "assets;assets/" main.py')    # ? --add-data "assets;assets/" for macos and install Pillow to auto convert .ico files to .icns files.
export py2debugexe=$(echo -e 'pyinstaller --noconfirm --onedir --console --clean --name "unGSTfy" --icon "assets/icons/gst_logo.ico" --log-level "INFO" --add-data "assets;assets/"  main.py')    # ? --add-data "assets;assets/" for macos and install Pillow to auto convert .ico files to .icns files.
export clean=$(echo -e 'rm -rf unGSTfy.spec build dist')

#######################################################################################################

### Main script logic
# if [[ "$PWD" == "/path/to/specific/directory" ]]; then

    if [ -n "$1" ]; then             # $1 is the 1st argument passed to this script. eg., `./commands.sh lah`
        command=$(eval "echo \$$1")

        if [ -n "$command" ]; then
            eval "$command"          # Finally, eval is used to evaluate and execute the command stored in the command variable
        else
            echo "Custom command not found: $1"
        fi
    else
        echo "Command not provided as argument in the script."
    fi

# else
#   echo "Command not allowed in this directory path: $PWD"
# fi
