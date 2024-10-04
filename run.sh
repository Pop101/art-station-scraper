#!/bin/bash

echo "Ensure the correct conda environment is activated!"

# Run each jpy notebook
jupyter nbconvert --to notebook --execute art-station-scraper.ipynb
jupyter nbconvert --to notebook --execute art-station-to-df.ipynb
jupyter nbconvert --to notebook --execute art-station-to-download-images.ipynb
jupyter nbconvert --to notebook --execute art-station-to-df.ipynb # again to update img paths