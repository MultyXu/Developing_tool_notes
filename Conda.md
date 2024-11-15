# Some useful notes and commend to copy for conda

## course environment (if install not under `~`)
```
source /path/to/miniconda3/bin/activate
conda init --all
```

> The above method somehow failed if `pip` is not installed by `conda`, use pip freeze to export pip requirements
```
pip freeze > requirements.txt
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

