#!/bin/bash

if [ $1 -eq 2 ]
then
  python2 ~/Desktop/vistrans/vistrans -s ~/Desktop/vistrans/test/sample_inputs/trial.species.newick.txt -S ~/Desktop/vistrans/test/sample_inputs/trial.smap.txt -b ~/Desktop/vistrans/test/sample_inputs/trial.brecon -t ~/Desktop/vistrans/test/sample_inputs/trial.genes.newick.txt --output ~/Desktop/vistrans/test/tree.svg
fi

if [ $1 -eq 3 ]
then
  python3 ~/Desktop/vistrans/vistrans -s ~/Desktop/vistrans/test/sample_inputs/trial.species.newick.txt -S ~/Desktop/vistrans/test/sample_inputs/trial.smap.txt -b ~/Desktop/vistrans/test/sample_inputs/trial.brecon -t ~/Desktop/vistrans/test/sample_inputs/trial.genes.newick.txt --output ~/Desktop/vistrans/test/tree.svg
fi

