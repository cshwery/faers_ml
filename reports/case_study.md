# FAERS Case Study

FAERS is an FDA database and API of adverse events associated with medicinal products (a broad term, which can include more than pharmaceuticals, but I'll use the term 'drug' here liberally). This case study examines patient reactions and interactions around a group of drugs, namely the 2019 top 10 best selling drugs by AstraZeneca (as found in [this article](https://www.biopharmadive.com/news/astrazeneca-pharma-dive-awards/566229/#:~:text=Lung%20cancer%20drug%20Tagrisso%20has,overtaking%20Symbicort%20earlier%20this%20year.)). 
### Drugs of interest in this case study:
* SYMBICORT
* TAGRISSO
* NEXIUM
* CRESTOR
* FARXIGA
* BRILINTA
* PULMICORT
* FASLODEX
* ZOLADEX
* SELOKEN
* TOPROL-XL

### Fields leveraged for this case study
In order to gather some useful data for exploration, I'll leverage the following [Fields](https://open.fda.gov/apis/drug/event/searchable-fields/)
 in the FAERS API:

* patient.patientsex
    * '1': 'Male', '2': 'Female'
* patient.drug.medicinalproduct
    * This field contains the name of the drugs reported by the patient.
        
* patient.reaction.reactionmeddrapt

    * Patient reaction, as a MedDRA term. Note: MedDRA has a hierarchical organization, and I'd leverage that taxonomy here, but it is a paid/subscription service so I'm unable to for this case study.
    
    * This returns counts of specific patient reaction
* serious

    * Seriousness of the adverse event.
    * Value is one of the following
1 = The adverse event resulted in death, a life threatening condition, hospitalization, disability, congenital anomaly, or other serious condition
2 = The adverse event did not result in any of the above

* patient.patientagegroup

    * '1': 'Recovered/resolved',
  '2': 'Recovering/resolving',
  '3': 'Not recovered/not resolved',
  '4': 'Recovered/resolved with sequelae (consequent health issues)',
  '5': 'Fatal'

### Data Exploration
In order to quickly acquire data to explore and manipulate, I created a class to enable easy interaction with the API for my purposes. This is available [here](https://github.com/cshwery/faers_ml/blob/master/src/data/helpers.py). This allows me to quickly create a dataset for exploratory visualization, which I did with the following design:
* Iterate through the drugs listed above (initial_drug)
    * For each drug, identify the 10 drugs which co-occur with the initial drug most frequently in the database ('interaction_drug').
        * For each (initial_drug,interaction_drug) pair get the top 10 most frequent reactions.
        * For each (initial_drug,interaction_drug,reaction) combination, partition it by whether or not it was serious
* Visualize the results in a heat map. In particular, visualize the the % of an outcome involving that interaction pair. This is done by dividing the count of times the drug was co-incident with another drug by how many times the initial_drug was associated with a specific reaction.

To gather the data the following code was leveraged [here]()

Additionally, I made a recursive method (.return_categorical_counts) that takes as input a set of parameters and a set of categories and the values they take, and recursively makes api calls for all combination of category states (while also leveraging the input parameters). However, this was not done at this step.    

