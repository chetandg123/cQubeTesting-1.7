import unittest

from Composite_report.check_blockwise_records import composite_blockwise_records
from Composite_report.check_clusterwise_records import composite_schoolevel_records
from Composite_report.check_districtwise_records import test_composite_report_districtwise
from Composite_report.check_homebtn import Homebutton_icon
from Composite_report.check_xaxis_and_yaxis_from_selectbox import test_Graph
from Composite_report.click_on_block_cluster_school_buttons import Blocks_cluster_schools_Buttons

from Composite_report.click_on_hyperlink import click_on_hyperlinks
from Composite_report.download_blockwise_csv import download_blockwise_csv
from Composite_report.download_clusterwise_csv import download_clusterwise_csv
from Composite_report.download_districtwise_csv import Districtwise_download
from Composite_report.download_schoolwise_csv import school_wise_download

from Data.parameters import Data
from reuse_func import GetData


class composite_report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(50)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_composite_report()
        self.data.page_loading(self.driver)

    def test_navigate_composite(self):
        self.data.page_loading(self.driver)
        count = 0
        if 'composit-report' in self.driver.current_url:
            print("Composite report is present ")
        else:
            print("Composite report is not displayed ")
            count = count + 1
        self.assertEqual(0,count,msg="Composite report is not present ")
        self.data.page_loading(self.driver)

    def test_composite_icon(self):
        self.data.page_loading(self.driver)
        count = 0
        self.driver.find_element_by_id(Data.home).click()
        self.data.page_loading(self.driver)
        if 'home' in self.driver.current_url:
            print("Landing page is displayed ")
        else:
            print('Home button is not working ')
            count = count + 1
        self.assertEqual(0,count,msg="Home btn is not working ")
        self.driver.find_element_by_id('composit').click()
        self.data.page_loading(self.driver)

    def test_graph_on_report(self):
        self.data.page_loading(self.driver)
        graph = self.driver.find_element_by_id('myChart')
        self.assertTrue(graph.is_displayed(),msg='Graph is not present')
        print("Checked with Graph on composite report ")

    def test_districtwise_csv_download(self):
        b = Districtwise_download(self.driver)
        res = b.test_districtwise()
        self.assertTrue(res,msg="Districtwise csv file is not downloaded ")
        print("Checked district wise csv downloading functionality is working ")
        b.remove_csv()
        self.data.page_loading(self.driver)

    def test_blockwise_csv_download(self):
        b = download_blockwise_csv(self.driver)
        res = b.test_blockwise()
        self.assertTrue(res,msg="Blockwise csv file is not downloaded ")
        print("Checked block wise csv downloading functionality is working ")
        b.remove_file()
        self.data.page_loading(self.driver)

    def test_clusterwise_csv_download(self):
        b = download_clusterwise_csv(self.driver)
        res = b.test_clusterwise()
        self.assertTrue(res, msg="Clusterwise csv file is not downloaded ")
        print("Checked cluster wise csv downloading functionality is working ")
        b.remove_file()
        self.data.page_loading(self.driver)

    def test_school_wise_download(self):
        b = school_wise_download(self.driver)
        res = b.test_schoolwise()
        self.assertTrue(res, msg="Schoolwise csv file is not downloaded ")
        print("Checked school wise csv downloading functionality is working ")
        b.remove_file()
        self.data.page_loading(self.driver)

    def test_test_districtwise(self):
        b = test_composite_report_districtwise(self.driver)
        res = b.test_districtwise()
        self.assertTrue(res,msg="Some of district csv file is not downloaded ")
        print("Checked with district wise csv file downloading ")
        self.data.page_loading(self.driver)

    def test_composite_blockwise_records(self):
        b = composite_blockwise_records(self.driver)
        res = b.test_blockwise()
        self.assertTrue(res, msg="Some of blocks csv file is not downloaded ")
        print("Checked with Block wise csv file downloading ")
        self.data.page_loading(self.driver)

    def test_composite_schoolwise_records(self):
        b = composite_schoolevel_records(self.driver)
        res = b.check_csv_download()
        self.assertTrue(res, msg="Some of school csv file is not downloaded ")
        print("Checked with School wise csv file downloading ")
        self.data.page_loading(self.driver)

    def test_hyperlink(self):
        b = click_on_hyperlinks(self.driver)
        res = b.test_hyperlink()
        print("Checked with hyper link ")
        self.data.page_loading(self.driver)

    def test_xaxis_selectbox(self):
        b = test_Graph(self.driver)
        res = b.test_xaxis()
        self.assertNotEqual(0,res,msg="X-axis dropdown does not have options")
        print("Xaxis having options ")
        self.data.page_loading(self.driver)


    def test_yaxis_selectbox(self):
        b = test_Graph(self.driver)
        res = b.test_yaxis()
        self.assertNotEqual(0,res,msg="Y-axis dropdown does not have options")
        print("Yaxis having options ")
        self.data.page_loading(self.driver)

    def test_xaxis_options(self):
        b = test_Graph(self.driver)
        res = b.test_xplots()
        print("Checked with all xaxis options are selectable")
        self.data.page_loading(self.driver)

    def test_yaxis_options(self):
        b = test_Graph(self.driver)
        res = b.test_yplots()
        print("Checked with all yaxis options are selectable")
        self.data.page_loading(self.driver)

    def test_Homeicon(self):
        b = Homebutton_icon(self.driver)
        res = b.test_homeicon()
        print("Homeicon is working fine ")
        self.data.page_loading(self.driver)

    def test_homebutton(self):
        b = Homebutton_icon(self.driver)
        res = b.test_homebutton()
        self.assertEqual(0,res,msg="Home button is not working")
        print("Home button is working ")
        self.data.page_loading(self.driver)

    def test_logout_button(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.logout).click()
        self.data.page_loading(self.driver)
        self.assertEqual('Log in to cQube',self.driver.title,msg="Logout button is not working ")
        print("logout button is working fine ")
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_composite_report()
        self.data.page_loading(self.driver)

    def test_clicking_blocks(self):
        b = Blocks_cluster_schools_Buttons(self.driver)
        res = b.click_on_blocks_button()
        self.assertEqual(0,res,msg="Blocks graph is displayed ")
        print("Block wise graph is displayed ")
        self.data.page_loading(self.driver)

    def test_clicking_cluster(self):
        b = Blocks_cluster_schools_Buttons(self.driver)
        res = b.click_on_clusters_button()
        self.assertEqual(0, res, msg="Cluster graph is displayed ")
        print("Cluster wise graph is displayed ")
        self.data.page_loading(self.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

