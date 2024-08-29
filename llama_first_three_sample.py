from gpt4all import GPT4All
from urllib.parse import unquote
c = 0
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
seperator = '-' * 40
element_list = []
set_length = 0
sample_number = 3
i = 0
first = True
element_list2 = []

with open("set_member_larger_6_format_random_first_30000.txt","r") as f:

    while True:
        line = f.readline()
        if len(line) == 0:
            print("EOF")
            break



        
        
            
            

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
            print(current_set)
            if set_length < (sample_number*2):

                pass
            else:   






                    
                    element_string = f"'''\n"
                    for g in range(sample_number):
                        element_string += f"{element_list[g+3]}\n"
                    element_string += f"'''"
                    prompt = f"###Your task is to expand a given list with more members.###\nYour output must be in the format of\n'''\nmember1\nmember2\nmember3\nmember4\nmember5\n'''\n\nAll members should belong to the same grouping or class. You must expand the list by at least twice the size of the sample. All members must be different. This is the small sample of a list: \n\n{unquote(element_string)}\n"
                    with model.chat_session():
                        with open(f"llama3_8b_instruct_output_all_{sample_number}sample_random_first_3_sample.txt","a") as a, open(f"llama3_8b_instruct_output_stat_all_{sample_number}sample_random_first_3_sample.csv","a") as a2,open(f"llama3_8b_instruct_output_generated_list_all_{sample_number}sample_random_first_3_sample.csv","a") as a3, open(f"llama3_8b_instruct_output_stat_all_{sample_number}sample_csv_format_random_first_3_sample.csv","a") as a4, open(f"llama3_8b_instruct_output_desire_output_first_3_sample.csv","a") as a5:
                            a.write(prompt)
                            a.write(f"\nmodel output:\n")
                            output = model.generate(prompt, max_tokens=2048)
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
                                
                                    
                            element_set = set(element_list2)

                            same_element_set = generate_set.intersection(element_set)
                            a3.write(f"set name: {current_set}\n")
                            for b in generate_list:
                                if b in element_list[0:3]:
                                    a5.write(f"{current_set},{b},I\n")
                                else:
                                    a5.write(f"{current_set},{b},O\n")


                                a3.write(f"{b}\n")
                            a3.write(f"{seperator}\n")
                            a2.write(f"set name: {current_set}, set length: {set_length}, generated set length:{len(generate_set)}, number of same element: {len(same_element_set)}, sample number give to llm: {sample_number}\n")
                            a4.write(f"{current_set},{set_length},{len(generate_set)},{len(same_element_set)},{sample_number}\n")




                    
                            


        

            set_length = 1
            element_list.clear()
            element_list.append(element)
            current_set = set_name
            
        





        

        
