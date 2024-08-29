import google.generativeai as genai
import time
#list of gemini api key that i used
geminiONe= "AIzaSyBXlc2Fv6RijN1S4UYZlc0a4g-FQ3zzCVs" 
geminitwo="AIzaSyCbrSE63bgPaagQISBLrsV3KwKDpJjIuyI"
geminiThree = "AIzaSyDEJ0dzEI31tYYIG7asozrufE7GIxWhSmU"
geminifour = "AIzaSyAN05rbN6CmTq9FxGo34vyajSfKlsZATqE"
geminifive = 'AIzaSyD3q794Bi5NlQPQG9OyMutsNKT1THA87kI'
geminisix = 'AIzaSyDD0BsMjEMC546qebsiaDiahC4lReM6HoM'
ball= "AIzaSyAek2Tdke1ZQDOgmjJGR9G6JnLweovTeUw"
daviddavid="AIzaSyBJ0uqwFw3dm7vzwcclfBfkWHEriFp5vdo"
brendan = "AIzaSyDfw6fPe_k1XrfprpDsDxq3yHPp0ChtA4g"
brendan2 = "AIzaSyAWm8Qak8HYVZx2jHKaAV7yFZdOoa4OEj0"


limit1 = 3000  #process the 3000th to 4500th sets.
limit2 = 4500


element_list2 = []
# model settings
generation_config = {
        "temperature": 0,
        "top_p": 1,
        "top_k": 0,
    }

safety_settings = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
]
model = genai.GenerativeModel(model_name="gemini-1.5-flash", safety_settings=safety_settings, generation_config=generation_config)
from urllib.parse import unquote

seperator = '-' * 40
element_list = []
set_length = 0
sample_number = 3
with open("set_member_larger_6_format_random_first_30000.txt","r") as f:
    first = True
    count = 0
    lin_num = 0
    while True:
        
        lin_num = lin_num+1
        line = f.readline()
        if len(line) == 0:
            break

        else:
            line = line.strip()
            line_list = line.split("|",2)
            set_name = line_list[0]
            if first == True:
                current_set = set_name
                first = False
            element = line_list[1]
            if set_name == current_set:
                element_list.append(element)
                set_length += 1
            else:
                if set_length < (sample_number * 2):
                    pass
                else:
                        count  = count + 1


                        if count <= limit1:  #only read the sets before limit1
                            pass
                        elif count <= limit2:
                            genai.configure(api_key=geminisix) 



                            element_string = f"'''\n"
                            for i in range(sample_number):
                                #add the first three members of the sets for llm to process
                                element_string += f"{element_list[i]}\n"
                            element_string += f"'''"
                            prompt = f"###Your task is to expand a given list with more members.###\nYour output must be in the format of\n'''\nmember1\nmember2\nmember3\nmember4\nmember5\n'''\n\nAll members should belong to the same grouping or class. You must expand the list by at least twice the size of the sample. All members must be different. This is the small sample of a list: \n\n{unquote(element_string)}\n"

                            with open(f"gemini_1.5_flash_output_all_{sample_number}sample_random_{limit1}_{limit2}_first_3_sample.txt","a") as a, open(f"gemini_1.5_flash_output_generated_list_all_{sample_number}sample_{limit1}_{limit2}_first_3_sample.csv","a") as a3,open(f"gemini_1.5_flash_output_stat_all_{sample_number}sample_csv_format_{limit1}_{limit2}_first_3_sample.csv","a") as a4,open(f"gemini_desired_output_{limit1}_{limit2}_first_3_sample.csv","a") as a5,open(f"erro_set_missing_{limit1}_{limit2}_first_3.csv","a") as a6:
                                        a.write(prompt)
                                        a.write(f"\nmodel output:\n")
                                        response = model.generate_content(f"{prompt}")
                                        print(count)
                                        print(current_set)
                                        try:
                                            output = response.text

                                            a.write(f"{output}\n")
                                            a.write(f"\n{seperator}\n")

                                            output_list = output.split("\n")
                                            start = False
                                            end = False
                                            generate_list = []
                                            for line in output_list:
                                                #removed the unwanted line
                                                if "'''" in line:
                                                    pass
                                                elif "```" in line:
                                                    pass
                                                elif line == "":
                                                    pass
                                                elif "-------" in line:
                                                    pass
                                                else:
                                                    generate_list.append(line)

                                            generate_set = set(generate_list)

                                            #get the original sets without the given element
                                            element_list2 = element_list[3:]  
                                            element_set = set(element_list2)

                                            #get their intersection
                                            same_element_set = generate_set.intersection(element_set)
                                            a3.write(f"set name: {current_set}\n")
                                            for i in generate_list:
                                                a3.write(f"{i}\n")
                                                if i in element_list[0:3]:
                                                    a5.write(f"{current_set},{i},I\n")
                                                else:
                                                    a5.write(f"{current_set},{i},O\n")

                                            a3.write(f"{seperator}\n")
                                            
                                            a4.write(f"{current_set},{set_length},{len(generate_set)},{len(same_element_set)},{sample_number}\n")
                                            
                                            time.sleep(4)
                                        except:
                                            a.write(f"{response}\n")
                                            a.write(f"\n{seperator}\n")
                                            a6.write(f"{current_set}\n")
                        else:
                            break

                                    





                            
                                    


                
            
                set_length = 1
                element_list.clear()
                element_list.append(element)
                current_set = set_name
