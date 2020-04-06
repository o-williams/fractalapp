########################################################################################################################
# This file defines the EscapeTimeFractal object which is the main representation of the images we are trying to create.
########################################################################################################################

# Class Definition/Name of Object - not much to worry about here
class EscapeTimeFractal():
    """
    Quick note on data types:
                                You'll notice below that I've used 'tuples'. Tuples are a data type in Python that are
                                *pretty much* lists, but they are immutable meaning once they are set they cannot be
                                changed, i.e.

                                You could define a list
                                l = [1, 2, 3, 4, 5] *use square brackets for lists

                                and a tuple
                                t = (1, 2, 3, 4, 5) *use parenthesis for tuples

                                and then change the first (zeroth in Python) element of the list l from 1 to 10 using
                                l[0] = 10
                                so that if you printed l, you would see
                                [10, 2, 3, 4, 5]

                                If you try the same for a tuple, the line
                                t[0] = 10
                                will return
                                "TypeError: 'tuple' object does not support item assignment"
                                and if you printed t you would still see
                                (1, 2, 3, 4, 5)

                                It is good practice to have initialization parameters be immutable.
    OBJECT USAGE:
    _____________________________________________
    Initializing EscapeTimeFractal object:

    fractal = EscapeTimeFractal(
                                domain - tuple of tuples representing the boundaries of the portion of the complex plane
                                            under consideration, i.e. if domain=((-2,2),(-1,1)) then the image generated
                                            will have x-coordinates between -2 & 2 and y-coordinates between -1 & 1 and
                                            each coordinate on the plane represents the complex number x+i*y.
                                    default value: ((-2,2), (-2,2))

                                resolution - tuple representing the number of pixels used for the x-axis and y-axis, i.e.
                                            if resolution=(400,200) then the image generated will be 400 pixels wide and
                                            200 pixels tall and each pixel is assigned a complex number corresponding to
                                            the dimensions of the domain defined above.
                                    default value: (500, 500)

                                *NOTE: If domain and resolution are not scaled properly, the final image will turn out
                                        distorted. It would be possible to automatically choose some parameters so
                                        the scale is always perfect, but there may be instances where the user WANTS to
                                        stretch/squeeze the image in a certain direction to reveal more detail.
                                )

    Example:
        fractal = EscapeTimeFractal(
                                    domain = ((-2, 2), (-2, 2)),
                                    resolution = (500, 500)
                                    )
    """

    # Init method is the first thing that happens when a new instance of the EscapeTimeFractal is created (the example
    # above is what you would type to create one of these objects). If you want to use default values, you would type:
    # fractal = EscapeTimeFractal()
    def __init__(self, # self (explained more below) is always a required input for any method (function) within a class
                 domain = ((-2, 2), (-2, 2)), # set default domain
                 resolution = (500, 500) # set default resolution
                 ):

        # The first thing we usually want to do is put initialization parameters on 'self':
        self.domain = domain
        self.resolution = resolution

        # Without doing this, the variables 'domain' and 'resolution' will only be usable within this init method. We
        # will likely need to use 'domain' and 'resolution' elsewhere in the code, so adding them to self allows us to
        # access that information by typing self.domain or self.resolution

    # Examples of methods that are not within the above init method but may need to access domain and resolution:
    def getdomain_good(self):
        return self.domain # this way works and is correct

    def getdomain_bad(self):
        return domain # this way does not work - note the red squigglies

    def getresolution_good(self):
        return self.resolution # this way works and is correct

    def getresolution_bad(self):
        return resolution