from image import Image #check the import issue 
import numpy as np

def adjust_brightness(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    #we first need to see how big the image is to iterate through each pixel
    x_pixels, y_pixels, num_channels = image.array.shape #getting x, y pixels and channels
    #make an empty image to not change the original
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)

    #this is the non vectorized version(intuitive way to do this)
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x, y, c] = image.array[x, y, c] * factor

    #vectorised version, much faster
    new_im.array = image.array * factor

    return new_im

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape #getting x, y pixels and channels
    #make an empty image to not change the original
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid

    #vectorised version
    # new_im.array = (image.array - mid) * factor + mid

    return new_im
    

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape #getting x, y pixels and channels
    #make an empty image to not change the original
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)

    neighbour_range = kernel_size // 2 #how many neighbours to one side we need to look at

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                #we're gonna use a naive interpretation of iterating through each neighbour and then taking avg at the end
                #there's a faster way to do this stuff, by incorporating memorization of sorts, but this is more straightforward
                total = 0
                #max and min because if it reached 0 or stuff
                for x_i in range(max(0, x - neighbour_range), min(x_pixels - 1), x + neighbour_range + 1): #obvi + 1 becoz range
                    for y_i in range(max(0, y - neighbour_range), min(y_pixels - 1), x + neighbour_range + 1): #obvi + 1 becoz range
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size ** 2) #it's divided by the total size, gives us average value
    
    return new_im
    
def apply_kernel(image, kernel):
    # the kernel should be a numpy 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]

    x_pixels, y_pixels, num_channels = image.array.shape #getting x, y pixels and channels
    #make an empty image to not change the original
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)
    kernel_size = kernel.shape[0]
    neighbour_range = kernel_size // 2 #how many neighbours to one side we need to look at
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x - neighbour_range), min(x_pixels - 1), x + neighbour_range + 1): #obvi + 1 becoz range
                    for y_i in range(max(0, y - neighbour_range), min(y_pixels - 1), x + neighbour_range + 1): #obvi + 1 becoz range
                    #we need to find out which value of the kernel this corresponds to
                        x_k = x_i + neighbour_range - x
                        y_k = y_i + neighbour_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x, y, c]

    return new_im
    
def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels, num_channels = image1.array.shape #getting x, y pixels and channels
    #make an empty image to not change the original
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image1.array[x, y, c] ** 2 + image2.array[x, y, c] ** 2) ** 0.5

    return new_im
    
    
if __name__ == '__main__':
    lake = Image(filename="lake.png")
    city = Image(filename="city.png")

    #let's lighten the image
    brightened_im = adjust_brightness(lake, 1.7)
    brightened_im.write_image("brightened.png")

    # #darken image
    darkened_im = adjust_brightness(lake, 0.3)
    darkened_im.write_image("darkened.png")

    #adjusting contrast of the lake image - higher the scaling, the more the contrast
    incr_contrast = adjust_contrast(lake, 2, 0.5 )
    incr_contrast.write_image("incrcontrast.png")

    #adjusting contrast of the lake image - higher the scaling, the more the contrast
    decr_contrast = adjust_contrast(lake, 0.5, 0.5 )
    decr_contrast.write_image("decrcontrast.png")

    #blur with kernel size 3
    blur_3 = blur(city, 3)
    blur_3.write_image("blur_k3.png")

    #blur with kernel size 15
    blur_3 = blur(city, 15)
    blur_3.write_image("blur_k15.png")

    #let's apply a sobel edge detection kernel on x & y axis, 
    sobel_x_kernel = np.array([
        [1, 2, 1], 
        [0, 0, 0], 
        [-1, -2, -1]
    ])
    sobel_y_kernel = np.array([
        [1, 0, -1], 
        [2, 0, -2], 
        [1, 0, -1]
    ])

    sobel_x = apply_kernel(city, sobel_x_kernel)
    sobel_x.write_image('edge_x.png')
    sobel_y = apply_kernel(city, sobel_y_kernel)
    sobel_y.write_image('edge_y.png')

    #maybe try combining both for an edge detection filter
    sobel_xy = combine_images(sobel_x, sobel_y)
    sobel_xy.write_image("edge_xy.png")


     


