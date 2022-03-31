# DL ListenBrainz Recommendation

DL ListenBrainz Recommendation is a personal project notebook for the UPF-MTG Music Information Retrieval Course Final Project utilizing [tensorflow-recommenders](https://github.com/topics/tensorflow-recommenders). The data does not utilize api calls to aggregate Listenbrainz information (not yet at least), rather the repository is lacking the full export data dump download found here on ListenBrainz.

The objective of this notebook is to generate a working example of how it is possible to improve recommendation of songs to users by incorporating more contextual information of the listening session. These contextual pieces of information can include, the time features of the listen, the audio features from the song listened to, and the metadata from the song listened to.

## How to Use

Firstly, go to the [ListenBrainz full export downloads](http://ftp.musicbrainz.org/pub/musicbrainz/listenbrainz/fullexport/listenbrainz-dump-789-20220315-040002-full/) and download `listenbrainz-dump-789-20220315-040002-full.tar`. **Warning:** it is in fact around 39 GB that you will need to download and unzip inside the project directory.

Upon unzipping the folder, you are all set to begin running the notebook, which will parse the folder and aggregate all the information neccessary to run the notebook.

If you are interested in the project, feel free to read the project report as well.