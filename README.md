# TLS States
Code for experimenting with TLS 1.3 client and server state machines.

## Prerequisites
To run the TLS 1.3 state simulation, you'll need the Python package [transitions](https://github.com/pytransitions/transitions). The package can be installed with:
```bash
pip install transitions
```

To prevent your Python environment from becoming poluted over time, especially if you need different versions of a Python package for different projects, you should use [Python 3 virtual environments](https://docs.python.org/3/library/venv.html). As an example, to create a new environment called `tls` in `~/Temp`:
```bash
python -m venv ~/Temp/tls
``` 

You can now install Python packages in `tls` environment without poluting the standard Python installation. To activate `tls` next time, go to `~/Temp` and do:
```bash
source ~/Temp/tls/bin/active
```

## How to Interpret the Output
* The active TLS 1.3 client or TLS 1.3 server state is denoted by the symbol &#x25CB;
* What triggers a state transition or occurs during the state transition is denoted by &#x2192;  
