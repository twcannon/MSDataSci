from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from svg.path import parse_path 
from scipy import optimize
import sys


Alternberg  = '/home/thomas/git/MSDataSci/OpsResearch/luge/Alternberg.png'
Calgary     = '/home/thomas/git/MSDataSci/OpsResearch/luge/Calgary.png'
Koenigssee  = '/home/thomas/git/MSDataSci/OpsResearch/luge/Koenigssee.png'
Lillehammer = '/home/thomas/git/MSDataSci/OpsResearch/luge/Lillehammer.png'
Oberhof     = '/home/thomas/git/MSDataSci/OpsResearch/luge/Oberhof.png'
Whistler    = '/home/thomas/git/MSDataSci/OpsResearch/luge/Whistler.png'
Winterberg  = '/home/thomas/git/MSDataSci/OpsResearch/luge/Winterberg.png'


Whistler_path = """m 60.26342,352.57207 c 0,0 -2.174454,40.07206 -2.795726,42.24652 -0.621272,2.17445 -0.931909,30.44234 -0.931909,30.44234 0,0 -1.863817,111.20776 -0.931908,130.15656 0.931908,18.94881 4.348906,18.94881 16.463718,26.71472 12.114811,7.7659 25.16153,-2.48509 31.374255,-6.21273 6.21272,-3.72763 7.14463,-11.49354 9.62972,-29.51043 2.48509,-18.0169 -0.62127,-20.50199 -4.03827,-23.60835 -3.417,-3.10637 -24.229622,-18.0169 -29.510437,-31.99553 -5.280815,-13.97863 4.348906,-39.4508 5.280815,-47.2167 0.931909,-7.76591 0,-7.14463 -4.348907,-23.29771 -4.348906,-16.15309 2.48509,-24.54026 17.395627,-45.35289 14.910532,-20.81262 10.872262,-27.64662 5.280812,-37.27634 -5.591448,-9.62972 -31.374252,-15.53181 -35.101886,-18.0169 -3.727634,-2.48509 -2.485089,-2.48509 -6.833996,-13.35735 -4.348906,-10.87227 -2.795726,-31.99553 0.310636,-41.00398 3.106362,-9.00845 11.804175,-15.22117 32.6168,-20.81262 20.812626,-5.59146 28.267896,-9.94036 34.169976,-17.39563 5.90209,-7.45527 0,-15.53181 -6.52336,-20.19135 -6.52336,-4.65955 -22.987074,1.86381 -39.140155,4.03827 -16.153082,2.17445 -20.191352,-7.14463 -22.055169,-14.28927 -1.863817,-7.14463 7.144632,-17.25944 10.250994,-20.05517 3.106362,-2.79572 28.578529,-11.94035 34.79125,-13.1829 6.21273,-1.24254 17.08499,-7.7659 22.05517,-11.1829 4.97018,-3.417 3.10636,-9.31909 -2.17445,-13.66799 -5.28082,-4.34891 -21.74453,0.31063 -25.16153,1.24254 -3.417001,0.93191 -33.548711,12.11481 -43.799705,8.69781 -10.250994,-3.41699 -15.221173,-8.07654 -17.706262,-13.35735 -2.48509,-5.28082 -2.48509,-9.94036 -2.48509,-12.73608 0,-2.79573 1.242545,-7.45527 1.242545,-7.45527 0,0 2.795726,-4.34891 5.902088,-6.52336 3.106361,-2.17446 19.259443,-1.55318 19.259443,-1.55318 0,0 5.280815,-0.62128 9.940358,-6.834 4.659543,-6.212723 6.52336,-77.037773 6.52336,-77.037773"""
Whistler_path_reverse = """m 79.212227,22.987077 c 0,0 -1.863817,70.82505 -6.52336,77.037773 -4.659543,6.21272 -9.940358,6.834 -9.940358,6.834 0,0 -16.153082,-0.62128 -19.259443,1.55318 -3.106362,2.17445 -5.902088,6.52336 -5.902088,6.52336 0,0 -1.242545,4.65954 -1.242545,7.45527 0,2.79572 0,7.45526 2.48509,12.73608 2.485089,5.28081 7.455268,9.94036 17.706262,13.35735 10.250994,3.417 40.382704,-7.7659 43.799705,-8.69781 3.417,-0.93191 19.88071,-5.59145 25.16153,-1.24254 5.28081,4.3489 7.14463,10.25099 2.17445,13.66799 -4.97018,3.417 -15.84244,9.94036 -22.05517,11.1829 -6.212721,1.24255 -31.684888,10.38718 -34.79125,13.1829 -3.106362,2.79573 -12.114811,12.91054 -10.250994,20.05517 1.863817,7.14464 5.902087,16.46372 22.055169,14.28927 16.153081,-2.17446 32.616795,-8.69782 39.140155,-4.03827 6.52336,4.65954 12.42545,12.73608 6.52336,20.19135 -5.90208,7.45527 -13.35735,11.80417 -34.169976,17.39563 -20.812625,5.59145 -29.510438,11.80417 -32.6168,20.81262 -3.106362,9.00845 -4.659542,30.13171 -0.310636,41.00398 4.348907,10.87226 3.106362,10.87226 6.833996,13.35735 3.727634,2.48509 29.510438,8.38718 35.101886,18.0169 5.59145,9.62972 9.62972,16.46372 -5.280812,37.27634 -14.910537,20.81263 -21.744533,29.1998 -17.395627,45.35289 4.348907,16.15308 5.280816,15.5318 4.348907,23.29771 -0.931909,7.7659 -10.56163,33.23807 -5.280815,47.2167 5.280815,13.97863 26.093437,28.88916 29.510437,31.99553 3.417,3.10636 6.52336,5.59145 4.03827,23.60835 -2.48509,18.01689 -3.417,25.7828 -9.62972,29.51043 -6.212725,3.72764 -19.259444,13.97863 -31.374255,6.21273 -12.114812,-7.76591 -15.53181,-7.76591 -16.463718,-26.71472 -0.931909,-18.9488 0.931908,-130.15656 0.931908,-130.15656 0,0 0.310637,-28.26789 0.931909,-30.44234 0.621272,-2.17446 2.795726,-42.24652 2.795726,-42.24652"""

