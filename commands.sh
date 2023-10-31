#!/bin/bash

### Importing custom commands specified in the file.
source "$PWD/aliases.sh"    # Write: USERNAME="USERNAME_HERE"
# . "$PWD/aliases.sh"


### Custom commands
export gitpush=$(echo -e "git add --all && git commit -m 'updated' && git pull origin HEAD && git push origin HEAD")
export designer=$(echo -e 'C:/Users/${USERNAME}/.conda/envs/gstenv/Lib/site-packages/qt6_applications/Qt/bin/designer.exe &')
export ui2py=$(echo -e 'pyuic6 -x _ui_archives/untitled.ui -o _ui_archives/untitled.py')    # * Just save .ui file in ui/ dir of this project and run this command in the terminal.
export py2exe=$(echo -e 'pyinstaller --name=unGSTfy --noconfirm --onefile --windowed --icon=assets/icons/gst_logo.ico main.py')


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
