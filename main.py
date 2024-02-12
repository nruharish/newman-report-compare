import logging
from config import Config
from log import get_log_level
from os import listdir
from test_report_parser import get_errors
import os
from generate_scan_reports import ScanReport

#constants
LOG_FILE = r'./scanner.log'
DELIMITER = ' --- '

class Scanner :
    def __init__(self):
        self.config = Config()
        log_level = get_log_level(self.config.get_value('log_level'))
        logging.basicConfig(filename=LOG_FILE, encoding='utf-8', level=log_level)
        self.scan_report_gen = ScanReport()

    def run(self):
        logging.error("hello")
        self.analyze_test_reports()

    def compare_errors (self, iter1, iter2, new_failed_tc, new_failed_asserts, change_asserts) :
        result = ()
        print(iter1)
        print(iter2)
        for tckey, tcvalue in iter2.items() :
            if tckey not in iter1:
                new_failed_tc.append(tckey)
            else :
                for askey, asvalue in tcvalue.items() :
                    if askey not in iter1[tckey] :
                        new_failed_asserts.append(tckey + DELIMITER + askey)
                    else:
                        if asvalue != iter1[tckey][askey] :
                            change_asserts.append(tckey + DELIMITER + askey + DELIMITER + asvalue)

    def analyze_test_reports(self) :
        iteration1 = self.config.get_value('previous_run_dir')
        iteration2 = self.config.get_value('current_run_dir')
        for report_file in listdir(iteration1) :
            iter1_errors = {}
            iter2_errors = {}
            new_errors = []
            if '.html' not in report_file :
                continue
            print('processing .. ' + report_file)
            with open(os.path.join(iteration1, report_file)) as it1_f:
                iter1_errors = get_errors(it1_f)
                try :
                    with open(os.path.join(iteration2, report_file)) as it2_f:
                        iter2_errors = get_errors(it2_f)
                except FileNotFoundError: 
                    print("file not found: " + report_file + " Continuing ..")
            if(len(iter2_errors) > 0) :
                new_failed_tc = [] 
                new_failed_asserts = []
                change_asserts = []
                self.compare_errors(iter1_errors, iter2_errors, new_failed_tc, new_failed_asserts, change_asserts)
                self.scan_report_gen.generate_report(report_file, new_failed_tc, new_failed_asserts, change_asserts)

scanner = Scanner()
scanner.run()