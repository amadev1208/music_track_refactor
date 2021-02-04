import csv

# Constants CSV fields (as it is constant, made it as tuple)
# Fields should be in order as they are in the csv files for further maintenance
CSV_FIELDS = \
    (
        'track_id',
        'album_id',
        'album_title',
        'album_url',
        'artist_id',
        'artist_name',
        'artist_url',
        'track_date_created',
        'track_duration',
        'track_listens',
        'track_title',
        'track_url',
    )


class MusicTracks:
    @staticmethod
    def where(options={}):
        field_to_find, field_index = Utils.check_fields(options)

        output = []
        data = Utils.get_csv_data()
        for row in data:
            if row[field_index] == options[field_to_find]:
                mapped = {}
                n = 0
                for field in CSV_FIELDS:
                    mapped[field] = row[n]
                    n = n + 1

                output.append(mapped)

        return output

    @staticmethod
    def find_by_id(options):
        field_to_find, field_index = Utils.check_fields(options)
        data = Utils.get_csv_data()
        # find the record by field id not just three ids
        # that were implemented before (for further maintenance)
        for row in data:
            if row[field_index] == options[field_to_find]:
                mapped = {}
                n = 0
                for field in CSV_FIELDS:
                    mapped[field] = row[n]
                    n = n + 1

                return mapped

        raise RecordNotFound

    @staticmethod
    def get_top_ten_most_listened_tracks():
        options = {'track_listens': '0'}
        field_to_find, field_index = Utils.check_fields(options)
        data = Utils.get_csv_data(field_index)
        sorted_list = sorted(data, key=lambda k: k[9], reverse=True)

        return sorted_list[0:10]


class RecordNotFound(Exception):
    pass


class Utils:
    @staticmethod
    def check_fields(options: dict):
        # check if the field(to find) exists in the csv fields and find its index
        field_to_find = None
        field_index = 0
        for field in CSV_FIELDS:
            if field in options:
                field_to_find = field
                break
            field_index = field_index + 1

        if not field_to_find:
            raise RecordNotFound

        return field_to_find, field_index

    @staticmethod
    def get_csv_data(field_index_to_convert_to_int: int = -1):
        # field_index_to_convert_to_int: Convert string to int for that specific field
        # To get top ten most records sth like by track_listens
        with open("./tracks.csv", "rt") as csv_file:
            data = csv.reader(csv_file, delimiter=',', quotechar='"')
            csv_data = []
            for row in data:
                if field_index_to_convert_to_int != -1:
                    try:
                        row[field_index_to_convert_to_int] = int(row[field_index_to_convert_to_int])
                    except ValueError:
                        row[field_index_to_convert_to_int] = 0

                csv_data.append(row)

        return csv_data
