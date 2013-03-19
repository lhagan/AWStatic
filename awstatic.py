#!/usr/bin/python
import awstatic.cli
import shutil

# delete old output (required if last run failed)
shutil.rmtree('out')

# run
awstatic.cli.main()
