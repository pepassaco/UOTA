## qso_dump

#### Uso: 

eQSL:

```
python3 qso_dump.py -i CALLSIGN -c PASSWORD -qsl 0 (optional: --fecha YYYY)
```

LoTW:

```
python3 qso_dump.py -i CALLSIGN -c PASSWORD -qsl 1 (optional: --fecha YYYY)
```

## checkAward.py




## generaAward


### assets folder structure

.
└── assets/
    ├── permanent_awards/
    │   ├── 0/ (category nº 0)
    │   │   ├── 0.pdf (firstQSL)
    │   │   ├── 1.pdf (bronze)
    │   │   ├── 2.pdf (silver)
    │   │   ├── 3.pdf (gold)
    │   │   └── ...
    │   ├── 1/ (category nº 1)
    │   │   ├── 0.pdf (firstQSL)
    │   │   ├── 1.pdf (bronze)
    │   │   ├── 2.pdf (...)
    │   │   ├── 3.pdf
    │   │   └── ...
    │   └── ...
    └── leaderboards/
        ├── 0/ (category nº 0)
        │   ├── 0.pdf
        │   ├── 1.pdf
        │   ├── 2.pdf
        │   ├── 3.pdf
        │   └── ...
        ├── 1/ (category nº 1)
        │   ├── 0.pdf
        │   ├── 1.pdf
        │   ├── 2.pdf
        │   ├── 3.pdf
        │   └── ...
        └── ...




