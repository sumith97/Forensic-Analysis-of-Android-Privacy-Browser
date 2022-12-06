import xlsxwriter
import subprocess

browsers=["Firefoxfocus","Chrome_Default","Chrome_Incognito","Tor","Dolphin","Brave","Opera","Firefox"]
search_list=["yahoo.com","twitter.com","nytimes.com","2700chess.com","wikipedia.org","uselessweb.com","reddit.com","duckduckgo.com","yandex.com","bing.com","youtube.com","anonymous2_email_research_test","continental2_email_research_test","private2_email_research_test","Content_search_research_test","Convict_search_research_test","Symptom_search_research_test","Deprive_search_research_test","Nightmare_search_research_test","Flood_search_research_test","Craftsman_search_research_test","Tolerate_search_research_test","Flow_search_research_test","Spill_search_research_test","Intrusion_search_research_test","Infiltrate_search_research_test","Conclude_search_research_test","Confirm_search_research_test"]
file_list=["domain_histogram.txt","domain.txt","email_domain_histogram.txt","email_histogram.txt","email.txt","json.txt","url_searches.txt","url_services.txt","sqlite_carved","url_histogram.txt","url.txt"]

workbook=xlsxwriter.Workbook('Browser Artifacts.xlsx')
for i in range(len(browsers)):
	print(f"<-----------------------------------------{browsers[i]}---------------------------------------------->")
	print("Collecting Data Artifcats...........")
	worksheet=workbook.add_worksheet(browsers[i])
	worksheet.write('B1','domain_histogram.txt')
	worksheet.write('C1','domain.txt')
	worksheet.write('D1','email_domain_histogram.txt')
	worksheet.write('E1','email_histogram.txt')
	worksheet.write('F1','email.txt')
	worksheet.write('G1','json.txt')
	worksheet.write('H1','url_searches.txt')
	worksheet.write('I1','url_services.txt')
	worksheet.write('J1','sqlite_carved')
	worksheet.write('K1','url_histogram.txt')
	worksheet.write('L1','url.txt')
	for j in range(len(search_list)):
		print(f"Started {search_list[j]}")
		worksheet.write(j+1,0,search_list[j])
		for k in range(len(file_list)):
			data=subprocess.check_output(f"grep -a -R {search_list[j]} {browsers[i]} | cut -d : -f -1 | grep {file_list[k]} | sort -d | wc -l",shell=True)
			value=int(data.decode("utf-8"))
			worksheet.write(j+1,k+1,value)
		print(f"Completed {search_list[j]}")

workbook.close()
