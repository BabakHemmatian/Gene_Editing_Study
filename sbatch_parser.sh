#!/bin/bash

# Default resources are 1 core with 2.8GB of memory per core.

# job name:
#SBATCH -J Gene_Editing_Parse


# email error reports
#SBATCH --mail-user=noah_jones@brown.edu 
#SBATCH --mail-type=ALL

# output file
#SBATCH -J parsing
#SBATCH -o parsing-%j.out
#SBATCH -e parsing-%j.err
# %A is the job id (as you find it when searching for your running / finished jobs on the cluster)
# %a is the array id of your current array job


# Request runtime, memory, cores
#SBATCH --time=48:00:00
#SBATCH --mem=64G
#SBATCH -c 4
#SBATCH -N 1

eval "$(conda shell.bash hook)"
conda activate Gene_study

machine='ccv'

python Reddit_LDA_Analysis.py --machine $machine 
