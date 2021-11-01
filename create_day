#!/bin/sh

if [ $# != 1 ]; then
    echo "Usage: $(basename "$0") <day-number>" >&2
    exit 1
fi

if [ ! -d .git ]; then
    echo "must be run from root of advent-of-code repository" >&2
    exit 1
fi

name="$(printf "day%02d" "$1")"
mkdir "$name"

touch "$name"/input.txt
touch "$name"/testinput.txt
touch "$name"/main.py