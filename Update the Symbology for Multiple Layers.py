import arcpy.mapping;

sourceBasinBoundary = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Basin Boundary.lyr') # the source Symbology Layer for Basin Boundary
sourceDeletedMains = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Deleted Gravity Mains.lyr') # Deleted Mains
sourceDeletedManholes = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Deleted Manholes.lyr') # Deleted Manholes
sourceNetworkStructure = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Network Structure.lyr') # Network Structure
sourceSanitaryBends = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sanitary Sewer Bends.lyr') # Sanitary Sewer Bends
sourceCleanouts = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Clean Outs.lyr') # You get the idea
sourceControlValves = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Control Valves.lyr')
sourceFittings = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Fittings.lyr')
sourceGravityMains = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Gravity Main.lyr')
sourceLaterals = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Lateral Lines.lyr')
sourceManhole = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Manhole.lyr')
sourcePressurizedMains = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Pressurized Mains.lyr')
sourcePumpStations = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Sewer Pump Station.lyr')
sourceSSO = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\SSO.lyr')
sourceAddressPoint = arcpy.mapping.Layer(r'C:\Users\luchaymm\Documents\Work From Home\Layers\Base_Data\Address Point.lyr')

mxd = arcpy.mapping.MapDocument(r'C:\Users\luchaymm\Documents\Programming Test Environment\Symbology Updating\Working\Symbology Updating.mxd') # the MXD to change the Symbology
df = arcpy.mapping.ListDataFrames(mxd)[0] # grab the dataframe from the MXD
layers = arcpy.mapping.ListLayers(mxd, data_frame = df)[0] # list the layers in the data frame - must use the first indice of the ListLayers object to return an object type as a layer!
for each in layers: # loop through each of the layers

    if each.name == 'ssBend': # condition to meet to update the symbology for Bends
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceSanitaryBends, False) # update the current layer with the sourceLayer's symbology and update all other properties by using the False parameter


    elif each.name == 'ssCleanOut': # condition to meet to update the symbology for Cleanouts
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceCleanouts, False) # update the current layer with the sourceLayer's symbology and update all other properties by using the False parameter


    elif each.name == 'ssControlValve': # condition to meet to update the symbology for Control Valves
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceControlValves, False) # update the current layer with the sourceLayer's symbology and update all other properties by using the False parameter


    elif each.name == 'ssFitting':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceFittings, False)


    elif each.name == 'ssManhole':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceManhole, False)


    elif each.name == 'ssManhole_Deleted':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceDeletedManholes, False)


    elif each.name == 'ssNetworkStructure':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceNetworkStructure, False)


    elif each.name == 'ssPumpStation':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourcePumpStations, False)


    elif each.name == 'ssGravityMain':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceGravityMains, False)


    elif each.name == 'ssGravityMain_Deleted':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceDeletedMains, False)


    elif each.name == 'ssLateralLine':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceLaterals, False)


    elif each.name == 'ssPressurizedMain':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourcePressurizedMains, False)


    elif each.name == 'SSO':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceSSO, False)


    elif each.name == 'ssBasinBoundary':
        print (each.name + ' is being updated.')
        arcpy.mapping.UpdateLayer(df, each, sourceBasinBoundary, False)


mxd.saveACopy(r'C:\Users\luchaymm\Documents\Programming Test Environment\Symbology Updating\Working\Symbology Updating_Copy.mxd') # must make a copy for this script to work