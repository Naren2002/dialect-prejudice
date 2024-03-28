#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

for variable in groenwold_mini
do
    python3 -u ../probing/mgp_gpt3_v2.py \
    --model gpt-3.5-turbo \
    --variable $variable \
    --attribute occupations_mini_ultra
done
