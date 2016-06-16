#!/bin/bash
cd $(pwd)
for i in `ls | grep Gene_Symbol.txt`; do
  #echo ${i}
  python convert_gene_list.py ${i};
done
