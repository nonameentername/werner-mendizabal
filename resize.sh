#!/bin/bash

if [[ -z $1 ]]; then
    echo "Usage: $0 <name>"
    exit 0
fi

name=$1

gm convert content/images/$name.jpg -resize '840x' -gravity center -crop 840x341+0+0 +repage content/images/small/$name.jpg
gm convert content/images/$name.jpg -resize '351x' -gravity center -crop 351x176+0+0 +repage content/images/mini/$name.jpg
gm convert content/images/$name.jpg -resize '102x' -gravity center -crop 51x51+0+0 +repage content/images/icon/$name.jpg

gthumb content/images/small/$name.jpg content/images/mini/$name.jpg content/images/icon/$name.jpg
