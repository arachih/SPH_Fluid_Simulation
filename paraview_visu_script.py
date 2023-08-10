# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

LoadPalette(paletteName='WhiteBackground')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

file_names = []
for i in range(0, 3950, 50):  # Assuming the VTK files are named as sph000.vtk, sph050.vtk, ..., sph3900.vtk
    file_name = f'.\\output\\sph{i:04d}.vtk'
    file_names.append(file_name)

sph = LegacyVTKReader(registrationName='sph*', FileNames=file_names)


# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# show data in view
sphDisplay = Show(sph, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')

# trace defaults for the display properties.
sphDisplay.Representation = 'Surface'
sphDisplay.ColorArrayName = ['POINTS', 'Density']
sphDisplay.LookupTable = densityLUT
sphDisplay.SelectTCoordArray = 'None'
sphDisplay.SelectNormalArray = 'None'
sphDisplay.SelectTangentArray = 'None'
sphDisplay.OSPRayScaleArray = 'Density'
sphDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sphDisplay.SelectOrientationVectors = 'None'
sphDisplay.ScaleFactor = 31.52952259523674
sphDisplay.SelectScaleArray = 'Density'
sphDisplay.GlyphType = 'Arrow'
sphDisplay.GlyphTableIndexArray = 'Density'
sphDisplay.GaussianRadius = 1.576476129761837
sphDisplay.SetScaleArray = ['POINTS', 'Density']
sphDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sphDisplay.OpacityArray = ['POINTS', 'Density']
sphDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sphDisplay.DataAxesGrid = 'GridAxesRepresentation'
sphDisplay.PolarAxes = 'PolarAxesRepresentation'
sphDisplay.BumpMapInputDataArray = ['POINTS', 'Density']
sphDisplay.ExtrusionInputDataArray = ['POINTS', 'Density']
sphDisplay.InputVectors = [None, '']
sphDisplay.SelectInputVectors = [None, '']
sphDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sphDisplay.ScaleTransferFunction.Points = [0.012533451768486758, 0.0, 0.5, 0.0, 0.05015779676886105, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sphDisplay.OpacityTransferFunction.Points = [0.012533451768486758, 0.0, 0.5, 0.0, 0.05015779676886105, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [50.24599973906396, 162.6703381825437, 10000.0]
renderView1.CameraFocalPoint = [50.24599973906396, 162.6703381825437, 0.0]

# show color bar/color legend
sphDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')

# create a new 'Delaunay 2D'
delaunay2D1 = Delaunay2D(registrationName='Delaunay2D1', Input=sph)

# show data in view
delaunay2D1Display = Show(delaunay2D1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
delaunay2D1Display.Representation = 'Surface'
delaunay2D1Display.ColorArrayName = ['POINTS', 'Density']
delaunay2D1Display.LookupTable = densityLUT
delaunay2D1Display.SelectTCoordArray = 'None'
delaunay2D1Display.SelectNormalArray = 'None'
delaunay2D1Display.SelectTangentArray = 'None'
delaunay2D1Display.OSPRayScaleArray = 'Density'
delaunay2D1Display.OSPRayScaleFunction = 'PiecewiseFunction'
delaunay2D1Display.SelectOrientationVectors = 'None'
delaunay2D1Display.ScaleFactor = 31.52952259523674
delaunay2D1Display.SelectScaleArray = 'Density'
delaunay2D1Display.GlyphType = 'Arrow'
delaunay2D1Display.GlyphTableIndexArray = 'Density'
delaunay2D1Display.GaussianRadius = 1.576476129761837
delaunay2D1Display.SetScaleArray = ['POINTS', 'Density']
delaunay2D1Display.ScaleTransferFunction = 'PiecewiseFunction'
delaunay2D1Display.OpacityArray = ['POINTS', 'Density']
delaunay2D1Display.OpacityTransferFunction = 'PiecewiseFunction'
delaunay2D1Display.DataAxesGrid = 'GridAxesRepresentation'
delaunay2D1Display.PolarAxes = 'PolarAxesRepresentation'
delaunay2D1Display.BumpMapInputDataArray = ['POINTS', 'Density']
delaunay2D1Display.ExtrusionInputDataArray = ['POINTS', 'Density']
delaunay2D1Display.InputVectors = [None, '']
delaunay2D1Display.SelectInputVectors = [None, '']
delaunay2D1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
delaunay2D1Display.ScaleTransferFunction.Points = [0.012533451768486758, 0.0, 0.5, 0.0, 0.05015779676886105, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
delaunay2D1Display.OpacityTransferFunction.Points = [0.012533451768486758, 0.0, 0.5, 0.0, 0.05015779676886105, 1.0, 0.5, 0.0]

# hide data in view
Hide(sph, renderView1)

# show color bar/color legend
delaunay2D1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on delaunay2D1
delaunay2D1.Alpha = 3.0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on delaunay2D1
delaunay2D1.Alpha = 1.0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on delaunay2D1
delaunay2D1.Alpha = 8.0

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plane'
plane1 = Plane(registrationName='Plane1')

# Properties modified on plane1
plane1.Point1 = [400.0, 0.0, 0.0]
plane1.Point2 = [0.0, 400.0, 0.0]

# show data in view
plane1Display = Show(plane1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plane1Display.Representation = 'Surface'
plane1Display.ColorArrayName = [None, '']
plane1Display.SelectTCoordArray = 'TextureCoordinates'
plane1Display.SelectNormalArray = 'Normals'
plane1Display.SelectTangentArray = 'None'
plane1Display.OSPRayScaleArray = 'Normals'
plane1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plane1Display.SelectOrientationVectors = 'None'
plane1Display.ScaleFactor = 40.1
plane1Display.SelectScaleArray = 'None'
plane1Display.GlyphType = 'Arrow'
plane1Display.GlyphTableIndexArray = 'None'
plane1Display.GaussianRadius = 2.005
plane1Display.SetScaleArray = ['POINTS', 'Normals']
plane1Display.ScaleTransferFunction = 'PiecewiseFunction'
plane1Display.OpacityArray = ['POINTS', 'Normals']
plane1Display.OpacityTransferFunction = 'PiecewiseFunction'
plane1Display.DataAxesGrid = 'GridAxesRepresentation'
plane1Display.PolarAxes = 'PolarAxesRepresentation'
plane1Display.BumpMapInputDataArray = [None, '']
plane1Display.ExtrusionInputDataArray = ['POINTS', 'Normals']
plane1Display.InputVectors = ['POINTS', 'Normals']
plane1Display.SelectInputVectors = ['POINTS', 'Normals']
plane1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plane1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plane1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(delaunay2D1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
densityLUT.ApplyPreset('Jet', True)

# Properties modified on densityLUT
densityLUT.NumberOfTableValues = 20

# get color legend/bar for densityLUT in view renderView1
densityLUTColorBar = GetScalarBar(densityLUT, renderView1)

# Properties modified on densityLUTColorBar
densityLUTColorBar.TitleFontFamily = 'Courier'
densityLUTColorBar.TitleBold = 1
densityLUTColorBar.TitleFontSize = 20
densityLUTColorBar.LabelFontFamily = 'Courier'
densityLUTColorBar.LabelBold = 1
densityLUTColorBar.LabelFontSize = 20

# change scalar bar placement
densityLUTColorBar.WindowLocation = 'AnyLocation'
densityLUTColorBar.Position = [0.8054714532871973, 0.5201005025125628]
densityLUTColorBar.ScalarBarLength = 0.32999999999999985

# change scalar bar placement
densityLUTColorBar.Position = [0.8054714532871973, 0.1482412060301507]
densityLUTColorBar.ScalarBarLength = 0.7018592964824119

animationScene1.Play()

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1156, 796)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [200.0, 200.0, 1095.5523738351199]
renderView1.CameraFocalPoint = [200.0, 200.0, 0.0]
renderView1.CameraParallelScale = 283.5498192558056

# save animation
SaveAnimation('./output/sph_anim.png', renderView1, ImageResolution=[1156, 796],
    FrameWindow=[0, 78])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1156, 796)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [200.0, 200.0, 1095.5523738351199]
renderView1.CameraFocalPoint = [200.0, 200.0, 0.0]
renderView1.CameraParallelScale = 283.5498192558056

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).