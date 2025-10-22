import requests, json
import data_extration
import time
import notification

# scarpe data from different link using get api 
def scrape_data(url, name):
    
        response = requests.get(url, stream=True)
        if response.status_code==200:
            with open(name, "wb") as f:
                for chunck in response.iter_content(chunk_size=1024):
                    if chunck:
                        f.write(chunck)
            print("Download Successful", time.ctime())
        else:
            print("failed to download", response.status_code)
            notification.send_notification("Failed to Download File", f"Response status is {response.status_code} and Download Link is {url} \n Error is {response.text}")
            
    
        
    
    
def call_scrape_funtion():
    
    try:
        # nested dict 
        DOCUMENT_MAP= {
            # key : value  = {}
            "DPA": {"json_file":"json_files/dpa.json", "link":r"https://www.benchmarkone.com/wp-content/uploads/2018/05/GDPR-Sample-Agreement.pdf"},
            "JCA": {"json_file":"json_files/jca.json", "link":r"https://www.surf.nl/files/2019-11/model-joint-controllership-agreement.pdf"},
            "C2C":{"json_file":"json_files/c2c.json", "link":r"https://www.fcmtravel.com/sites/default/files/2020-03/2-Controller-to-controller-data-privacy-addendum.pdf"},    
            "SCC":{"json_file":"json_files/scc.json", "link":r"https://www.miller-insurance.com/assets/PDF-Downloads/Standard-Contractual-Clauses-SCCs.pdf"},    
            "subprocessing":{"json_file":"json_files/subprocessing.json", "link":r"https://greaterthan.eu/wp-content/uploads/Personal-Data-Sub-Processor-Agreement-2024-01-24.pdf"}    
        }
        
        temp_agreement= "temp_agreement.pdf"
        
        for key, value in DOCUMENT_MAP.items():
            # dealing with DPA agreement only
            scrape_data(DOCUMENT_MAP[key]["link"], temp_agreement)
            
            # clauses = data_extration.Clause_extraction(temp_agreement)
            
            # Step 6: Update respective json file with new clauses (dpa.json)
            # with open(DOCUMENT_MAP[key]["json_file"], "w", encoding="utf-8") as f:
            #     json.dump(clauses, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Error Occured in Scraping", e)
        notification.send_notification("Error Occured in Scraping",f"Error is {e}")
            
# call_scrape_funtion()