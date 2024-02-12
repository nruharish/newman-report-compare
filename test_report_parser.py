from bs4 import BeautifulSoup

def get_errors(fp):
    errors = {}
    full_html = BeautifulSoup(fp, 'html.parser')
    #for test_case in full_html.find_all('div', {'class' : ['card-deck', 'iteration-0']}):
    for test_case in full_html.select('div.card-deck.iteration-0'):
        tc = test_case.find('div', {'class': ['card-header', 'bg-danger', 'iteration-0']})
        if tc is not None:
            tc_title = tc.find('a')
            if tc_title is not None :
                failed_assertion_name = test_case.find_all('td', {'class':'w-45'})
                failed_assertion_text = test_case.find_all('td', {'class':'w-55'})
                test_case = tc_title.text.strip()
                if(len(failed_assertion_name)) :
                    errors[test_case]= {}
                for i, element in enumerate(failed_assertion_name) :
                    #errors[test_case].append({failed_assertion_name[i].text: failed_assertion_text[i].text})
                    errors[test_case][failed_assertion_name[i].text] = failed_assertion_text[i].text
    return errors
