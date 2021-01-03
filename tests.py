import unittest
import file_manager as fm
import data_processing as prc
import charts as ct
from pandas import testing as pdt
import pandas as pd


class TestFileManager(unittest.TestCase):
    """
    Test class to test the file manager class.
    """
    # PATH TO ISSUU_CW2 DATASET
    path_10 = "C:/Users/amogh/PycharmProjects/dataAnalysis/data/issuu_cw2.json"

    def test_fileformat(self):
        """
        Tests if the file format is returned correctly
        """
        # Create our class objects
        f = fm.FileManager(self.path_10)
        self.assertEqual(f.check_file_format(), True, "Should be True for JSON")

    def test_filename(self):
        """
        Tests if the file name is returned correctly
        """
        # Create our class objects
        f = fm.FileManager(self.path_10)
        self.assertEqual(f.get_file_name, "issuu_cw2.json", "Should be issuu_cw2.json")

    def test_filelines(self):
        """
        Tests if the number of lines in the file are outputted correctly.
        """
        # Create our class objects
        f = fm.FileManager(self.path_10)
        self.assertEqual(f.get_file_lines, "10003", "Should be 10003")

    def test_loading(self):
        """
        Tests if the file dataset is loaded correctly.

        It uses the pandas' library's dataframe testing method assert_frame_equal which compares two dataframes
        which when equal returns OK.

        """
        # Create our class objects
        f = fm.FileManager(self.path_10)
        df_from_method = f.parse_json_dataframe()
        # Load dataframe using read_json and remove some of it's columns and change datatypes.
        dtypes = {"visitor_uuid": 'category', "visitor_useragent": "category", "visitor_country": 'category',
                  "subject_doc_id": "category", "event_type": "category", "event_readtime": "float32"}
        df_from_test = pd.read_json("C:/Users/amogh/PycharmProjects/dataAnalysis/data/issuu_cw2.json", lines=True).loc[
                       :, ["visitor_uuid", "visitor_useragent", "visitor_country", "subject_doc_id", "event_readtime",
                           "event_type"]]
        df_from_test["event_readtime"] = df_from_test["event_readtime"].fillna(0)
        df_from_test = df_from_test.astype(dtypes)
        # Compare left and right dataframes
        pdt.assert_frame_equal(left=df_from_method, right=df_from_test)


