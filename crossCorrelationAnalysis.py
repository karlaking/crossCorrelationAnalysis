# ---------------------------------------------------------------------------
# crossCorrelationAnalysis.py
# Created on: 2013-02-05 
# Description: Extracts the mean and standard
# deviation from a satellite image for comparison to a feature class.
# ---------------------------------------------------------------------------

import arcpy
import os


# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")


# Local variables:
workspace = os.path.expanduser('~/Documents/Yosemite')  
raster_image = os.path.expanduser(workspace, 'Final/tDiff/tDiff.rst')
feature_class = os.path.expanduser(workspace, 'Final/tDiff/Forest Mask.rst')
mean = os.path.expanduser(workspace, 'Yosemite GIS/CCA/MEAN')
stDev = os.path.expanduser(workspace, 'Yosemite GIS/CCA/StDEV')
zscore = os.path.expanduser(workspace, 'Yosemite GIS/CCA/zscore')


try:
    # Process: Zonal Statistics
    arcpy.gp.ZonalStatistics_sa(feature_class, 'Value', raster_image,
        mean,'MEAN', 'DATA')

    # Process: Zonal Statistics (2)
    arcpy.gp.ZonalStatistics_sa(feature_class, 'Value', raster_image,
        stDev, 'STD', 'DATA')

except:
    print "Clip example failed."
    print arcpy.GetMessages()


try:
    #Proces: Map Algebra
    RasterCalculator (raster_image - mean / stDev,zscore)


except:
    print "Clip example failed."
    print arcpy.GetMessages()

#Add processes: modal filter & reclass based on observational threshold.
    
