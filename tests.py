from music_tracks import MusicTracks

def test_where_returns_tracks_per_album():
  assert len(MusicTracks.where({'album_title': 'Kung Flu'})) == 5

def test_where_returns_correct_keys():
  row = MusicTracks.where({'album_title': 'KONTRAST'})[0]
  keys = ['track_id', 'album_id', 'album_title', 'album_url', 'artist_id', 'artist_name', 'artist_url', 'track_date_created', 'track_duration', 'track_listens', 'track_title', 'track_url']
  values = ['56482', '10439', 'KONTRAST', 'http://freemusicarchive.org/music/KVZE/KONTRAST/', '12270', 'KVZE', 'http://freemusicarchive.org/music/KVZE/', '11/16/2011 03:54:59 PM', '02:21', '1047', 'Scotch', 'http://freemusicarchive.org/music/KVZE/KONTRAST/08_kvze_-_scotch']
  for i in range(0, len(keys)):
    assert row[keys[i]] == values[i]

def test_where_returns_tracks_by_artist_name():
  assert len(MusicTracks.where({'artist_name': 'The Loving Knives'})) == 6

def test_where_returns_tracks_by_listens():
  assert len(MusicTracks.where({'track_listens': '842'})) == 4

def test_where_returns_tracks_by_title():
  assert len(MusicTracks.where({'track_title': 'Introduction'})) == 2

def test_where_returns_no_tracks():
  assert len(MusicTracks.where({'track_title': 'NotExistentTitle'})) == 0

def test_find_by_track_id():
  row = MusicTracks.find_by_id({'track_id': '143342'})
  keys = ['track_id', 'album_id', 'album_title', 'album_url', 'artist_id', 'artist_name', 'artist_url', 'track_date_created', 'track_duration', 'track_listens', 'track_title', 'track_url']
  values = ['143342', '21515', 'Timethod', 'http://freemusicarchive.org/music/Ars_Sonor__Total_ET/Timethod/', '22800', 'Ars Sonor & Total E.T.', 'http://freemusicarchive.org/music/Ars_Sonor__Total_ET/', '9/21/2016 05:23:45 AM', '01:40', '5168', 'Intro', 'http://freemusicarchive.org/music/Ars_Sonor__Total_ET/Timethod/01-Intro_1074']
  for i in range(0, len(keys)):
    assert row[keys[i]] == values[i]

def test_find_by_album_id():
  row = MusicTracks.find_by_id({'album_id': '21390'})
  keys = ['track_id', 'album_id', 'album_title', 'album_url', 'artist_id', 'artist_name', 'artist_url', 'track_date_created', 'track_duration', 'track_listens', 'track_title', 'track_url']
  values = ['142485', '21390', 'Sanctuary', 'http://freemusicarchive.org/music/Artem_Bemba/Sanctuary/', '20476', 'Artem Bemba', 'http://freemusicarchive.org/music/Artem_Bemba/', '9/03/2016 04:14:26 AM', '13:24', '1900', 'Flour', 'http://freemusicarchive.org/music/Artem_Bemba/Sanctuary/Artem_Bemba_-_01_-_Flour']
  for i in range(0, len(keys)):
    assert row[keys[i]] == values[i]

def test_find_by_artist_id():
  row = MusicTracks.find_by_id({'artist_id': '11070'})
  keys = ['track_id', 'album_id', 'album_title', 'album_url', 'artist_id', 'artist_name', 'artist_url', 'track_date_created', 'track_duration', 'track_listens', 'track_title', 'track_url']
  values = ['143654', '21538', 'Necktar Volume 2', 'http://freemusicarchive.org/music/Subversive_Intentions/Volume_2_1042/', '11070', 'Subversive Intentions', 'http://freemusicarchive.org/music/Subversive_Intentions/', '9/26/2016 05:36:34 AM', '10:28', '13', 'Permanentpress', 'http://freemusicarchive.org/music/Subversive_Intentions/Volume_2_1042/23_-_Permanentpress']
  for i in range(0, len(keys)):
    assert row[keys[i]] == values[i]

def test_get_top_ten_most_listened_tracks():
  rows = MusicTracks.get_top_ten_most_listened_tracks()
  values = [491235, 158793, 108682, 92059, 89844, 89302, 77324, 68234, 66866, 61303]
  assert len(rows) == 10
  n = 0
  for row in rows:
    assert row[9] == values[0]
    n = n + 1


test_where_returns_tracks_per_album()
test_where_returns_correct_keys()
test_where_returns_tracks_by_artist_name()
test_where_returns_tracks_by_listens()
test_where_returns_tracks_by_title()
test_where_returns_no_tracks()
test_find_by_track_id()
test_find_by_album_id()
test_find_by_artist_id()
