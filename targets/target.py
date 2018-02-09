import numpy as np
import matplotlib.pyplot as plt


ft = 3000
ft_red = 100
black = np.array((10, 20, 30, 44))
white = 60

scaler = ft_red / ft

black = scaler * black
white = scaler * white



# hard code in targets on 8.5 x 11 paper

width = 11
height = 8.5


fig=plt.figure()
ax=fig.add_subplot(111)

fig.set_size_inches([width, height])


#centers = list(c(3, 3), c(5.5, 5.5), c(8, 3))

black = plt.Circle((3, 3), radius = black[-1], color='black')

ax.add_artist(black)


fig.savefig('palma_100.pdf')
