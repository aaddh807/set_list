The gemini_first_three_sample.py and gemini_three_six_sample.py are used to input to gemini with 1500 sets a time. I run these with all the samples by changeging the limit1 and limit2.
After running all the sets, you need to combine the gemini_desired_output_{limit1}_{limit2}_diff_sample.csv to get the list that generated.
And combine the gemini_1.5_flash_output_stat_all_{sample_number}sample_csv_format_{limit1}_{limit2}_diff_sample.csv for the stats for the sets that have generated.


Then I import it to sqlite database and sort it, when sorting, cast the the things you need to sort to integer as it is import as a text.



To run the llama model, you have to run pip install gpt4all in terminal first.
