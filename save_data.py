import os
import pandas as pd

def save_data(over_and_ball_info, shot_types, output_path='data/'):
    os.makedirs(output_path, exist_ok=True)
    df = pd.DataFrame({'Over': over_and_ball_info[0],
                       'Ball': over_and_ball_info[1],
                       'Shot_Type': shot_types})
    df.to_csv(os.path.join(output_path, 'cricket_shots.csv'), index=False)

over_and_ball_info = ([0.1, 0.2, 0.3], [1, 2, 3]) 
shot_types = ['Drive', 'Pull', 'Cut']
save_data(over_and_ball_info, shot_types)
