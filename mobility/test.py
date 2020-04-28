import numpy
from PIL import Image

def voronoi(points,shape=(10,10)):
    depthmap = numpy.ones(shape,numpy.float)*1e308
    colormap = numpy.zeros(shape,numpy.int)
    linemap = numpy.zeros(shape,numpy.int)

    def hypot(X,Y):
        return (X-x)**2 + (Y-y)**2

    for i,(x,y) in enumerate(points):
        paraboloid = numpy.fromfunction(hypot,shape)
        colormap = numpy.where(paraboloid < depthmap,i+1,colormap)
        diff = depthmap-paraboloid
        print(diff)
        colormap = numpy.where(numpy.logical_and( diff >= 0 , diff <= 20), 4, colormap)
        depthmap = numpy.where(paraboloid < depthmap,paraboloid,depthmap)

    # for (x,y) in points:
    #     colormap[x-1:x+2,y-1:y+2] = 0

    return colormap

def draw_map(colormap):
    shape = colormap.shape

    palette = numpy.array([
            0x000000FF,
            0xFF0000FF,
            0x00FF00FF,
            0xFFFF00FF,
            0x0000FFFF,
            0xFF00FFFF,
            0x00FFFFFF,
            0xFFFFFFFF,
            ])

    colormap = numpy.transpose(colormap)
    pixels = numpy.empty(colormap.shape+(4,),numpy.int8)

    pixels[:,:,3] = palette[colormap] & 0xFF
    pixels[:,:,2] = (palette[colormap]>>8) & 0xFF
    pixels[:,:,1] = (palette[colormap]>>16) & 0xFF
    pixels[:,:,0] = (palette[colormap]>>24) & 0xFF

    image = Image.frombytes("RGBA",shape,pixels)
    image.save('voronoi.png')

if __name__ == '__main__':
    draw_map(voronoi(([3,9],[5,5],[6,8])))