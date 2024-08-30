"""
This script fetches all QIDs which have a relationship with a specific value. 

For example: all entities which played 'quarterback' on a football team (corresponding to P413 and a value of Q622747)

to run: 
python3.6 fetch_with_rel_and_value.py --data $DATA --out_dir $OUT
"""

import argparse
from tqdm import tqdm
from multiprocessing import Pool
from functools import partial

from utils import jsonl_generator, get_batch_files


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='entity_rels', help='path to output directory')
    parser.add_argument('--rel', type=str, default='P413', help='relationship')
    parser.add_argument('--entity', type=str, default='Q622747', help='entity value')
    return parser


def filtering_func(rel,entity,filename):
    P31 = []
    P279 = []
    for item in jsonl_generator(filename):
        match item['property_id']:

            case "P31":    # change this one to get other relation. P31 means "instance of"
                P31.append(item)




        
    return P31,P279


def main():
    args = get_arg_parser().parse_args()
    print(args)
    table_files = get_batch_files("entity_rels2")
    pool = Pool(processes=16)

    instance_of = []
    subclass_of = []
    for output in tqdm(
            pool.imap_unordered(
                partial(filtering_func, "P31",args.entity), table_files, chunksize=1),
            total=len(table_files)
    ):       
        if len(output[0]) != 0:
            instance_of.append(output[0])
        if len(output[1]) != 0:
            subclass_of.append(output[1])

    print(f"Extracted isntance_of {len(instance_of)} rows:")
    with open("P31_rels.txt","w",endoding="utf-8") as f:
        f.write('id,wiki_title,property_id,value\n')
        for list in instance_of:
            for item in list:
                if ',' in item['wiki_title']:
                    item['wiki_title'] = f'"{item['wiki_title']}"'
                if ',' in item['value']:
                    item['value'] = f'"{item['value']}"'  
                f.write(f"{item['qid']},{item['wiki_title']},{item['property_id']},{item['value']}\n")
    
    
    
    


if __name__ == "__main__":
    main()