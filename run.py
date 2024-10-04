import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(path:str):
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=-1, kernel_name='python3')
    ep.allow_errors = True
    ep.preprocess(nb, {'metadata': {'path': './'}})

print("Ensure the correct conda environment is activated!")
run_notebook('art-station-scraper.ipynb')
run_notebook('art-station-to-df.ipynb')
run_notebook('art-station-to-download-images.ipynb')
run_notebook('art-station-to-df.ipynb') # again to update img paths