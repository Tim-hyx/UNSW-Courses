# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Defines two classes, Point and NonVerticalLine.
#
# Point:
# Either no coordinate or two coordinates should be passed to __init__(),
# as floating point numbers or as integers.
# In the first case, the coordinates are set to those of the point
# at the origin.
#
# NonVerticalLine:
# No, one or two named arguments, point_1 and point_2, of type Point,
# should be passed to __init__().
# When an argument is not passed, it is set to the point at the origin.
# Both points have to determine a nonvertical line.
# Such an object can be modified by changing one point or both points
# thanks to the change_point_or_points() method.
# At any stage, the object maintains correct values for slope and intersect.


# Will be tested only when passing no, one or two arguments; moreover,
# when an argument is passed, it will be a float or an int.
class Point:
    def __init__(self, x=None, y=None):
        if (x is None) and (y is None):
            self.x = 0
            self.y = 0
        elif (x is not None) and (y is not None):
            self.x = x
            self.y = y
        else:
            raise PointError('Cannot create point.')
    # REPLACE PASS ABOVE WITH YOUR CODE


class PointError(Exception):
    def __init__(self, feedback):
        self.feedback = feedback


# Will be tested only when passing no, one or two arguments,
# that have to be named; moreover, when an argument is passed,
# it will be a Point object.
class NonVerticalLine:
    def __init__(self, *, point_1=None, point_2=None):
        if point_1 is None and point_2 is None:
            self.point_2 = Point(0, 0)
            self.point_1 = Point(0, 0)
        if point_1 is not None and point_2 is not None:
            self.point_2 = point_2
            self.point_1 = point_1
        if point_1 is not None and point_2 is None:
            self.point_2 = Point(0, 0)
            self.point_1 = point_1
        if point_1 is None and point_2 is not None:
            self.point_1 = Point(0, 0)
            self.point_2 = point_2
        if self.point_2.x == self.point_1.x:
            raise NonVerticalLineError('Cannot create nonvertical line.')
        self.slope = (self.point_1.y - self.point_2.y) / (self.point_1.x - self.point_2.x)
        self.intercept = self.point_1.y - self.slope * self.point_1.x

    def change_point_or_points(self, **kwargs):
        if 'point_1' in kwargs and 'point_2' not in kwargs:
            point_1 = kwargs.get('point_1')
            if point_1.x == self.point_2.x:
                raise NonVerticalLineError('Cannot perform this change.')
            else:
                self.point_1 = point_1
        if 'point_2' in kwargs and 'point_1' not in kwargs:
            point_2 = kwargs.get('point_2')
            if point_2.x == self.point_1.x:
                raise NonVerticalLineError('Cannot perform this change.')
            else:
                self.point_2 = point_2
        if 'point_1' in kwargs and 'point_2' in kwargs:
            point_1 = kwargs.get('point_1')
            point_2 = kwargs.get('point_2')
            if point_1.x == point_2.x:
                raise NonVerticalLineError('Cannot perform this change.')
            else:
                self.point_2 = point_2
                self.point_1 = point_1
        self.slope = (self.point_2.y - self.point_1.y) / (self.point_2.x - self.point_1.x)
        self.intercept = self.point_1.y - self.slope * self.point_1.x
    # REPLACE PASS ABOVE WITH YOUR CODE


class NonVerticalLineError(Exception):
    def __init__(self, feedback):
        self.feedback = feedback
