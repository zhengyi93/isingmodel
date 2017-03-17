from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initializing the Ising Ferromagnet
N = 10                   # N*N 2D square lattice
T = 120                   # Thermodynamic temperature (units of J/k_b)
H = 100
state = 2*random.randint(2,size=(N, N))-1


def fixB(x, y):         # Boundary fix
    if x < 0: return state[N-1][y]
    if y < 0: return state[x][N-1]
    if x == N: return state[0][y]
    if y == N: return state[x][0]
    return state[x][y]


def flip(x, y):
    global state
    deltaE = -2*state[x][y]*(fixB(x-1, y)+fixB(x, y-1)+fixB(x+1, y)+fixB(x, y+1) + H)
    if exp(deltaE/T) > random.rand():
        state[x][y] = -state[x][y]

fig = plt.figure()

im = plt.imshow(matrix(state), animated=True)


def updatefig(*args):
    # A single time step: flipping N*N random points
    global state
    for j in range(N**2):
        x = random.randint(N)
        y = random.randint(N)
        flip(x, y)
    im.set_array(matrix(state))
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=5, blit=True)
plt.show()
