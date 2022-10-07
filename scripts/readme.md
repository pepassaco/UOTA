## qso_dump

#### About: 

Calls wither the eQSL or LoTW APIs, retrieves the QSL logs, selects the entries in which the QSO CALLSIGN corresponds to an university taking place in the UOTA, checks whether it is a new entry that was not alredy in the database and, if it is, it is sent to the UOTA API.

#### Usage: 

eQSL:

```
python3 qso_dump.py -i CALLSIGN -c PASSWORD -qsl 0 (optional: --fecha YYYY)
```

LoTW:

```
python3 qso_dump.py -i CALLSIGN -c PASSWORD -qsl 1 (optional: --fecha YYYY)
```








## checkAward.py

#### About: 

For an specified callsign, retrieves the log with universities in the UOTA program from the UOTA API, checks one by one whether the conditions to get any award are fullfilled and, sends to the API a boolean array with the awards that have been obtained.

#### Usage: 

```
python3 checkAward.py -i CALLSIGN
```







## generaAward

#### About: 

Given the promary key of an awarded award and a callsign, accesses the UOTA API to retrieve the detais of such award and generates the corresponding PDF file.

#### Usage: 
```
python3 generaAward.py -i CALLSIGN -d AWARD_NUMBER
```

AWARD_NUMBER is intended to be the primary key (an ID integer) of the specific entry in the database corresponding to the award to be generated.


## Assets folder structure

```
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

```


