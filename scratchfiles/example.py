from scratchfiles.escapetimefractal import EscapeTimeFractal

mandelbrotSet = EscapeTimeFractal(domain=((-1,1), (-1,1)), resolution=(100, 100)) # x(n+1) = x(n)^2 + C
burningShip = EscapeTimeFractal(domain=((-2,2), (-2,2)), resolution=(300, 300))