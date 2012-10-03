import matplotlib.colors as col
import numpy

def createColourmap(A, name):
  """ Create a colourmap based
  on a matrix A, where negative
  is relative blue, and positive
  is relative red."""
  matrix = numpy.matrix(A)
  maxvalue = matrix.max()
  minvalue = matrix.min()

  # Colours
  red   = '#ff0000'
  blue  = '#0000ff'
  white = '#ffffff'

  if(minvalue > 0.0):
    return col.LinearSegmentedColormap.from_list(name, [white, red])
    print 'positive axis'

  if(maxvalue < 0.0):
    return col.LinearSegmentedColormap.from_list(name, [blue, white])
    print 'negative axis'

  reds = [
   '#FF0000',
   '#FF1111',
   '#FF3333',
   '#FF5555',
   '#FF7777',
   '#FF9999',
   '#FFBBBB',
   '#FFDDDD',
   '#FFEEEE']

  blues = [
   '#0000FF',
   '#1111FF',
   '#3333FF',
   '#5555FF',
   '#9999FF',
   '#BBBBFF',
   '#DDDDFF',
   '#EEEEFF']

  blues = blues[::-1]
  reds = reds[::-1]

  colorArray = []
  colorArrayRed = []
  colorArrayBlue = []

  stepSizer = 6.0

  if abs(maxvalue) > abs(minvalue):
    stepSize = maxvalue/stepSizer
  else:
    stepSize = abs(minvalue)/stepSizer

  i = 0
  val = minvalue
  val += stepSize
  while val < 0.0:
    val += stepSize
    colorArrayBlue.append(blues[i])
    i += 1

  i = 0
  val = maxvalue
  val -= stepSize
  while val > 0.0:
    val -= stepSize
    colorArrayRed.append(reds[i])
    i += 1

  colorArrayBlue = colorArrayBlue[::-1]
  colorArray.extend(colorArrayBlue)
  colorArray.append(white)
  colorArray.extend(colorArrayRed)

  return col.LinearSegmentedColormap.from_list(name, colorArray)


