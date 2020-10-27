faers_endpoint = "https://api.fda.gov/drug/event.json?"
faers_translations = {"patient.patientagegroup": {"1": "Neonate",
                                                  "2": "Infant",
                                                  "3": "Child",
                                                  "4": "Adolescent",
                                                  "5": "Adult",
                                                  "6": "Elderly", },
                      "patient.patientsex": {#"0": "Unknown",
                                             "1": "Male",
                                             "2": "Female", },
                      # "patient.reaction.reactionoutcome": {"1": "Recovered/resolved",
                      #                                      "2": "Recovering/resolving",
                      #                                      "3": "Not recovered/not resolved",
                      #                                      "4": "Recovered/resolved with sequelae (consequent health issues)",
                      #                                      "5": "Fatal",
                      #                                      #"6": "Unknown",
                      #                                      }
                      "serious": {"1":"Serious Adverse Event",
                                  "2":"Non-Serious"}
                      }
