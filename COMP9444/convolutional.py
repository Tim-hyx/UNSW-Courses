A = [int(i) for i in input('input J K Layer M N Padding stride filter: ').split()]
J, K, L, M, N, P, s, f = A
weights, width, height = 1 + M * N * L, 1 + (J + 2 * P - M) // s, 1 + (K + 2 * P - N) // s
print(f'weights per neuron:     1+M*N*L=1+{M}*{N}*{L}={weights}')
print(f'width:                  1+(J+2*P-M)/s=1+({J}+2*{P}-{M})/{s}={width}')
print(f'height:                 1+(K+2*P-N)/s=1+({K}+2*{P}-{N})/{s}={height}')
print(f'neurons in layer:       {width}*{height}*{f}={width * height * f}')
print(f'connections:            {width}*{height}*{f}*{weights}={width * height * f * weights}')
print(f'independent parameters: {f}*{weights}={f * weights}')