path = parse_path(Whistler_path)

Whistler_length = 1400
Whistler_points = [(p.real,p.imag) for p in (path.point(i/Whistler_length) for i in range(0,Whistler_length+1))]

line_x,line_y = zip(*Whistler_points)

# track = Image.open(Alternberg).convert('P')
# track = Image.open(Calgary).convert('P')
# track = Image.open(Koenigssee).convert('P')
# track = Image.open(Lillehammer).convert('P')
# track = Image.open(Oberhof).convert('P')
track = Image.open(Whistler).convert('P')
# track = Image.open(Winterberg).convert('P')

x_lim = track.size[0]
y_lim = track.size[1]

track = ((np.asarray(track)/225.0)-1.0)*(-1.0)
line_y = tuple((np.asarray(line_y)-y_lim)*(-1))


f = plt.figure(figsize=(3,10))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)
ax.imshow(track, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
ax2.plot(line_x,line_y,'b-')
ax2.set_xlim(0,x_lim)
ax2.set_ylim(0,y_lim)
plt.show()





class ComputeCurvature:
    def __init__(self):
        """ Initialize some variables """
        self.xc = 0  # X-coordinate of circle center
        self.yc = 0  # Y-coordinate of circle center
        self.r = 0   # Radius of the circle
        self.xx = np.array([])  # Data points
        self.yy = np.array([])  # Data points

    def calc_r(self, xc, yc):
        """ calculate the distance of each 2D points from the center (xc, yc) """
        return np.sqrt((self.xx-xc)**2 + (self.yy-yc)**2)

    def f(self, c):
        """ calculate the algebraic distance between the data points and the mean circle centered at c=(xc, yc) """
        ri = self.calc_r(*c)
        return ri - ri.mean()

    def df(self, c):
        """ Jacobian of f_2b
        The axis corresponding to derivatives must be coherent with the col_deriv option of leastsq"""
        xc, yc = c
        df_dc = np.empty((len(c), x.size))

        ri = self.calc_r(xc, yc)
        df_dc[0] = (xc - x)/ri                   # dR/dxc
        df_dc[1] = (yc - y)/ri                   # dR/dyc
        df_dc = df_dc - df_dc.mean(axis=1)[:, np.newaxis]
        return df_dc

    def fit(self, xx, yy):
        self.xx = xx
        self.yy = yy
        center_estimate = np.r_[np.mean(xx), np.mean(yy)]
        center = optimize.leastsq(self.f, center_estimate, Dfun=self.df, col_deriv=True)[0]

        self.xc, self.yc = center
        ri = self.calc_r(*center)
        self.r = ri.mean()

        # return 1/self.r  # Return the curvature
        return self.r  # Return the radius

line_x = list(line_x)[::-1]
line_y = list(line_y)[::-1]

curve_point_total = 10

radius_array = []
for n in range (0,Whistler_length-curve_point_total,curve_point_total):

    x = np.asarray(line_x[n:n+curve_point_total])
    y = np.asarray(line_y[n:n+curve_point_total])

    comp_curv = ComputeCurvature()
    radius = comp_curv.fit(x, y)
    radius_array.append(radius)
    # Plot the result
    # theta_fit = np.linspace(-np.pi, np.pi, 180)
    # x_fit = comp_curv.xc + comp_curv.r*np.cos(theta_fit)
    # y_fit = comp_curv.yc + comp_curv.r*np.sin(theta_fit)
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(line_x,line_y,'b-')
    # ax.set_xlim(0,x_lim)
    # ax.set_ylim(0,y_lim)
    # ax.plot(x_fit, y_fit, 'k--', label='fit', lw=2)
    # ax.plot(x, y, 'ro', label='data', ms=8, mec='b', mew=1)
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_aspect(aspect='equal')
    # ax.set_title('radius = {:.2f}'.format(radius))
    # # plt.show()
    # plt.savefig('Whistler_'+str(n)+'.png')


print('average radius ', np.mean(radius_array))
print('median radius ', np.median(radius_array))

plt.hist(np.log(radius_array), bins=50)
plt.show()