var url='http://127.0.0.1:5000//api/v1.0/database'

//Creating dropdown menu

disease_dict = { 'Cardiovascular Diseases': 'Cardiovascular_diseases', 
                 'Cancer': 'Neoplasms', 
                 'Respiratory Infections and Tuberculosis': 'Respiratory_infections_and_tuberculosis', 
                 'Diabetes and Kidney Diseases': 'Diabetes_and_kidney_diseases', 
                 'Digestive Diseases': 'Digestive_diseases', 
                 'Nutritional Deficiencies': 'Nutritional_deficiencies', 
                 "Chronic Respiratory Disease": 'Chronic_respiratory_diseases', 
                 "Enteric Infections": 'Enteric_infections', 
                 'Mental Disorders': 'Mental_disorders', 
                 "Neurological Disorders": 'Neurological_disorders', 
                 "Sense Organ Diseases": 'Sense_organ_diseases', 
                 "Skin and Subcutaneous Diseases": 'Skin_and_subcutaneous_diseases' }

diet_dict = { 'Sugar': 'Sugar', 
               'Starchy Roots': 'Starchy_roots', 
               'Pulses': 'Pulses', 
               'Other': 'Other',
               'Oils and Fats': 'Oils_fats', 
               'Meat': 'Meat', 
               'Fruit and Vegetables': 'Fruit_vegetables', 
               'Dairy and Eggs': 'Dairy_eggs', 
               'Cereals and Grains': 'Cereals_grains', 
               'Alcohol beverages': 'Alcohol_beverages' }

d3.json(url).then(function(data) {
    //let values = Object.values(data);
    diet_data = data["diet_comp"];
    //disease_data = data["disease"];

    //console.log(data);
    //console.log(disease_data);

    const unique = Array.from(new Set(diet_data.map((item) => item.Entity)));
    ///console.log(unique);

    for (let i = 0; i < unique.length; i++) {
        //sample = data[i]
        let dropdownMenu = d3.select("#selDataset")
        let new_option = dropdownMenu.append("option").text(unique[i])
    }});
    

disease_list = [ 'Cardiovascular Diseases', 'Cancer', 'Respiratory Infections and Tuberculosis', 
'Diabetes and Kidney Diseases', 'Digestive Diseases', 'Nutritional Deficiencies', 
"Chronic Respiratory Disease", "Enteric Infections", 'Mental Disorders', 
"Neurological Disorders", "Sense Organ Diseases", "Skin and Subcutaneous Diseases" ]

for (let i = 0; i < disease_list.length; i++) {
    //sample = data[i]
    let dropdownMenu = d3.select("#disease_select")
    let new_option = dropdownMenu.append("option").text(disease_list[i])
}; 

diet_list = [ 'Sugar', 'Starchy Roots', 'Pulses', 'Other',
'Oils and Fats', 'Meat', 'Fruit and Vegetables', 
'Dairy and Eggs', 'Cereals and Grains', 'Alcohol beverages' ]

for (let i = 0; i < diet_list.length; i++) {
    //sample = data[i]
    let dropdownMenu = d3.select("#diet_select")
    let new_option = dropdownMenu.append("option").text(diet_list[i])
};

function init() {
    disease_plotter('Afghanistan')
    diet_plotter('Afghanistan')

    correlation_plotter('Afghanistan', 'Cardiovascular Diseases', 'Sugar')

    let disease_choice = d3.select("#disease_select")
    
    disease_choice.on("change", function() {
        let disease_value = d3.event.target.value;
        console.log(disease_value);
        correlation_plotter('Afghanistan', disease_value, 'Sugar')

        let diet_choice_2 = d3.select("#diet_select")
    
        diet_choice_2.on("change", function() {
            let diet_value = d3.select("#diet_select").node().value;
            console.log(disease_value);
            correlation_plotter('Afghanistan', disease_value, diet_value)
        }); 
    }); 

    let diet_choice = d3.select("#diet_select")
    
    diet_choice.on("change", function() {
        let diet_value = d3.select("#diet_select").node().value;
        //console.log(disease_value);
        correlation_plotter('Afghanistan', 'Cardiovascular Diseases', diet_value)

        let disease_choice_2 = d3.select("#disease_select")
    
        disease_choice_2.on("change", function() {
            let disease_value = d3.event.target.value;
            console.log(disease_value);
            correlation_plotter('Afghanistan', disease_value, diet_value)
        }); 
    }); 
    
}


