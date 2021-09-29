[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ess-dmsc-dram/python-course-ikon/master)

# python-course-ikon
A collection of notebooks for the IKON python training

## Scipp

The tutorials in this module are part of the `scippneutron` documentation.
The files in this repository can be generated as follows:

```sh
tutorials=../scippneutron/docs/tutorials  # adjust as necessary
python "$tutorials"/strip-solutions.py "$tutorials"/[1-9]* --output-dir=notebooks/6_scipp
cp "$tutorials"/[1-9]* solutions/6_scipp
```
