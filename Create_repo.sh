#! /bin/sh

function prepare_repo() {
    blih -u antoine.dabin@epitech.eu repository create "$1"
    blih -u antoine.dabin@epitech.eu repository setacl "$1" ramassage-tek r
    git clone git@git.epitech.eu:/antoine.dabin@epitech.eu/"$1"

    echo "What do you want to do ?"
    echo "1: CSFML"
    echo "2: PSU/CPE"
    echo "3: exit"

    until [[ $MENU_OPTION =~ ^[1-4]$ ]];do
        read -rp "Select an option [1-4]:" MENU_OPTION
    done
    case $MENU_OPTION in
    1)
        csfml "$1"
        ;;
    2)
        other "$1"
        ;;
    3)
        exit 0
        ;;
    esac
}

function csfml() {
    cp wait/base/csfml/Makefile "$1"
    cp wait/base/main.c "$1"
}

function other() {
    cp wait/base/main.c "$1"
    mkdir "$1"/lib
    mkdir "$1"/lib/my
    mkdir "$1"/lib/my/include
    cp wait/base/PSU_CPE/Makefile "$1"
    cp wait/base/lib/my/*.c "$1"/lib/my
    cp wait/base/lib/my/include/* "$1"/lib/my/include
}

function add_user() {
    blih -u antoine.dabin@epitech.eu repository setacl "$1" "$2"@epitech.eu "$3"
}

function usage() {
    echo "Si repo non existant"
    echo "./prepare_my_repo.sh nom_repo"
    echo "Pour ajouter droits"
    echo "./prepare_my_repo.sh nom_repo login_user rights"
}

function main() {
    if [[ -z "$1" ]];then
        usage
        exit 1
    fi

    if [[ -n "$1" && -z "$2" ]];then
        prepare_repo "$1" "$2"
    fi

    if [[ -n $2 && -n "$3" ]];then
        add_user "$1" "$2" "$3"
    fi
}

main "$1" "$2" "$3"
