# FREDio
Simple scripts to work with FRED Data

## `pullfred.py`

`pullfred.py` is a simple script that can be run from the command to download
data from FRED in either XML (default) or JSON formats supproted by the FRED API. The
script requires python 3.

### Usage
The minimal function call is `python3 pullfred.py <series name> <api_key>`. The
script defines and calls a single function `download_fred`. The script will by
default attempt to download an XML file with the data for the FRED series
`<series name>` and save it as `<series name>.xml`. 

The function call itself can be edited in the script to change the date range
pulled, the units, the frequency, the aggreation method, and the file type
downloaded. If none of these are specified then the script downloads the exact
data that you would have gotten if you had gone to the FRED website and searched
for the series name and openened the default series which is usually the highest
frequency series available. If the user changes the `file_type` argument to
`json`, then a JSON file will be downloaded and the output file will have a
`.json` suffix in place of a `.xml` suffix.  

### API Key
api keys can be accessed from the [FRED
website](https://research.stlouisfed.org/docs/api/api_key.html). 


## `read_fred.jl`
`read_fred.jl` contains a function that can be used to read in XML data from
FRED that is downloaded by `pullfred.pdsa`. XML file is read in as a DataFrame object

### project files
The julia code has some dependencies that can be automatically loaded by using 
[Pkg](https://julialang.github.io/Pkg.jl/v1/environments/#Using-someone-else's-project-1)
