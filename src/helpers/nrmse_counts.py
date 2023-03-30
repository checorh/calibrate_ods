import numpy as np

def compute_nrmse_counts(df_true, df_simulated):
    # Merge simulated output with ground truth
    df1 = df_true\
        .merge(df_simulated, on=['EdgeID', 'interval_begin', 'interval_end'],
        suffixes=('_GT', '_sim'), how='left')
    
    df1['diff_square'] = (
        df1['interval_nVehContrib_GT'] - df1['interval_nVehContrib_sim']
        )**2
    
    n = df1.shape[0]
    
    RMSN = np.sqrt(n*(df1['diff_square'].sum()))/df1['interval_nVehContrib_GT'].sum()
    
    return RMSN