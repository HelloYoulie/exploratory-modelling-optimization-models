def cos_dist_df(x):
    """Takes dataframe x and returns a matrix with the cosine DISTANCE ...
    between all column vectors a, b and returns a DISTANCE matrix of ...
    the cosine DISTANCE according to the definition of the dot product
    
    Use distance.cosine to calculate the cosine distance
    Use distance.squareform to produce a DISTANCE matrix
    
    The row and column indices represent the experiment number. Index 0...
    is experiment 1, 1 is 2 asoasf.
    """ 
    import pandas as pd
    from scipy.spatial.distance import pdist, squareform

    # Dataframe is filled with cosine distance values
    cd = pd.DataFrame(squareform(pdist(x.T, metric='cosine')))
        
    return cd