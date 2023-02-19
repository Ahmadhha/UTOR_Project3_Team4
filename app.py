import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///diet_disease_db.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table

cal_info = Base.classes.calorie_info
diet_comp = Base.classes.dietary_composition
daly = Base.classes.Disability_adjusted_life_years
by_cause = Base.classes.Total_disease_burden_by_cause
by_disease = Base.classes.disease_burden_by_diseases


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"Static APIs:<br/>"
        f"/api/v1.0/database_json<br/>"
        f"/api/v1.0/database<br/>"
        f"/api/v1.0/sample_data_10_rows<br/>"
    )


@app.route("/api/v1.0/database_json")
def database_json():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Retrieve the Test Database"""

    # Perform a query to retrieve all data
    Table1 = session.query(cal_info).all()
    Table2 = session.query(diet_comp).all()
    Table3 = session.query(daly).all()
    Table4 = session.query(by_cause).all()
    Table5 = session.query(by_disease).all()

    session.close() 

    database_dict = {"calorie_info" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Animal_protein" : row.Animal_protein, "Plant_protein" : row.Plant_protein,
                                     "Fat" : row.Fat, "Carbohydrate" : row.Carbohydrate
                                        } for row in Table1],
                    "diet_comp" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Other" : row.Other, "Alcohol_beverages" : row.Alcohol_beverages,
                                     "Sugar" : row.Sugar, "Oils_fats" : row.Oils_fats,
                                     "Meat" : row.Meat, "Dairy_eggs" : row.Dairy_eggs,
                                     "Fruit_vegetables" : row.Fruit_vegetables, "Starchy_roots" : row.Starchy_roots,
                                     "Pulses" : row.Pulses, "Cereals_grains" : row.Cereals_grains
                                    } for row in Table2],
                    "daly" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Disability_adjusted_life_years" : row.Disability_adjusted_life_years
                                    } for row in Table3],
                    "by_cause" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Injuries" : row.Injuries, "Communicable_maternal_neonatal_nutritional_diseases" : row.Communicable_maternal_neonatal_nutritional_diseases,
                                     "Non_communicable_diseases" : row.Non_communicable_diseases
                                    } for row in Table4],
                    "by_disease" : [{"Entity" : row.Entity,"Code" : row.Code,"Year" : row.Year,
                                    "Self_harm" : row.Self_harm,"Exposure_to_forces_of_nature" : row.Exposure_to_forces_of_nature,
                                    "Conflict_terrorism" : row.Conflict_terrorism,"Interpersonal_violence" : row.Interpersonal_violence,
                                    "Neglected_tropical_diseases_and_malaria" : row.Neglected_tropical_diseases_and_malaria,
                                    "Substance_use_disorder" : row.Substance_use_disorder,"Skin_and_subcutaneous_diseases" : row.Skin_and_subcutaneous_diseases,
                                    "Enteric_infections" : row.Enteric_infections,"Diabetes_and_kidney_diseases" : row.Diabetes_and_kidney_diseases,
                                    "Cardiovascular_diseases" : row.Cardiovascular_diseases,"Digestive_diseases" : row.Digestive_diseases,
                                    "Nutritional_deficiencies" : row.Nutritional_deficiencies,"Respiratory_infections_and_tuberculosis" : row.Respiratory_infections_and_tuberculosis,
                                    "Neonatal_disorders" : row.Neonatal_disorders,"Chronic_respiratory_diseases" : row.Chronic_respiratory_diseases,
                                    "Other_non_communicable_diseases" : row.Other_non_communicable_diseases,"Maternal_disorders" : row.Maternal_disorders,
                                    "Unintentional_injuries" : row.Unintentional_injuries,"Musculoskeletal_disorders" : row.Musculoskeletal_disorders,
                                    "Neoplasms" : row.Neoplasms,"Mental_disorders" : row.Mental_disorders,"Neurological_disorders" : row.Neurological_disorders,
                                    "HIV_AIDS_and_sexually_transmitted_infections" : row.HIV_AIDS_and_sexually_transmitted_infections,
                                    "Transport_injuries" : row.Transport_injuries,"Sense_organ_diseases" : row.Sense_organ_diseases
                                    } for row in Table5],                                                                    
                    }

    return jsonify(database_dict)

@app.route("/api/v1.0/database")
def database():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Retrieve the Test Database"""

    # Perform a query to retrieve all data
    Table1 = session.query(cal_info).all()
    Table2 = session.query(diet_comp).all()
    Table3 = session.query(daly).all()
    Table4 = session.query(by_cause).all()
    Table5 = session.query(by_disease).all()

    session.close() 

    database_dict = {"calorie_info" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Animal_protein" : row.Animal_protein, "Plant_protein" : row.Plant_protein,
                                     "Fat" : row.Fat, "Carbohydrate" : row.Carbohydrate
                                        } for row in Table1],
                    "diet_comp" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Other" : row.Other, "Alcohol_beverages" : row.Alcohol_beverages,
                                     "Sugar" : row.Sugar, "Oils_fats" : row.Oils_fats,
                                     "Meat" : row.Meat, "Dairy_eggs" : row.Dairy_eggs,
                                     "Fruit_vegetables" : row.Fruit_vegetables, "Starchy_roots" : row.Starchy_roots,
                                     "Pulses" : row.Pulses, "Cereals_grains" : row.Cereals_grains
                                    } for row in Table2],
                    "daly" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Disability_adjusted_life_years" : row.Disability_adjusted_life_years
                                    } for row in Table3],
                    "by_cause" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Injuries" : row.Injuries, "Communicable_maternal_neonatal_nutritional_diseases" : row.Communicable_maternal_neonatal_nutritional_diseases,
                                     "Non_communicable_diseases" : row.Non_communicable_diseases
                                    } for row in Table4],
                    "by_disease" : [{"Entity" : row.Entity,"Code" : row.Code,"Year" : row.Year,
                                    "Self_harm" : row.Self_harm,"Exposure_to_forces_of_nature" : row.Exposure_to_forces_of_nature,
                                    "Conflict_terrorism" : row.Conflict_terrorism,"Interpersonal_violence" : row.Interpersonal_violence,
                                    "Neglected_tropical_diseases_and_malaria" : row.Neglected_tropical_diseases_and_malaria,
                                    "Substance_use_disorder" : row.Substance_use_disorder,"Skin_and_subcutaneous_diseases" : row.Skin_and_subcutaneous_diseases,
                                    "Enteric_infections" : row.Enteric_infections,"Diabetes_and_kidney_diseases" : row.Diabetes_and_kidney_diseases,
                                    "Cardiovascular_diseases" : row.Cardiovascular_diseases,"Digestive_diseases" : row.Digestive_diseases,
                                    "Nutritional_deficiencies" : row.Nutritional_deficiencies,"Respiratory_infections_and_tuberculosis" : row.Respiratory_infections_and_tuberculosis,
                                    "Neonatal_disorders" : row.Neonatal_disorders,"Chronic_respiratory_diseases" : row.Chronic_respiratory_diseases,
                                    "Other_non_communicable_diseases" : row.Other_non_communicable_diseases,"Maternal_disorders" : row.Maternal_disorders,
                                    "Unintentional_injuries" : row.Unintentional_injuries,"Musculoskeletal_disorders" : row.Musculoskeletal_disorders,
                                    "Neoplasms" : row.Neoplasms,"Mental_disorders" : row.Mental_disorders,"Neurological_disorders" : row.Neurological_disorders,
                                    "HIV_AIDS_and_sexually_transmitted_infections" : row.HIV_AIDS_and_sexually_transmitted_infections,
                                    "Transport_injuries" : row.Transport_injuries,"Sense_organ_diseases" : row.Sense_organ_diseases
                                    } for row in Table5],                                                                    
                    }

    return (database_dict)


