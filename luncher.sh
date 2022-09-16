#!/bin/sh



x=0


for VARIABLE in ecommerce book calendar crypto email entrateinment events food games healt jobs music django lavarel angular react springboot akana express fastapi go phoenix flask ruby rails slim lumen symfony node expres graphql 
do
    python3 searcher.py $VARIABLE $x

    x=$((x+1))
done

python3 finder.py