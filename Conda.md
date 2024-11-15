# Some useful notes and commend to copy for conda

## sourse environment (if install not under `~`)
```
source /path/to/miniconda3/bin/activate
conda init --all
conda config --set auto_activate_base false
```

## create from file 
```
conda create -f environment.yml
```

## export clean environment with pip
```
conda update pip 
conda export --from-history > environment.yml
```

`update pip` let conda konw what pips are installed. `--from-history` packages only manually installed, so it's much cleaner. 

> The above method somehow failed if `pip` is not installed by `conda`, use pip freeze to export pip requirements
```
pip freeze > requirements.txt
```