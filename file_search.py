import os
import json
import datetime
import time


class FileSearch:
    def __init__(
        self,
        path,
        keywords,
        start="1990-01-01",
        end="2030-01-01",
    ) -> None:
        self.path = path
        self.keywords = keywords
        self.start = start
        self.end = end

    def convert_date(self, date):
        date_format = "%Y-%m-%d"
        my_date = datetime.datetime.strptime(date, date_format)
        timestamp = time.mktime(my_date.timetuple())

        return timestamp

    def file_search(self):
        # Check dates and if not default convert to UNIX format
        start_date = self.convert_date(self.start)
        end_date = self.convert_date(self.end)

        # Empty list to hold files that meet date criteria
        daterange_files = []

        # Loop through DIRs to find files that meet the date criteria and save as list
        for root, dirs, files in os.walk(self.path):
            for f in files:
                try:
                    if (
                        os.path.getctime(root + "\\" + f) >= start_date
                        and os.path.getctime(root + "\\" + f) <= end_date
                    ):
                        daterange_files.append(root + "\\" + f)
                except FileNotFoundError:
                    pass

        # Store the files that meet the date criteria in a JSON file
        files_by_date = "date_files.json"
        with open(files_by_date, "w") as f:
            json.dump(daterange_files, f)

        # Load the json file to read each file
        file_has_keyword = []

        files_to_be_read = "date_files.json"
        with open(
            files_to_be_read,
        ) as f:
            reading_files = json.load(f)
            print(f"READING FILES {reading_files}")

        for i in range(len(reading_files)):
            try:
                with open(reading_files[i]) as f:
                    contents = f.read().lower()

                    for word in self.keywords:
                        if word in contents:
                            file_has_keyword.append(f.name)

            except FileNotFoundError:
                pass

        # Dump list of files that contain the keyword into JSON file
        keyword_json_file = "keyword_file.json"
        with open(keyword_json_file, "w") as f:
            json.dump(file_has_keyword, f)


# search1 = FileSearch(
#     "c:\\users\\mfouq\\Documents",
#     ["key1", "key2", "key3", "key4", "key5"],
#     "2023-07-07",
# )
# search1.file_search()