class TestDataProcessing(unittest.TestCase):
    """
    Test class to test the DataProcessing class which handles the bulk of the apps requirements.
    All test data and datasets are used from: http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Test_Data/index.html

    """
    # FOR 100K DATASET
    user_id_100 = "00000000deadbeef"
    doc_id_100 = "100806162735-00000000115598650cb8b514246272b5"
    path_100 = "C:/Users/amogh/PycharmProjects/dataAnalysis/data/sample_100k_lines.json"

    # FOR 600K DATASET
    user_id_600 = ""
    doc_id_600 = "140207031738-eb742a5444c9b73df2d1ec9bff15dae9"
    path_600 = "C:/Users/amogh/PycharmProjects/dataAnalysis/data/sample_600k_lines.json"

    def test_graph_100k(self):
        """
        Displays the graph for the first 100k dataset's task 6 test parameters.
        """
        f = fm.FileManager(file_path=self.path_100)
        df = f.parse_json_dataframe()
        p = prc.DataProcessing(df)
        p.run_task_6(self.doc_id_100, self.user_id_100)

    def test_graph_600k(self):
        """
        Displays the graph for the 600k dataset's task 6 test parameters.
        """
        f = fm.FileManager(self.path_600)
        df = f.parse_json_dataframe()
        p = prc.DataProcessing(df)
        p.run_task_6(self.doc_id_600, self.user_id_600)

    def test_also_likes_readers_100k(self):
        """
        Test to see if the readers is as expected for a document and visitor in the 100k dataset.
        """
        f = fm.FileManager(file_path=self.path_100)
        df = f.parse_json_dataframe()
        p = prc.DataProcessing(df)
        # get relevant readers gets a set of readers for a document and user id
        set_readers = p.get_relevant_readers(self.doc_id_100, self.user_id_100)
        set_expected = {'4108dc09bfe11a0c'}  # We expect only 1 reader based on the given test data
        self.assertEqual(set_readers, set_expected, "Should be %s" % set_expected)

    def test_also_likes_readers_600k(self):
        """
        Test to see if the readers is as expected for a document and visitor in the 600k dataset.
        """
        f = fm.FileManager(self.path_600)
        df = f.parse_json_dataframe()
        p = prc.DataProcessing(df)
        # get relevant readers gets a set of readers for a document and user id
        set_readers = p.get_relevant_readers(self.doc_id_600, self.user_id_600)
        # We expect the following 4 readers based on the given test data.
        set_expected = {'383508ea93fd2fd1', '3f64bccfd160557e', '1f891eb0b573e42c', '7134a88f8b201d31'}
        self.assertEqual(set_readers, set_expected, "Should be %s" % set_expected)

    def test_also_likes_documents_100k(self):
        """
        Test to see if the documents is as expected for a document and visitor in the 100k dataset.
        """
        f = fm.FileManager(file_path=self.path_100)
        df = f.parse_json_dataframe()
        p = prc.DataProcessing(df)
        # get relevant readers gets a set of readers for a document and user id
        set_readers = p.get_relevant_readers(self.doc_id_100, self.user_id_100)
        # get the documents that these readers like
        set_docs = p.get_documents(set_readers)
        # We expect only 4 documents based on the given test data
        set_expected = {'4108dc09bfe11a0c': {'100405170355-00000000ee4bfd24d2ff703b9147dd59',
                                             '100806162735-00000000115598650cb8b514246272b5',
                                             '100806172045-0000000081705fbea3553bd0d745b92f',
                                             '101122221951-00000000a695c340822e61891c8f14cf'}}
        self.assertEqual(set_docs, set_expected, "Should be %s" % set_expected)

    def test_also_likes_documents_600k(self):
        """
        Test to see if the documents is as expected for a document and visitor in the 600k dataset.
        """
        f = fm.FileManager(self.path_600)
        df = f.parse_json_dataframe()
        p = prc.DataProcessing(df)
        # get relevant readers gets a set of readers for a document and user id
        set_readers = p.get_relevant_readers(self.doc_id_600, self.user_id_600)
        # get the documents that these readers like
        set_docs = p.get_documents(set_readers)
        # We expect the following 4 readers based on the given test data.
        set_expected = {'1f891eb0b573e42c': {'130308221433-09f8d746cb5e46f79842433817ffa908',
                                             '130322204045-7e140c31b4df4b8da1b0d4a410620ad1',
                                             '130406004921-f9e3072c82364ccfba25da4bc8be3b04',
                                             '130412203635-288742d148524251b4ef59dfaa222008',
                                             '130412215325-b2802be64be04a86b8c67acede394982',
                                             '130517181940-3f89e9f4524d4e769c205ed6f1b0e7ae',
                                             '130601015527-c1e2993d8290975e7ef350f078134390',
                                             '130626002918-2e934fcf5642becffed4c4325fcfa6d8',
                                             '130813183014-f447fd9c4d6abcdfb20e8f0d925c63fd',
                                             '130828160643-3f7e01676f04a2f60d02f80fcbd702e1',
                                             '130829034400-ae346135ab80c636d6d7b4c0f7960c41',
                                             '130829155547-4da063e3c66df0bc6149aced2abc3720',
                                             '130930182254-898ec9d4d3724afb31b1168517d4228a',
                                             '131004224723-076660492fa2c66e5398e3dde8890d73',
                                             '131022215916-907a48e13645fa9a81860efd03e85352',
                                             '140207031738-eb742a5444c9b73df2d1ec9bff15dae9'},
                        '383508ea93fd2fd1': {'130412203635-288742d148524251b4ef59dfaa222008',
                                             '130412215325-b2802be64be04a86b8c67acede394982',
                                             '130601015527-c1e2993d8290975e7ef350f078134390',
                                             '130828160643-3f7e01676f04a2f60d02f80fcbd702e1',
                                             '130930182254-898ec9d4d3724afb31b1168517d4228a',
                                             '131022215916-907a48e13645fa9a81860efd03e85352',
                                             '140207031738-eb742a5444c9b73df2d1ec9bff15dae9'},
                        '3f64bccfd160557e': {'130406004921-f9e3072c82364ccfba25da4bc8be3b04',
                                             '130601015527-c1e2993d8290975e7ef350f078134390',
                                             '130626002918-2e934fcf5642becffed4c4325fcfa6d8',
                                             '130813183014-f447fd9c4d6abcdfb20e8f0d925c63fd',
                                             '130828160643-3f7e01676f04a2f60d02f80fcbd702e1',
                                             '130829034400-ae346135ab80c636d6d7b4c0f7960c41',
                                             '131030220741-ce78b0b193120c40fd3916fb616b63ce',
                                             '140207031738-eb742a5444c9b73df2d1ec9bff15dae9'},
                        '7134a88f8b201d31': {'130308221433-09f8d746cb5e46f79842433817ffa908',
                                             '130322204045-7e140c31b4df4b8da1b0d4a410620ad1',
                                             '130626002918-2e934fcf5642becffed4c4325fcfa6d8',
                                             '130813183014-f447fd9c4d6abcdfb20e8f0d925c63fd',
                                             '130829155547-4da063e3c66df0bc6149aced2abc3720',
                                             '130930182254-898ec9d4d3724afb31b1168517d4228a',
                                             '131022215916-907a48e13645fa9a81860efd03e85352',
                                             '131030220741-ce78b0b193120c40fd3916fb616b63ce',
                                             '140207031738-eb742a5444c9b73df2d1ec9bff15dae9'}}
        self.assertEqual(set_docs, set_expected, "Should be %s" % set_expected)

    def test_format_time(self):
        """Tests if the time is formatted correctly
        We test the seconds converted by this tool.
        test data: 1234567800
        source tool: https://www.convert-me.com/en/convert/time/millisecond/millisecond-to-dhms.html?u=millisecond&v=1%2C234%2C567%2C800
        """
        f = fm.FileManager(file_path=self.path_100)
        df = f.parse_json_dataframe()
        p = prc.DataProcessing(df)
        actual = p._format_time(1234567800) # 1234567800ms is 14 days 6 hours 56 minutes 7 seconds
        expected = "14d : 6h : 56m : 7s"
        self.assertEqual(actual, expected, "Should be %s" % expected)


class TestCharts(unittest.TestCase):
    """
    Test class to test the charts class.
    """
    # PATH TO ISSUU_CW2 DATASET
    file = {'a': 10, 'b': 120, 'c': 1, 'd': 5}

    def test_plotting(self):
        """
        Tests if the graph is plotted as expected for a given dictionary of
        keys with data point and its values with frequency values.

        """
        # Create a chart object of the charts class which we would plot
        chart = ct.Charts(self.file, "Graph title", "x axis label", "y axis label")
        # Plot the graph for the object
        chart.plot_histogram()


if __name__ == '__main__':
    unittest.main()
