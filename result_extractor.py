import re
import urllib
import re
from mechanize import Browser

branches = ['EC','CS','IS','EE','ME']
batch = '09'

for z in branches[:]:
  for x in range(0,5):
    for y in range(0,10):
	br = Browser()
	br.open("http://results.vtu.ac.in//")
	br.select_form(name="new")
	br["rid"] = "4VM"+batch+z+str(0)+str(x)+str(y)  # (the method here is __setitem__)
	response = br.submit()  # submit current form
	html_result = response.read()

	regex = '(.+?)<table>(.+?)</table>'
	pattern = re.compile(regex)
	student_data = str(re.findall(pattern,html_result))

	stripped_data = student_data.replace('td','').replace('tr','').replace('width=60','').replace('align=center','').replace('<','').replace('>','').replace('width=250','').replace('/','').replace('bPb','').replace('&nbsp;','').replace('Bbrbrbrbrhr','').replace('br','\n')

# while (i < len(stripped_data)) : 
       
	print stripped_data
	print "\n==============================================================================\n"

 


