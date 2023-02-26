import numpy as np

import sqlalchemy
from sqlalchemy import join
from sqlalchemy.sql import select
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_cors import CORS

engine = create_engine("sqlite:///diet_disease.sqlite", echo=False)

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(autoload_with=engine)
#Base.classes.keys()

dietary_composition = Base.classes.dietary_composition
disease_burden = Base.classes.disease_burden_by_diseases


#app = Flask(__name__)

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/dietary_composition<br/>"
        f"/api/v1.0/disease_burden"
    )


@app.route("/api/v1.0/diet_disease")
def diet_disease_func():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results_1 = session.query(
        dietary_composition.Entity,
        dietary_composition.Code,
        dietary_composition.Year, 
        dietary_composition.Other, 
        dietary_composition.Alcohol_beverages, 
        dietary_composition.Sugar, 
        dietary_composition.Oils_fats,
        dietary_composition.Meat,
        dietary_composition.Dairy_eggs,
        dietary_composition.Fruit_vegetables,
        dietary_composition.Starchy_roots,
        dietary_composition.Pulses,
        dietary_composition.Cereals_grains).all()

    #session.close()

    results_2 = session.query(
        disease_burden.Entity,
        disease_burden.Code,
        disease_burden.Year, 
        disease_burden.Skin_and_subcutaneous_diseases, 
        disease_burden.Enteric_infections, 
        disease_burden.Diabetes_and_kidney_diseases, 
        disease_burden.Cardiovascular_diseases,
        disease_burden.Digestive_diseases,
        disease_burden.Nutritional_deficiencies,
        disease_burden.Respiratory_infections_and_tuberculosis,
        disease_burden.Chronic_respiratory_diseases,
        disease_burden.Neoplasms,
        disease_burden.Mental_disorders,
        disease_burden.Neurological_disorders,
        disease_burden.Sense_organ_diseases).all()

    conn = engine.connect()
    results_3 = conn.execute("select disease_burden_by_diseases.Entity, disease_burden_by_diseases.Code, disease_burden_by_diseases.Year, dietary_composition.Other, dietary_composition.Alcohol_beverages, dietary_composition.Sugar, dietary_composition.Oils_fats, dietary_composition.Meat, dietary_composition.Dairy_eggs, dietary_composition.Fruit_vegetables, dietary_composition.Starchy_roots, dietary_composition.Pulses, dietary_composition.Cereals_grains, disease_burden_by_diseases.Skin_and_subcutaneous_diseases, disease_burden_by_diseases.Enteric_infections, disease_burden_by_diseases.Diabetes_and_kidney_diseases, disease_burden_by_diseases.Cardiovascular_diseases, disease_burden_by_diseases.Digestive_diseases, disease_burden_by_diseases.Nutritional_deficiencies, disease_burden_by_diseases.Respiratory_infections_and_tuberculosis, disease_burden_by_diseases.Chronic_respiratory_diseases, disease_burden_by_diseases.Neoplasms, disease_burden_by_diseases.Mental_disorders, disease_burden_by_diseases.Neurological_disorders, disease_burden_by_diseases.Sense_organ_diseases from dietary_composition inner join disease_burden_by_diseases ON dietary_composition.Entity = disease_burden_by_diseases.Entity AND dietary_composition.Year = disease_burden_by_diseases.Year" ).all()
    #results_3 = session.query(  ).join( disease_burden, (dietary_composition.Entity==disease_burden.Entity) & (dietary_composition.Year==disease_burden.Year) ).all()

  
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_dietary_composition = []
    for Entity, Code, Year, Other, Alcohol_beverages, Sugar, Oils_fats, Meat, Dairy_eggs, Fruit_vegetables, Starchy_roots, Pulses, Cereals_grains  in results_1:
        dietary_composition_dict = {}
        dietary_composition_dict["Entity"] = Entity
        dietary_composition_dict["Code"] = Code
        dietary_composition_dict["Year"] = Year
        dietary_composition_dict["Other"] = Other
        dietary_composition_dict["Alcohol_beverages"] = Alcohol_beverages
        dietary_composition_dict["Sugar"] = Sugar
        dietary_composition_dict["Oils_fats"] = Oils_fats
        dietary_composition_dict["Meat"] = Meat
        dietary_composition_dict["Dairy_eggs"] = Dairy_eggs
        dietary_composition_dict["Fruit_vegetables"] = Fruit_vegetables
        dietary_composition_dict["Starchy_roots"] = Starchy_roots
        dietary_composition_dict["Pulses"] = Pulses
        dietary_composition_dict["Cereals_grains"] = Cereals_grains

        all_dietary_composition.append(dietary_composition_dict)

    #jsonfied_diet=jsonify(all_dietary_composition)

    # Create a dictionary from the row data and append to a list of all_passengers
    all_disease_burden = []
    for Entity, Code, Year, Skin_and_subcutaneous_diseases, Enteric_infections,Diabetes_and_kidney_diseases,Cardiovascular_diseases,Digestive_diseases, Nutritional_deficiencies,Respiratory_infections_and_tuberculosis, Chronic_respiratory_diseases, Mental_disorders,Neoplasms, Neurological_disorders, Sense_organ_diseases in results_2:
        disease_burden_dict = {}
        disease_burden_dict["Entity"] = Entity
        disease_burden_dict["Code"] = Code
        disease_burden_dict["Year"] = Year
        disease_burden_dict["Skin_and_subcutaneous_diseases"] = Skin_and_subcutaneous_diseases
        disease_burden_dict["Enteric_infections"] = Enteric_infections
        disease_burden_dict["Diabetes_and_kidney_diseases"] = Diabetes_and_kidney_diseases
        disease_burden_dict["Cardiovascular_diseases"] = Cardiovascular_diseases
        disease_burden_dict["Digestive_diseases"] = Digestive_diseases
        disease_burden_dict["Nutritional_deficiencies"] = Nutritional_deficiencies
        disease_burden_dict["Respiratory_infections_and_tuberculosis"] = Respiratory_infections_and_tuberculosis
        disease_burden_dict["Chronic_respiratory_diseases"] = Chronic_respiratory_diseases
        disease_burden_dict["Neoplasms"] = Neoplasms
        disease_burden_dict["Mental_disorders"] = Mental_disorders
        disease_burden_dict["Neurological_disorders"] = Neurological_disorders
        disease_burden_dict["Sense_organ_diseases"] = Sense_organ_diseases
        all_disease_burden.append(disease_burden_dict)

    #joined=session.query(dietary_composition).join(disease_burden, dietary_composition.Entity ==disease_burden.Entity )
    
    diet_disease_joined = []
    for Entity, Code, Year, Other, Alcohol_beverages, Sugar, Oils_fats, Meat, Dairy_eggs, Fruit_vegetables, Starchy_roots, Pulses, Cereals_grains, Skin_and_subcutaneous_diseases, Enteric_infections,Diabetes_and_kidney_diseases,Cardiovascular_diseases,Digestive_diseases, Nutritional_deficiencies,Respiratory_infections_and_tuberculosis, Chronic_respiratory_diseases, Mental_disorders,Neoplasms, Neurological_disorders, Sense_organ_diseases in results_3:
        diet_disease_joined_dict = {}
        diet_disease_joined_dict["Entity"] = Entity
        diet_disease_joined_dict["Code"] = Code
        diet_disease_joined_dict["Year"] = Year

        diet_disease_joined_dict["Other"] = Other
        diet_disease_joined_dict["Alcohol_beverages"] = Alcohol_beverages
        diet_disease_joined_dict["Sugar"] = Sugar
        diet_disease_joined_dict["Oils_fats"] = Oils_fats
        diet_disease_joined_dict["Meat"] = Meat
        diet_disease_joined_dict["Dairy_eggs"] = Dairy_eggs
        diet_disease_joined_dict["Fruit_vegetables"] = Fruit_vegetables
        diet_disease_joined_dict["Starchy_roots"] = Starchy_roots
        diet_disease_joined_dict["Pulses"] = Pulses
        diet_disease_joined_dict["Cereals_grains"] = Cereals_grains

        diet_disease_joined_dict["Skin_and_subcutaneous_diseases"] = Skin_and_subcutaneous_diseases
        diet_disease_joined_dict["Enteric_infections"] = Enteric_infections
        diet_disease_joined_dict["Diabetes_and_kidney_diseases"] = Diabetes_and_kidney_diseases
        diet_disease_joined_dict["Cardiovascular_diseases"] = Cardiovascular_diseases
        diet_disease_joined_dict["Digestive_diseases"] = Digestive_diseases
        diet_disease_joined_dict["Nutritional_deficiencies"] = Nutritional_deficiencies
        diet_disease_joined_dict["Respiratory_infections_and_tuberculosis"] = Respiratory_infections_and_tuberculosis
        diet_disease_joined_dict["Chronic_respiratory_diseases"] = Chronic_respiratory_diseases
        diet_disease_joined_dict["Neoplasms"] = Neoplasms
        diet_disease_joined_dict["Mental_disorders"] = Mental_disorders
        diet_disease_joined_dict["Neurological_disorders"] = Neurological_disorders
        diet_disease_joined_dict["Sense_organ_diseases"] = Sense_organ_diseases

        diet_disease_joined.append(diet_disease_joined_dict)

   
    final_list = { 'diet_disease_join': diet_disease_joined, 'diet': all_dietary_composition, 'disease':all_disease_burden }
    return jsonify(final_list)
    
     
   
if __name__ == '__main__':
    app.run(debug=True)