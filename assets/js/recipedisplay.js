var json = `{
    "recipes": [

        {
            "title": "Asian Beef with Snow Peas",
            "description": "Stir-fried beef in a light gingery sauce. Serve over steamed rice or hot egg noodles.",
            "image": [
                { "url" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQew_3DUdMee8cUpXV2T-MCKWq8zOqM1sRFnJ0gqAT1pjOW436D&usqp=CAU"},
                { "url" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQew_3DUdMee8cUpXV2T-MCKWq8zOqM1sRFnJ0gqAT1pjOW436D&usqp=CAU"}
            ],
            "ingredientdetails": [
        {
            "quantity": "3 tablespoons",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85a87"
            },
            "directions": null
        },
        {
            "quantity": "2 tablespoons",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85aea"   
            },
            "directions": null
        },
        {
            "quantity": "1 tablespoon",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85a46"
            },
            "directions": null
        },
        {
            "quantity": "1/2 teaspoon",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85abd"
            },
            "directions": null
        },
        {
            "quantity": "1 tablespoon",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85a4c"
            },
            "directions": null
        },
        {
            "quantity": "1 tablespoon",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85b29"
            },
            "directions": "minced fresh"
        },
        {
            "quantity": "1 tablespoon",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85a43"
            },
            "directions": "minced"
        },
        {
            "quantity": "1 pound",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85a84"
            },
            "directions": "round"
        },
        {
            "quantity": "8 ounces",
            "ingredient": {
                "$oid": "5e6ddc43ec8c0e2d32b85d02"
            },
            "directions": null
        }
    ],
            "timetocook": {
                "hh": 0,
                "mm": 15
        },
         "instructions": "In a small bowl, combine the soy sauce, rice wine, brown sugar and cornstarch. Set aside. Heat oil in a wok or skillet over medium high heat. Stir-fry ginger and garlic for 30 seconds. Add the steak and stir-fry for 2 minutes or until evenly browned. Add the snow peas and stir-fry for an additional 3 minutes. Add the soy sauce mixture, bring to a boil, stirring constantly. Lower heat and simmer until the sauce is thick and smooth. Serve immediately.",
         "cuisine": "Chinese",
        "dishtype": "Main Dish",
        "mark": "red",
        "mealtype": null
        }


    ]


    
}`;
var userdata = JSON.parse(json);
var user1_name = userdata["recipes"][0]["title"];
var user2_name = userdata["recipes"][0]["description"];
var user3_name=""
for(var j=0;j<userdata["recipes"][0]["image"].length;j++){
    user3_name=userdata["recipes"][0]["image"][j]["url"];
    document.getElementById('output3').src=user3_name;
}
document.getElementById('output1').innerHTML=user1_name;
document.getElementById('output2').innerHTML=user2_name;

var obj1="";
for(var i=0;i<userdata["recipes"][0]["ingredientdetails"].length;i++){
    obj1=obj1+userdata["recipes"][0]["ingredientdetails"][i]["quantity"]+", "+userdata["recipes"][0]["ingredientdetails"][i]["ingredient"]["$oid"]+", "+userdata["recipes"][0]["ingredientdetails"][i]["directions"]+"<br>";
}
document.getElementById('output4').innerHTML=obj1;
var user4_name = userdata["recipes"][0]["timetocook"]["hh"] + " hours " + userdata["recipes"][0]["timetocook"]["mm"]+ " minutes ";
document.getElementById('output5').innerHTML=user4_name;
var user5_name = userdata["recipes"][0]["instructions"];
document.getElementById('output6').innerHTML=user5_name;
var user6_name = userdata["recipes"][0]["cuisine"];
document.getElementById('output7').innerHTML=user6_name;
var user7_name = userdata["recipes"][0]["dishtype"];
document.getElementById('output8').innerHTML=user7_name;
var user8_name = userdata["recipes"][0]["mark"];
document.getElementById('output9').innerHTML=user8_name;
var user9_name = userdata["recipes"][0]["mealtype"];
document.getElementById('output10').innerHTML=user9_name;