function optionChanged(value) {
    disease_plotter(value)
    diet_plotter(value)

    correlation_plotter(value, 'Cardiovascular Diseases', 'Sugar')

    let disease_choice = d3.select("#disease_select")

    
    disease_choice.on("change", function() {
        let disease_value = d3.select("#disease_select").node().value;
        console.log(disease_value);
        correlation_plotter(value, disease_value, 'Sugar')
 
        let diet_choice_2 = d3.select("#diet_select")
    
        diet_choice_2.on("change", function() {
            let diet_value = d3.select("#diet_select").node().value;
            console.log(disease_value);
            correlation_plotter(value, disease_value, diet_value)
        }); 
    }); 

    let diet_choice = d3.select("#diet_select")
    
    diet_choice.on("change", function() {
        let diet_value = d3.select("#diet_select").node().value;
        //console.log(disease_value);
        correlation_plotter(value, 'Cardiovascular Diseases', diet_value)

        let disease_choice_2 = d3.select("#disease_select")
    
        disease_choice_2.on("change", function() {
            let disease_value = d3.select("#disease_select").node().value;
            //console.log(disease_value);
            correlation_plotter(value, disease_value, diet_value)
        }); 
    });     

  };



function disease_plotter(country_value) {
    d3.json(url).then(function(data) {

        disease_data = data["by_disease"]

        let Year_list = []
        let Skin_and_subcutaneous_diseases_list  = []
        let Enteric_infections_list = []
        let Diabetes_and_kidney_diseases_list = []
        let Cardiovascular_diseases_list = []
        let Digestive_diseases_list = []
        let Nutritional_deficiencies_list = []
        let Respiratory_infections_and_tuberculosis_list = []
        let Chronic_respiratory_disease_list = []
        let Neoplasms_list2 = []
        let Mental_disorders_list = []
        let Neurological_disorders_list = []
        let Sense_organ_diseases_list = []

        for (let i = 0; i < disease_data.length; i++) {
            sample = disease_data[i]
            if (sample.Entity == country_value) {
                Year_list.push(sample.Year)
                Skin_and_subcutaneous_diseases_list.push(sample.Skin_and_subcutaneous_diseases)
                Enteric_infections_list.push(sample.Enteric_infections)
                Diabetes_and_kidney_diseases_list.push(sample.Diabetes_and_kidney_diseases)
                Cardiovascular_diseases_list.push(sample.Cardiovascular_diseases)
                Digestive_diseases_list.push(sample.Digestive_diseases)
                Nutritional_deficiencies_list.push(sample.Nutritional_deficiencies)
                Respiratory_infections_and_tuberculosis_list.push(sample.Respiratory_infections_and_tuberculosis)
                Chronic_respiratory_disease_list.push(sample.Chronic_respiratory_disease)
                Neoplasms_list2.push(sample.Neoplasms)
                Neurological_disorders_list.push(sample.Neurological_disorders)
                Mental_disorders_list.push(sample.Mental_disorders)
                Sense_organ_diseases_list.push(sample.Sense_organ_diseases)
            }
        }
    
        var traces = [
            {x: Year_list, y: Cardiovascular_diseases_list, stackgroup: 'one', name: 'Cardiovascular Diseases'},
            {x: Year_list, y: Neoplasms_list2, stackgroup: 'one', name: 'Cancer'},
            {x: Year_list, y: Respiratory_infections_and_tuberculosis_list, stackgroup: 'one', name: 'Respiratory Infections and Tuberculosis'},
            {x: Year_list, y: Diabetes_and_kidney_diseases_list, stackgroup: 'one', name:'Diabetes and Kidney Diseases'},
            {x: Year_list, y: Digestive_diseases_list, stackgroup: 'one', name: 'Digestive Diseases'},
            {x: Year_list, y: Nutritional_deficiencies_list, stackgroup: 'one', name: 'Nutritional Deficiencies'},
            {x: Year_list, y: Chronic_respiratory_disease_list, stackgroup: 'one', name: "Chronic Respiratory Disease"},
            {x: Year_list, y: Enteric_infections_list, stackgroup: 'one', name: "Enteric Infections"},
            {x: Year_list, y: Mental_disorders_list, stackgroup: 'one', name: 'Mental Disorders'},
            {x: Year_list, y: Neurological_disorders_list, stackgroup: 'one', name: "Neurological Disorders"},
            {x: Year_list, y: Sense_organ_diseases_list, stackgroup: 'one', name: "Sense Organ Diseases"},
            {x: Year_list, y: Skin_and_subcutaneous_diseases_list, stackgroup: 'one', name: "Skin and Subcutaneous Diseases"},
    
        ];

        var layout = {
           yaxis: {title: {text: 'Percent'}}

        }
        
        Plotly.newPlot('area_bar_disease', traces,layout, {title: 'Burden of Disease by Cause'});


    })

}; 

