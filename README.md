The code in caligraph are used to extract sets and its member from the file "caligraph-instances_types.nt.bz2" in caligraph. I first decompress it then run the python code.

For wikidata, I first run the preprocess_dump.py with the wikidata dump that I downloaded. Then I used those "fetch" files to get te property or label that I want.
For sorting and mapping I import the csv to sqlite so no python code is used.

Before given to llm, all the list are unquote by this python code from urllib.parse import unquote and '_' are replace by space.

set_member_larger_6_format_random_first_30000.txt in google drive inside the llm_output folder are needed to run with the python code that input to LLM.


The gemini_first_three_sample.py and gemini_three_six_sample.py are used to input to gemini with 1500 sets a time. I run these with all the samples by changeging the limit1 and limit2.


After running all the sets, you need to combine the gemini_desired_output_{limit1}_{limit2}_diff_sample.csv to get the list that generated.
And combine the gemini_1.5_flash_output_stat_all_{sample_number}sample_csv_format_{limit1}_{limit2}_diff_sample.csv for the stats for the sets that have generated.
Then I import it to sqlite database and sort it, when sorting, cast the the things you need to sort to integer as it is import as a text.

To run the llama model, you have to run pip install gpt4all in terminal first.
The llama.py run about 2-3 days on my computer.





