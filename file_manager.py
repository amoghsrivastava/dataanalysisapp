# Python library imports
import orjson as j
import json
import os

import numpy as np
import pandas as pd


class FileManager:
    """
    This class provides attributes and methods for a file dataset to be loaded.
    """
    def __init__(self, file_path : str):
        """
        Class constructor which to initialise an object of this class with the path of the file.

        :param file_path: The path of the file used to construct the file manager class.
        """
        self.file_path = file_path

    @property
    def get_file_path(self):
        """:returns: the full path of the file"""
        return self.file_path

    @property
    def get_file_size(self):
        """:returns: the size of the file"""
        return "{:,.0f}".format(os.path.getsize(self.file_path) / float(1 << 20))

    @property
    def get_file_name(self):
        """:returns: the name of the file"""
        return os.path.basename(self.file_path)

    @property
    def get_file_lines(self):
        """
        Gets the number of lines in the file
        :returns: Number of lines of the file.
        """
        count = 0
        try:
            for line in open(self.file_path, encoding="utf-8").readlines():
                count += 1
        except IOError:  # Handle exception if file doesn't exist
            print("File does not exist. Recheck the file path for any typing errors.")
        except Exception as e:  # Handle any exception
            print("Unknown Exception" + str(e))
        return str(count)

    def check_file_format(self):
        """
        Checks the file of a file passed.

        :returns: True if the file is a .json file. False otherwise
        """
        extension = os.path.splitext(self.file_path)[1]
        if extension.lower() == ".json":
            return True
        else:
            return False

    def parse_json_dataframe(self):
        """
        Parses the JSON dataset and reads it into a dataframe.

        :returns: A dataframe with the dataset we will use to analyse.
        """
        # Data types we will use for our columns (Column names as keys and their types as value)
        dtypes = {"visitor_uuid": 'category', "visitor_useragent": "category", "visitor_country": 'category',
                  "subject_doc_id": "category", "event_type": "category", "event_readtime": np.float32}
        # The only columns we want to process in the dataset.
        columns = ["visitor_uuid", "visitor_useragent", "visitor_country", "subject_doc_id", "event_readtime",
                   "event_type"]
        try:
            # Uses the builtin map() function to apply the JSON's load function to the sequence of dictionaries
            # from open(file_path,...) and add each dictionary to the map of iterable list of dictionaries.
            json_records = map(j.loads, open(self.file_path, encoding="utf-8"))
            try:
                # Load the data from the json_records map and use only the specified columns.
                df = pd.DataFrame.from_records(json_records, columns=columns)
                # Convert NaN values of the event_readtime column to 0
                df["event_readtime"] = df["event_readtime"].fillna(0)
                # Set the new datatypes using the dtypes dictionary and return the dataframe
                df = df.astype(dtypes)
                return df
            except json.decoder.JSONDecodeError:  # We expected a dictionaries in the file.
                print("JSON Decode Error: The file doesn't contain the dictionary objects expected.")
                return pd.DataFrame()  # Return empty dataframe
        except IOError:  # If file is missing
            print("File does not exist. Recheck the file path for any typing errors.")
            return pd.DataFrame()
        except Exception as e:  # For any unknown exception, just handle it and return the error.
            print("Unknown Exception" + str(e))

    #
    #
    # ------------------------------------------------------------------------------------------------------------------
    # OLD IMPLEMENTATIONS
    # These should not be used for production stage and is just kept as an archive to remind what solutions were used before.
    # They are not used anywhere.

    def parse_json_dataframe_v2(self):
        """Parses the JSON dataset and reads it into a dataframe"""
        # A dictionary of column and type pairs.
        dtypes = {"visitor_uuid": 'category', "visitor_useragent": "category", "visitor_country": 'category',
                  "subject_doc_id": "category", "event_type": "category", "event_readtime": np.uint16}
        # Before loading, check for if file is valid JSON
        if self.check_file_format():
            # Return a dataframe with selected columns we need for the analysis, and setting types of the data as we defined in dtypes.
            df = pd.read_json(self.file_path, encoding="utf-8", lines=True).loc[:, ["visitor_uuid", "visitor_useragent",
                                                                                    "visitor_country", "subject_doc_id",
                                                                                    "event_readtime", "event_type"]]
            df["event_readtime"] = df["event_readtime"].fillna(0)
            return df.astype(dtypes)
        else:
            return False

    # SLOWEST AND EARLIEST IMPLEMENTATION
    def parse_json_dataframe_v1(self):
        """Parses the JSON dataset and reads it into a dataframe"""
        # Before loading, check for if file is valid JSON
        if self.check_file_format():
            # Return a dataframe
            return pd.read_json(self.file_path, encoding="utf-8", lines=True)
        else:
            return False