function diet_plotter(country_value) {
    d3.json(url).then(function(data) {
        let diet_data=data['diet_comp']
        let Year_list = []
        let Alcohol_beverages_list = []
        let Cereals_grains_list = []
        let Dairy_eggs_list = []
        let Fruit_vegetables_list = []
        let Meat_list = []
        let Oils_fats_list = []
        let Other_list = []
        let Pulses_list = []
        let Starchy_roots_list = []
        let Sugar_list = []

        for (let i = 0; i < diet_data.length; i++) {
            if (diet_data[i].Entity == country_value) {
                Year_list.push(diet_data[i].Year)
                Alcohol_beverages_list.push(diet_data[i].Alcohol_beverages)
                Cereals_grains_list.push(diet_data[i].Cereals_grains)
                Dairy_eggs_list.push(diet_data[i].Dairy_eggs)
                Fruit_vegetables_list.push(diet_data[i].Fruit_vegetables)
                Meat_list.push(diet_data[i].Meat)
                Oils_fats_list.push(diet_data[i].Oils_fats)
                Other_list.push(diet_data[i].Other)
                Pulses_list.push(diet_data[i].Pulses)
                Starchy_roots_list.push(diet_data[i].Starchy_roots)
                Sugar_list.push(diet_data[i].Sugar)
            }
        }
        //console.log(Year_list)
        //console.log(Sugar_list)

        var traces = [
            {x: Year_list, y: Alcohol_beverages_list, stackgroup: 'one', name: 'Alcohol beverages'},
            {x: Year_list, y: Cereals_grains_list, stackgroup: 'one', name: 'Cereals and Grains'},
            {x: Year_list, y: Dairy_eggs_list, stackgroup: 'one', name: 'Dairy and Eggs'},
            {x: Year_list, y: Fruit_vegetables_list, stackgroup: 'one', name:'Fruit and Vegetables'},
            {x: Year_list, y: Meat_list, stackgroup: 'one', name: 'Meat'},
            {x: Year_list, y: Oils_fats_list, stackgroup: 'one', name: 'Oils and Fats'},
            {x: Year_list, y: Other_list, stackgroup: 'one', name: "Other"},
            {x: Year_list, y: Pulses_list, stackgroup: 'one', name: "Pulses"},
            {x: Year_list, y: Starchy_roots_list, stackgroup: 'one', name: 'Starchy Roots'},
            {x: Year_list, y: Sugar_list, stackgroup: 'one', name: "Sugar"},
    
        ];

        var layout = {
           yaxis: {title: {text: 'kcal per day'}}

        }
        
        Plotly.newPlot('area_bar_diet', traces,layout, {title: 'Diet Composition by Food Groups'});


    })

}; 

function correlation_plotter(country_value, disease_value, diet_value) {
    d3.json(url).then(function(data) {
        let diet_disease=data['joined_disease_diet']

        let disease_values_list = []
        let diet_values_list = []

        for (let i = 0; i < diet_disease.length; i++) {
            if (diet_disease[i].Entity == country_value) {

                disease_values_list.push(diet_disease[i][ disease_dict[disease_value] ])
                //disease_values_list.push( diet_disease[i].Cardiovascular_diseases )
                diet_values_list.push(diet_disease[i][ diet_dict[diet_value] ])
                //console.log(disease_dict[disease_value])
                //console.log(diet_disease[i].Entity)
            }

        }
        var trace_scatter = {
            x: diet_values_list,
            y: disease_values_list,
            mode: 'markers',
            type: 'scatter'
          };
        
        Plotly.newPlot('diet_disease_correlation', [trace_scatter])
        //console.log(disease_values_list)
        //console.log(diet_values_list)
        //console.log(diet_disease)
    })
}; 

init()