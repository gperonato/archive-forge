from dataflows import Flow, dump_to_path, load
from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV
import requests, io, zipfile
import glob, os

 # Create in and out directories
if not os.path.exists("in/"):
	os.mkdir("in/")

if not os.path.exists("out/"):
	os.mkdir("out/")

# Download sample files from Dropbox
zip_file_url = "https://www.dropbox.com/sh/l9vhourn6145hbe/AAA1c-J2cougYT89XAJMZAOza?dl=1"


if not os.path.exists("in/example/"):
	print("Donwloading files from Dropbox")
	r = requests.get(zip_file_url)
	z = zipfile.ZipFile(io.BytesIO(r.content))
	z.extractall("in/example/")


# Covert sdf files to csv files
for file in glob.glob("in/example/*/*/*/*.sdf"):
	suppl = Chem.SDMolSupplier(file)
	with open(file.replace("sdf","csv"),"w") as outfile:
		SDFToCSV.Convert(suppl,outfile)
	

# Create a datapackage for sdf file
count = 1
for file in glob.glob("in/example/*/*/*/*.csv"):
	print(file)
	Flow(
	    load(
	        file,
	    ),
	    dump_to_path("out/compound_{}".format(count)),
	).process()
	count +=1

