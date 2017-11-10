# Plot target on 8.5 x 11 paper
# Converting 1000yd palma target from full to reduced size

ft = 3000
ft_red = 100
black = c(10, 20, 30, 44)
white = 60


scaler = ft_red / ft

black = scaler * black
white = scaler * white




target = function(center)
{
    x = center[1]
    y = center[2]

    nb = length(black)

    # Aiming black
    symbols(x, y, circles = black[nb], bg = "black")

    # Rings in black
    symbols(rep(x, nb), rep(y, nb), circles = black, fg = "white")

    # Outer ring
    symbols(x, y, circles = white)
}




# hard code in targets on 8.5 x 11 paper

width = 11
height = 8.5

centers = list(c(3, 3), c(5.5, 5.5), c(8, 3))

plot(c(0, width), c(0, height), type = "n")

lapply(centers, target)

target(centers[[1]])

# This is totally failing. Going to Python
