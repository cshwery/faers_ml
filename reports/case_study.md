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

    Patient reaction, as a MedDRA term. Note: MedDRA has a hierarchical organization, and I'd leverage that taxonomy here, but it is a paid/subscription service so I'm unable to for this case study.
    
    * This returns counts of specific patient reaction
* patient.reaction.reactionoutcome

    * Outcome of the reaction in reactionmeddrapt at the time of last observation.

    * Value is one of the following
1 = Recovered/resolved
2 = Recovering/resolving
3 = Not recovered/not resolved
4 = Recovered/resolved with sequelae (consequent health issues)
5 = Fatal
6 = Unknown

* patient.patientagegroup

    * '1': 'Recovered/resolved',
  '2': 'Recovering/resolving',
  '3': 'Not recovered/not resolved',
  '4': 'Recovered/resolved with sequelae (consequent health issues)',
  '5': 'Fatal'

### Data Collection
In order to explore and manipulate some data, I created a class to enable easy interaction with the API for my purposes. This is available [here](. In particular I made a recursive method that would make a