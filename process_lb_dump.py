import json
import pandas as pd


def get_listens(path):
    """
    Description:
    the get_listens function takes a string path to a .listens file in the ListenBrainz format, and reads each JSON object on every line. 
    The data is then stored in a python dictionary with the corresponding key value pairs

    Params:
    path - String path name to a listens file
    """
    
    data={
            "user_id":[],
            "timestamp":[],
            "track_name":[],
            "artist_name":[],
            "recording_msid":[],
            #### Additional key names to be added here
            # ex.
            # "recording_mbid":[],
            # "artist_mbid":[],
            # "genre":[],
            # "artist_bio":[],
            # "location":[],
            # "artist_home_country":[],
            # "lyrics":[],

            ####
        }
    print('reading a file in root directory:', path)
    with open(path) as f:
        count=0
        for line in f:
            count+=1
            if count % 100 == 0:
                print('\r', 'aggregating line',count,  end='')
            try:
                line_obj = json.loads(line)
                data['user_id'].append(line_obj['user_id'])
                data['timestamp'].append(line_obj['timestamp'])
                data['artist_name'].append(line_obj['track_metadata']['artist_name'])
                data['track_name'].append(line_obj['track_metadata']['track_name'])
                data['recording_msid'].append(line_obj['recording_msid'])
                #### for every additional key added, search for the corresponding value here
                # ex. data['track_name'].append(line_obj['track_metadata']['additional_info']['recording_mbid'])

                ####
            except:
                pass
    print()
    return data


# starting to aggregate JSON objects
print('Process started')
pd.DataFrame(get_listens(f'./listenbrainz-listens-dump-789-20220315-040002-full/listens/1970/1.listens')).to_csv('listenbrainz-listens-dump-fullexport.csv')

# inital save
df = pd.read_csv('listenbrainz-listens-dump-fullexport.csv').drop(columns=['Unnamed: 0'])
# aggreagate the rest of the JSON objects
df = pd.concat([df,pd.concat([pd.DataFrame(get_listens(f'./listenbrainz-listens-dump-789-20220315-040002-full/listens/2005/{id}.listens')) for id in [2,3,4,5,6,7,8,9]],axis=0)],axis=0)
# final save
print('saving...')
df.to_csv('listenbrainz-listens-dump-fullexport.csv')
print('done')