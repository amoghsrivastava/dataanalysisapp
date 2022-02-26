# Coursework 2 - Data Analysis App in Python
This coursework is a part of the F20SC course.

### Overview
The app is developed in Python 3.8 scripting language. The packages used in the app are
- tkinter
- pandas
- numpy
- orjson
- matplotlib

All packages can be installed using the commands from the installation section [Go to Installation](###Installation)


### Prerequisites
While in the root folder, run the command line and type the command. This will install all packages necessary to run the app.
```bash
pip install requirements.txt
```

### Starting the CLI

Enter the following command to start using the command-line-interface
```bash
python cw2.py -h
```
You should get this sort of output. You can now use the commands to run the app. [View command examples](### Examples)
```bash
usage: cw2.py [-h] [-u] [-d] -t  -f

Python Data Analysis App

optional arguments:
  -h, --help      show this help message and exit
  -u , --userid   A visitor/reader UUID
  -d , --docid    A document UUID
  -t , --task     The task you want to run
  -f , --file     The path of the JSON file with the data to be analysed

A simple data intensive python app built for F20SC Coursework 2

(venv) C:\Users\amogh\Desktop\F20SC\DataAnalysisApp>python cw2 -h
C:\Python38\python.exe: can't open file 'cw2': [Errno 2] No such file or directory

(venv) C:\Users\amogh\Desktop\F20SC\DataAnalysisApp>python cw2.py -h
usage: cw2.py [-h] [-u] [-d] -t  -f

Python Data Analysis App

optional arguments:
  -h, --help      show this help message and exit
  -u , --userid   A visitor/reader UUID
  -d , --docid    A document UUID
  -t , --task     The task you want to run
  -f , --file     The path of the JSON file with the data to be analysed

A simple data intensive python app built for F20SC Coursework 2

```


If you're using a virtual environment, use the same command but without python.
```bash
cw2.py -h
```

### Starting GUI
To start GUI, from the command line in the root directory of the app, type
```bash
python app.py
```

### Examples

To run any task, just write the ```-d``` flag followed by the document ID, ```-t``` followed 
by the task ID, and ```-f``` followed by the file path.

For example, to run task 2a,
```bash
python cw2.py -d aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe -t 2a -f "C:\Users\amogh\PycharmProjects\dataAnalysis\data\sample_100k_lines.json"
```

### Testing

To run the tests, in the tests.py file, change the path value of the following path variables.

##### In TestFileManager class:
```python
path_10 = ... #Path for 10K dataset
```

##### In TestDataProcessing class:
```python
path_100 = ... #Path for 100k dataset
path_600 = ... #Path for 600k dataset
```

### Questions
Reach out to me on teams (as348) Amogh or send me an email here [as348@hw.ac.uk](mailto:as348@hw.ac.uk) in the case
of any trouble running the tasks.

