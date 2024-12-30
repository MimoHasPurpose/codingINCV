import skimage as ski


def f1():
    image=ski.data.coins()
    edges=image
    # edges=ski.filters.sobel(image)
    ski.io.imshow(edges)
    ski.io.show()

def f2():
    image1=ski.data.human_mitosis()
    image2=ski.filters.sobel_h(image1)
    collection = [image1, image2]
    ski.io.imshow(image2)
    ski.io.show()

f2()