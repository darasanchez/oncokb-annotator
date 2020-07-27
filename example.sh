#!/usr/bin/env bash
IMAF="data/example_maf.txt"
OMAF="data/example_maf.oncokb.txt"
IF="data/example_fusions.txt"
OF="data/example_fusions.oncokb.txt"
ICNA="data/example_cna.txt"
OCNA="data/example_cna.oncokb.txt"
IC="data/example_clinical.txt"
OC="data/example_clinical.oncokb.txt"
OCPDF="data/example_clinical.oncokb.pdf"
TOKEN="8df5939f-ecbf-4c8b-81a8-60490cdf64b0" #OncoKB API Token
README="data/example_README.txt"
python3 MafAnnotator.py -i $IMAF -o $OMAF -c $IC -b $TOKEN
python3 FusionAnnotator.py -i $IF -o $OF -c $IC -b $TOKEN
python3 CnaAnnotator.py -i $ICNA -o $OCNA -c $IC -b $TOKEN
python3 ClinicalDataAnnotator.py -i $IC -o $OC -a $OMAF,$OCNA,$OF
python3 OncoKBPlots.py -i $OC -o $OCPDF -c ONCOTREE_CODE #-n 10
python3 GenerateReadMe.py -o $README
