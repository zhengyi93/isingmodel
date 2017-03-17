from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initializing the Ising Ferromagnet
N = 20                   # N*N 2D square lattice
T = 2                   # Thermodynamic temperature (units of J/k_b)
p = [1.0, exp(-4 / T), exp(-8 / T), 1.0, 1.0]
# state = [[1]*N]*N    # Initializing the state to all ones
primordialstate = 2*random.randint(2,size=(N, N))-1
state = 2*random.randint(2,size=(N, N))-1
M = sum(state)           # Magnetisation
E = -2*N**2            # Energy (units of J)


def fixB(x, y):         # Boundary fix
    if x < 0: return state[N-1][y]
    if y < 0: return state[x][N-1]
    if x == N: return state[0][y]
    if y == N: return state[x][0]
    return state[x][y]


def flip(x, y):
    global E, M, state
    deltaE = state[x][y]*(fixB(x-1, y)+fixB(x, y-1)+fixB(x+1, y)+fixB(x, y+1))//2
    if p[deltaE] > random.rand():
        state[x][y] = -state[x][y]
        E += deltaE
        M += 2*state[x][y]


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='ZY'), bitrate=1800)

fig = plt.figure()
ims = []

for i in range(1000):
    # A single time step: flipping N*N random points
    for j in range(N**2):
        x, y = random.randint(N, size=2)
        flip(x, y)
    im = plt.imshow(matrix(state), animated=True)
    ims.append([im])
    #print(M)
    #print(matrix(state))
    #print(M, E)
    #input()

im_ani = animation.ArtistAnimation(fig, ims, interval=10, repeat_delay=1000,
                                   blit=True)
im_ani.save('timelapse.mp4', writer=writer)