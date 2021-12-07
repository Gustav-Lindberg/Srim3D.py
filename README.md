# Srim3D.py
Srim3D.py is a Python script containing a set of functions that make it easier to work with [SRIM](http://srim.org/)'s 3D ionization output. This output can be generated in TRIM by clicking on the "F" button next to "Ionization 3D":

![](https://i.stack.imgur.com/yqVsJ.png)

# Setup
To start using srim3d.py, download [this file](https://raw.githubusercontent.com/Gustav-Lindberg/Srim3D.py/main/srim3d.py) and save it in the same folder as your Python code. Then add this line to the beginning of your Python code:

```
import srim3d
```

If you want it to be available for all projects, you can also save the file in the folder containing Python libraries. On Windows with Anaconda 3 this is `C:\ProgramData\Anaconda3\Lib`, and on Linux with Python 3.8 this is `/usr/lib/python3.8`.

# Usage
## `extractData(file="Ioniz-3D.txt")`
This function takes as parameter the name and path of SRIM's 3D output file, and returns a numpy array with the data. If the parameter isn't specified, it looks for a file named `Ioniz-3D.txt` in the same folder as the script.

## `ions(data)`
This function takes as parameter the numpy matrix returned by the `extractData` and returns a numpy vector with the deposited energy only as a function of depth (so summing up over all transverse positions at a given depth).

## `transverseIons(data)`
This function takes as parameter the numpy matrix returned by the `extractData` and returns a numpy vector with the deposited energy only as a function of transverse position (so summing up over all depths at a given transverse position).
