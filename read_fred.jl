################################################################################
## Script: read_fred_xml.jl
## Author: Joe Saia
## Notes: Simple script to read in XML with FRED data
################################################################################

using LightXML, DataFrames, CSV, Dates

function read_data(series_name; file_ext = "xml", dir = ".", df_series_name = Symbol(""))
  (df_series_name == Symbol("")) && (df_series_name = Symbol(series_name))
  xdoc = parse_file("$(dir)/$(series_name).$(file_ext)")
  # get the root element
  data = root(xdoc)  # an instance of XMLElement
  N = length(data["observation"])
  df = DataFrame([Date, Float64], [:date, df_series_name], N)
  date_form = DateFormat("yyyy-mm-dd")
  for ii in eachindex(data["observation"])
    df[ii,:date] = Date(attribute(data["observation"][ii],"date"),date_form)
    df[ii,df_series_name] = parse(Float64,attribute(data["observation"][ii],"value"))
  end
  return df
end

data = read_data("FEDFUNDS" )
