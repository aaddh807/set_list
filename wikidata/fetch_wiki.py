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


def filtering_func(rel, entity, filename):
    filtered = []
    for item in jsonl_generator(filename):
        
        filtered.append(item)
    return filtered


def main():
    args = get_arg_parser().parse_args()
    print(args)
    table_files = get_batch_files("wikipedia_links")
    pool = Pool()
    filtered = []
    
    for output in tqdm(
            pool.imap_unordered(
                partial(filtering_func, "P580", args.entity), table_files, chunksize=1),
            total=len(table_files)
    ):
            
        filtered.extend(output)
    print(f"Extracted {len(filtered)} rows:")
    with open("wiki.txt","w",encoding = "utf-8") as f:
        for i,item in enumerate(tqdm(filtered)):
            f.write(f"{item['qid']}|{item['wiki_title']}\n")


if __name__ == "__main__":
    main()