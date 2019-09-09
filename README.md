SMART-Q
================
### Introduction

Single molecular FISH (smFISH) experiments, such as RNAscope is critical for analyzing gene expression at the single-cell level. Although smFISH has become a popular tool for studying gene regulation in complex primary and tissue samples, the development of an efficient analysis tool is still lacking. Here we present SMART-Q, Single-Molecule Automatic RNA Transcription Quantification.

SMART-Q is a modular and customizable pipeline processing single molecule FISH data with much-improved efficiency and accuracy compared to the existing methods. It has new features that allow analyzing immunostaining signals and FISH signals simultaneously to achieve cell type-specific transcription analysis. SMART-Q is an efficient analysis tool for studying gene expression patterns in complex tissue and primary cell samples. 

For more detailed instructions about the pipeline, please see the SMART-Q Manual.docx.

### Installation

SMART-Q was written based on Python 3.7 and adapted from starfish. Some functions might not work in earlier versions, especially in Python 2. 

If you have not already installed Python 3.7, I recommend doing so using miniconda3, which you can download from this link. Once completed, create an environment for installments of SMART-Q, using the code below.

``` bash
conda create -n SMART-Q
y
conda activate SMART-Q # if this doesn’t work, then use source activate SMART-Q
conda install -c conda-forge openjdk=8 pyimagej
y
```

Next, download SMART-Q from github and install locally.

``` bash
git clone https://github.com/shenlab-ucsf/SMART-Q
cd SMART-Q
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

If you are using a Mac, then use the following two lines. Otherwise, there may be issues with matplotlib, the visualization installment used by Python.

``` bash
mkdir ~/.matplotlib
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```

Install the rest of the dependencies (IPython, tabulate, XlsxWrite, etc.) using pip.

``` bash
pip install ipython==7.1.1
pip install tabulate==0.8.3
pip install XlsxWriter==1.1.4
pip install xlrd==1.2.0
pip install cython==0.29.7
pip install pyimagej==0.4.0
pip install opencv-python==4.1.0.25
```

To know if the installation has worked, then use the template IPython file (.ipynb) provided by SMART-Q. In your command line, navigate to SMART-Q/pipeline_template, use the code below to open jupyter-notebook, then click on the .ipynb file.

``` bash
jupyter-notebook
```

Run only the first cell of the script by pressing Shift+Enter on your keyboard or by clicking Run. If no errors show up, then the installation was successful. If you experience issues while troubleshooting any errors in the installation, reach out to seth.bergenholtz@gmail.com for help.

Once this is finished, in order to make sure that the correct version of Python is used to run SMART-Q every time you open a new session of bash, replace your own file path into the example code below and run it.

``` bash
export PATH=/Users/sethb/SMART-Q/.venv/bin:$PATH
```

You may also add the below code to the file called ~/.bash_profile so that you do not have run the above code below every time you open a new bash session, but be aware that if you want to use a different version of Python afterward, then you will have to comment this line out or delete it from ~/.bash_profile
``` bash
echo "export PATH=/Users/sethb/SMART-Q/.venv/bin:$PATH" >> ~/.bash_profile
```

Finally, if you do not already have Fiji, download it from https://imagej.net/Fiji/Downloads.
