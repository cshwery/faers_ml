import requests
import json
from typing import List, Dict
from copy import copy
from dotenv import load_dotenv
from src.data import faers_translations, faers_endpoint
import pandas as pd
import os

load_dotenv()


class FaersApi():
    def __init__(self):
        # This makes the code less generalizable, but since we're doing this for just one api it's fine
        self.faers_ep = faers_endpoint + 'api_key=' + os.environ['fda_api_key'] + '&'
        self.faers_translations = faers_translations
    def construct_url(self
                      , query_params: Dict
                      , ) -> str:
        """This method does the url encoding for the faers events api get requests
        which gave me a few issues when using requests library and this seemed easy enough to do"""
        url_const = self.faers_ep
        initialized = False
        for param_q, param_val in query_params.items():
            # Need to add '&' to 2nd,3rd,... query_params
            if initialized:
                url_const += '&'
            else:
                initialized = True
            if type(param_val) == str and len(query_params) > 0 \
                    or type(param_val) == int:
                url_const += f'{param_q}={param_val}'
            elif type(param_val) == dict and len(param_val) > 0:
                url_const += f'{param_q}=' + "+AND+".join(
                    [f'{sub_p_k}:{sub_p_v}' for sub_p_k, sub_p_v in param_val.items()])
            elif type(param_val) == list and len(param_val) > 0:
                url_const += f'{param_q}=' + "+AND+".join(param_val)
            else:
                raise TypeError
        return url_const

    def make_call(self
                  , query_params: Dict
                  , ) -> Dict:
        """Simply makes the api call for a given set of query parameters"""
        return requests.get(self.construct_url(query_params))

    def return_categorical_counts(self
                                             , query_params: Dict
                                             , categories: Dict = {}
                                             , labels: Dict = {}
                                             , count_by: str = "occurcountry"
                                             , record_list: List = []
                                             , ) -> List[Dict]:
        """Takes a search criteria and a dict of dict of categories,
        recursively puts every combination of categories into the search parameters.
        Finally, it makes queries along all categories requested.
        Returns output as a list of dictionaries
        """
        # Make sure record list is list
        if not record_list:
            record_list = []
        # Make the api call if recursion is complete
        if len(categories) == 0:
            # Nuke any existing count variable, just on basis of last item
            query_params['count'] = count_by
            #print(query_params)
            resp = self.make_call(query_params)
            # modified to account for responses with no results
            records = resp.json().get('results')
            if records and len(records)>0:
                for rec in records:
                    rec.update(labels)
                    record_list.append(rec)
            return record_list
        else:
            for key, val in categories.items():
                categories_recur = copy(categories)
                del categories_recur[key]
                for sub_key,sub_val in val.items():
                    #print(key,sub_key,sub_val)
                    # Add the key/val pair to the search criteria
                    query_params_recur = copy(query_params)
                    if type(query_params_recur.get('search'))==dict:
                        query_params_recur['search'][key] = sub_key
                    elif type(query_params_recur.get('search'))==list:
                        query_params_recur['search'].append(f'{key}={sub_key}')
                    elif type(query_params_recur.get('search'))==str:
                        query_params_recur['search'] = [query_params['search']]
                        query_params_recur['search'].append(f'{key}={sub_key}')
                    elif not query_params_recur.get('search'):
                        query_params_recur['search'] = {key:sub_key}
                    labels.update({key:sub_val})
                    #print(query_params_recur)
                    #print(categories_recur)
                    record_list = self.return_categorical_counts(query_params=query_params_recur
                                              , categories=categories_recur
                                              , count_by=count_by
                                              , labels=labels
                                              , record_list = record_list)
                #Because additional categories are already processed, we return here
                return record_list







if __name__ == "__main__":
    faersApi = FaersApi()
    print(1 + 1)
