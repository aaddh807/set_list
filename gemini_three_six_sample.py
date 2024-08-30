import google.generativeai as genai
import time

#list of gemini api key that i used
geminisix = "input your api key here"


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
                                #add the  three to six members of the sets for llm to process
                                element_string += f"{element_list[i+3]}\n"
                            element_string += f"'''"
                            prompt = f"###Your task is to expand a given list with more members.###\nYour output must be in the format of\n'''\nmember1\nmember2\nmember3\nmember4\nmember5\n'''\n\nAll members should belong to the same grouping or class. You must expand the list by at least twice the size of the sample. All members must be different. This is the small sample of a list: \n\n{unquote(element_string)}\n"

                            with open(f"gemini_1.5_flash_output_all_{sample_number}sample_random_{limit1}_{limit2}_diff_sample.txt","a") as a, open(f"gemini_1.5_flash_output_generated_list_all_{sample_number}sample_{limit1}_{limit2}_diff_sample.csv","a") as a3,open(f"gemini_1.5_flash_output_stat_all_{sample_number}sample_csv_format_{limit1}_{limit2}_diff_sample.csv","a") as a4,open(f"gemini_desired_output_{limit1}_{limit2}_diff_sample.csv","a") as a5,open(f"erro_set_missing_{limit1}_{limit2}_diff_sample.csv","a") as a6:
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
                                            element_list2 = element_list[0:3] + element_list[6:]  
                                            element_set = set(element_list2)

                                            #get their intersection
                                            same_element_set = generate_set.intersection(element_set)
                                            current_set_final = ''
                                            for character in current_set:
                                                if character == '"':
                                                    current_set_final = current_set_final + character + '"'
                                                else:
                                                    current_set_final = current_set_final + character
                                            if ',' in current_set_final or '"' in current_set_final:
                                                    current_set_final = f'"{current_set_final}"'
                                            a3.write(f"set name: {current_set}\n")
                                            for generated_element in generate_list:
                                                element_final = ''
                                                a3.write(f"{generated_element}\n")
                                                if generated_element in element_list[3:6]:
                                                    for character in generated_element:
                                                        if character == '"':
                                                            element_final = element_final + character + '"'

                                                        else:
                                                            element_final = element_final + character
                                                    
                                                    if ',' in element_final or '"' in element_final:
                                                        element_final = f'"{element_final}"'
                                                    
                                                    a5.write(f"{current_set_final},{element_final},I\n")
                                                else:
                                                    for character in generated_element:
                                                        if character == '"':
                                                            element_final = element_final + character + '"'

                                                    else:
                                                            element_final = element_final + character
                                                    
                                                    if ',' in element_final or '"' in element_final:
                                                        element_final = f'"{element_final}"'
                                                    a5.write(f"{current_set_final},{element_final},O\n")

                                            a3.write(f"{seperator}\n")

                                            a4.write(f"{current_set_final},{set_length},{len(generate_set)},{len(same_element_set)},{sample_number}\n")
                                            
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
