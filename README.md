# Using Bluesky for social media analysis

This repository contains the software used for collecting and analyzing Dutch social media posts from the microblogging platform [Bluesky](https://bluesky.app). For more infomation see:

> Erik Tjong Kim Sang, "[Using Bluesky for Social Media Analysis](https://ifarm.nl/erikt/papers/DHBenelux_20251220.pdf)". Submitted to DHBenelux 2025, Amsterdam, The Netherlands, 20 December 2024

## Repository contents

* [notebooks/analyze_posts.ipynb](https://github.com/twinl/bsky/blob/main/notebooks/analyze_posts.ipynb) Jupyter notebook used for the analysis described in the paper
* [/scripts/crawler.py](https://github.com/twinl/bsky/blob/main/scripts/crawler.py) Python script used for collecting Dutch Bluesky posts (running every 5 minutes from cron)
* [/scripts/tscore.py](https://github.com/twinl/bsky/blob/main/scripts/tscore.py) Python library used by the Jupyter notebook
* [/tests/tscore-test.py](https://github.com/twinl/bsky/blob/main/tests/tscore-test.py) tests for the Python library

The data used for the analysis are not available in this repository
