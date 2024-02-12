from config import Config
import os

class ScanReport():

    def __init__(self):
        config = Config()
        self.scan_report_file = config.get_value('report_file')
        if os.path.exists(self.scan_report_file):
            os.remove(self.scan_report_file)

    def generate_report(self, report_file, new_failed_tc, new_failed_asserts, change_asserts) :
        if new_failed_tc or new_failed_asserts or change_asserts :
            with open(self.scan_report_file, 'a') as f :
                f.write('File: ' + report_file + '\n')
                for tc in new_failed_tc :
                    f.write('Failed TC: ' + tc + '\n')
                for new_assert in new_failed_asserts:
                    f.write('Failed Assertions: ' + new_assert + '\n')
                for ca in change_asserts:
                    f.write('Changed Assertions: ' + ca + '\n')
                f.write('\n\n')  
           




    