@app.route("/api/v1.0/sample_data_10_rows")
def sample_data_10_rows():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Retrieve the Test Database"""

    # Perform a query to retrieve all data
    Table1 = session.query(cal_info).all()
    Table2 = session.query(diet_comp).all()
    Table3 = session.query(daly).all()
    Table4 = session.query(by_cause).all()
    Table5 = session.query(by_disease).all()

    session.close() 

    n=10

    database_dict = {"calorie_info" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Animal_protein" : row.Animal_protein, "Plant_protein" : row.Plant_protein,
                                     "Fat" : row.Fat, "Carbohydrate" : row.Carbohydrate
                                        } for row in Table1[0:n]],
                    "diet_comp" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Other" : row.Other, "Alcohol_beverages" : row.Alcohol_beverages,
                                     "Sugar" : row.Sugar, "Oils_fats" : row.Oils_fats,
                                     "Meat" : row.Meat, "Dairy_eggs" : row.Dairy_eggs,
                                     "Fruit_vegetables" : row.Fruit_vegetables, "Starchy_roots" : row.Starchy_roots,
                                     "Pulses" : row.Pulses, "Cereals_grains" : row.Cereals_grains
                                    } for row in Table2[0:n]],
                    "daly" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Disability_adjusted_life_years" : row.Disability_adjusted_life_years
                                    } for row in Table3[0:n]],
                    "by_cause" : [{"Entity" : row.Entity, "Code" : row.Code, "Year" : row.Year,
                                     "Injuries" : row.Injuries, "Communicable_maternal_neonatal_nutritional_diseases" : row.Communicable_maternal_neonatal_nutritional_diseases,
                                     "Non_communicable_diseases" : row.Non_communicable_diseases
                                    } for row in Table4[0:n]],
                    "by_disease" : [{"Entity" : row.Entity,"Code" : row.Code,"Year" : row.Year,
                                    "Self_harm" : row.Self_harm,"Exposure_to_forces_of_nature" : row.Exposure_to_forces_of_nature,
                                    "Conflict_terrorism" : row.Conflict_terrorism,"Interpersonal_violence" : row.Interpersonal_violence,
                                    "Neglected_tropical_diseases_and_malaria" : row.Neglected_tropical_diseases_and_malaria,
                                    "Substance_use_disorder" : row.Substance_use_disorder,"Skin_and_subcutaneous_diseases" : row.Skin_and_subcutaneous_diseases,
                                    "Enteric_infections" : row.Enteric_infections,"Diabetes_and_kidney_diseases" : row.Diabetes_and_kidney_diseases,
                                    "Cardiovascular_diseases" : row.Cardiovascular_diseases,"Digestive_diseases" : row.Digestive_diseases,
                                    "Nutritional_deficiencies" : row.Nutritional_deficiencies,"Respiratory_infections_and_tuberculosis" : row.Respiratory_infections_and_tuberculosis,
                                    "Neonatal_disorders" : row.Neonatal_disorders,"Chronic_respiratory_diseases" : row.Chronic_respiratory_diseases,
                                    "Other_non_communicable_diseases" : row.Other_non_communicable_diseases,"Maternal_disorders" : row.Maternal_disorders,
                                    "Unintentional_injuries" : row.Unintentional_injuries,"Musculoskeletal_disorders" : row.Musculoskeletal_disorders,
                                    "Neoplasms" : row.Neoplasms,"Mental_disorders" : row.Mental_disorders,"Neurological_disorders" : row.Neurological_disorders,
                                    "HIV_AIDS_and_sexually_transmitted_infections" : row.HIV_AIDS_and_sexually_transmitted_infections,
                                    "Transport_injuries" : row.Transport_injuries,"Sense_organ_diseases" : row.Sense_organ_diseases
                                    } for row in Table5[0:n]],                                                                    
                    }

    return (database_dict)

if __name__ == '__main__':
    app.run(debug=True)