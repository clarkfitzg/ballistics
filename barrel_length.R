# Data from:
# https://rifleshooter.com/2015/12/223-remington-5-56mm-nato-barrel-length-and-velocity-26-inches-to-6-inches/

velocity = data.frame(length = 26:20
        , velocity = c(2849, 2828, 2804, 2775, 2774, 2762, 2740))

with(velocity, plot(length, velocity))

fit = lm(velocity ~ length, velocity)

summary(fit)

# So velocity increases by about 18 ft/s per inch of barrel in the region
# of 20 - 26 inches.

predict(fit)

# How much does an extra inch of barrel weigh?
outer_diam = 0.75
inner_diam = 0.22
steel_density = 0.285

# Each inch adds an extra 0.115 lbs
mass_inch = pi * ((outer_diam/2)^2 - (inner_diam/2)^2) * steel_density

# A 20" barrel is about 0.7 lbs lighter than a 26"
6 * mass_inch

# Maybe a 22" barrel in the light palma contour is the sweet spot for me.
4 * mass_inch

