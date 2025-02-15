# Script used to convert PCRaster data to GeoTIFF for use in ESRI ArcGIS Pro

def map_to_tiff(input_map, output_tiff):
    """
    Convert a .tif file to .map (PCRaster format) using gdal_translate.

    Args:
    - input_map (str): Path to the input PCRaster File i.e. .map file.
    - output_tiff (str): Path to the output TIFF file (.tif file)
    """
    try:
        # Define the gdal_translate command
        command = [
            'gdal_translate',
            '-of', 'GTiff',  # Output data type
             # Metadata option for PCRaster value scale
            input_map,  # Input file
            output_tiff  # Output file
        ]

        # Run the gdal_translate command
        subprocess.run(command, check=True)
        print(f"Conversion successful: {input_map} to {output_tiff}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")


# # convert DEM
input_map = r"path\to\pcraster\file\pcr_dem.map"
output_tiff = r"path\to\tiff\file\DEM_2m_CNV.tif"

map_to_tiff(input_map, output_tiff)