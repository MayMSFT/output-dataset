from utils import FileReader, get_breaks
from azureml.core import Dataset, Run
import pandas as pd
import argparse

def init():
    global meta_df
    run = Run.get_context()
    # get the input dataset by name
    workspace = run.experiment.workspace
    covid_meta = Dataset.get_by_name(workspace, 'covid-19 metadata').download()[0]
    # load the TabularDataset to pandas DataFrame
    meta_df = pd.read_csv(covid_meta, dtype={'pubmed_id': str, 'Microsoft Academic Paper ID': str, 'doi': str})

    



def run(mini_batch):
    print(f'dataprep start: {__file__}, run({mini_batch})')
    dict_ = {'paper_id': [], 'doi':[], 'abstract': [], 'body_text': [], 'authors': [], 'title': [], 'journal': [], 'abstract_summary': []}
    for entry in mini_batch:
        try:
            content = FileReader(entry)
        except Exception as e:
            continue  # invalid paper format, skip
        
        # get metadata information
        meta_data = meta_df.loc[meta_df['sha'] == content.paper_id]
        print('found meta_data', meta_data)
        # no metadata, skip this paper
        if len(meta_data) == 0:
            continue
        
        dict_['abstract'].append(content.abstract)
        dict_['paper_id'].append(content.paper_id)
        dict_['body_text'].append(content.body_text)
        
        # also create a column for the summary of abstract to be used in a plot
        if len(content.abstract) == 0: 
            # no abstract provided
            dict_['abstract_summary'].append("Not provided.")
        elif len(content.abstract.split(' ')) > 100:
            # abstract provided is too long for plot, take first 100 words append with ...
            info = content.abstract.split(' ')[:100]
            summary = get_breaks(' '.join(info), 40)
            dict_['abstract_summary'].append(summary + "...")
        else:
            # abstract is short enough
            summary = get_breaks(content.abstract, 40)
            dict_['abstract_summary'].append(summary)
            
        # get metadata information
        meta_data = meta_df.loc[meta_df['sha'] == content.paper_id]
        
        try:
            # if more than one author
            authors = meta_data['authors'].values[0].split(';')
            if len(authors) > 2:
                # if more than 2 authors, take them all with html tag breaks in between
                dict_['authors'].append(get_breaks('. '.join(authors), 40))
            else:
                # authors will fit in plot
                dict_['authors'].append(". ".join(authors))
        except Exception as e:
            # if only one author - or Null valie
            dict_['authors'].append(meta_data['authors'].values[0])
        
        # add the title information, add breaks when needed
        try:
            title = get_breaks(meta_data['title'].values[0], 40)
            dict_['title'].append(title)
        # if title was not provided
        except Exception as e:
            dict_['title'].append(meta_data['title'].values[0])
        
        # add the journal information
        dict_['journal'].append(meta_data['journal'].values[0])
        
        # add doi
        dict_['doi'].append(meta_data['doi'].values[0])
    
    df_covid = pd.DataFrame(dict_, columns=['paper_id', 'doi', 'abstract', 'body_text', 'authors', 'title', 'journal', 'abstract_summary'])
    print('processed: ', df_covid)

    return df_covid
