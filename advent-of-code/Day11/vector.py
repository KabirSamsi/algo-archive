def stretch(eigenvector, initial_vector, scalar_factor): #Increase a vector by a scalar factor to create an eigenvector
    return [(scalar_factor * initial_vector[0]) + eigenvector[0], (scalar_factor * initial_vector[1]) +eigenvector[1]]
