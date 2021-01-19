from dataflows import Flow, dump_to_path, load
from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV
import requests, io, zipfile
import glob, os, shutil
from datapackage import Package, Resource


# Initialize fields
fields = {
	"author" : "Walter White",
	"uid" : "https://doi.org/10.1080/15295036.2016.1238101"
}

def createPackage(csvpath, outpath, fields):
    """Creates a datapackage from csv file and adds custom fields

    Parameters:
    csvpath (str): Path of the input csv file (coverted from sdf)
    outpath (str): Output directory of the datapackage
    fields (dict): custom metadata to be added to the datapackage

   """

	Flow(
	    load(
	        csvpath,
	    ),
	    dump_to_path(outpath),
	).process()

	#Updating datapackage
	package = Package("{}/datapackage.json".format(outpath))
	if fields["author"] is not None:
		package.descriptor['contributors'] = [{"title": fields["author"],}]
	if fields["uid"] is not None:
		package.descriptor['id'] = fields["uid"]
	package.commit()

	if package.valid:
		package.save("{}/datapackage.json".format(outpath))
	else:
		print("Errors:", package.errors)

def addSpectrum(spectrumpath, datapackage):
    """Adds a resource for spectra to an existing datapackage

    Parameters:
    spectrumpath (str): Path of the nmr directory
    datapackage (str): path of the existing datapackage.json to be updated

   """
	package = Package(datapackage)
	resource = Resource()
	resource.descriptor["path"] = "nmr/"
	resource.commit()
	package.add_resource(resource.descriptor)
	package.commit()
	package.save(datapackage)
	print("Errors:", package.errors)	

def SDFtoCSV(sdfpath):
	suppl = Chem.SDMolSupplier(file)
	with open(file.replace("sdf","csv"),"w") as outfile:
		SDFToCSV.Convert(suppl,outfile)
			
if __name__ == '__main__':
	 # Create in and out directories
	if not os.path.exists("in/"):
		os.mkdir("in/")

	if not os.path.exists("out/"):
		os.mkdir("out/")

	# Download sample files from Dropbox
	zip_file_url = "https://www.dropbox.com/sh/l9vhourn6145hbe/AAA1c-J2cougYT89XAJMZAOza?dl=1"

	if not os.path.exists("in/example/"):
		print("Downloading files from Dropbox")
		r = requests.get(zip_file_url)
		z = zipfile.ZipFile(io.BytesIO(r.content))
		z.extractall("in/example/")

	# Covert sdf files to csv files
	for file in glob.glob("in/example/*/*/*/*.sdf"):
		item = os.path.basename(os.path.dirname(os.path.dirname(file)))
		SDFtoCSV(file)

	#Create a datapackage for sdf file
	for file in glob.glob("in/example/*/*/*/*.csv"):
		item = os.path.basename(os.path.dirname(os.path.dirname(file)))
		outpath = "out/compound_{}".format(item)
		createPackage(file, outpath, fields)
		# Copy the original sdf file to the same location as the csv
		sdf = file.replace("csv","sdf")
		shutil.copy(sdf,"out/compound_{}/{}".format(item,os.path.basename(sdf)))

	# Add a resource for the nmrSpectrum
	for file in glob.glob("in/example/*/*/nmrSpectrum/*"):
		item = os.path.basename(os.path.dirname(os.path.dirname(file)))
		destination = "out/compound_{}/nmr".format(item)
		if file[-4:] == ".zip": # some nmr are zipped
			z = zipfile.ZipFile(file)
			z.extractall(os.path.dirname(file))
			addSpectrum(destination,"out/compound_{}/datapackage.json".format(item))
			# Copy the directory within the datapackage
			if not os.path.exists(destination):
				shutil.copytree(file[:-4],destination)
		if os.path.isdir(file): # some nmr are already unzipped
			addSpectrum(destination,"out/compound_{}/datapackage.json".format(item))
			# Copy the directory within the datapackage
			if not os.path.exists(destination):
				shutil.copytree(file,destination)



