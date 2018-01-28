var bn = [
    "Sahit",
    "Arti",
    "Goni",
    "Adnan",
    "Enis",
    "Lumi",
    "Lumbardh",
    "Adnan",
    "Faruk",
    "Blend",
    "Bujar",
    "Burim",
    "Gent",
    "Astrit",
    "Altin",
    "Valon",
    "Valmir",
    "Besnik",
    "Trim",
    "Lindon",
    "Lindor",
    "Genc",
    "Diar",
    "Egzon",
    "Besart",
    "Florent",
    "Yll",
    "Shkelzen",
    "Mehmet",
    "Muhamed",
    "Hamdi",
    "Naim",
    "Bekim",
    "Ruzhdi",
    "Orhan",
    "Leotrim",
    "Petrit",
    "Labinot",
    "Albion",
    "Albin",
    "Hashim",
    "Ramush",
    "Shpat",
    "Isa",
    "Ibrahim",
    "Emir",
    "Adrian",
    "Adriatik",
    "Drin",
    "Argjent",
    "Valdrin",
    "Valton",
    "Drilon",
    "Jeton",
    "Jetmir",
    "Njazi",
    "Darsej",
    "Shpetim",
    "Agon",
    "Agron",
    "Ardian",
    "Kushtrim",
    "Kujtim",
    "Fitim",
    "Adem",
    "Krenar",
    "Premtim",
    "Fatbardh",
    "Bardh",
    "Jon",
    "Eris",
    "Dren",
    "Alban",
    "Ilir",
    "Diellon",
    "Bleron",
    "Besjan",
    "Besfort",
    "Ermir",
    "Luan",
    "Leka",
    "Besian",
    "Oso",
    "Olti",
    "Tigran",
    "Besim",
    "Fehmi",
    "Hyzdri",
    "Idriz",
    "Selatin",
    "Granit",
    ];
var gn = [
    "Nita",
    "Elita",
    "Sahide",
    "Ajana",
    "Drita",
    "Ariana",
    "Fjona",
    "Fjolla",
    "Diellza",
    "Anila",
    "Tina",
    "Dorentina",
    "Lendita",
    "Lendina",
    "Shpresa",
    "Agnesa",
    "Donika",
    "Festa",
    "Denisa",
    "Hana",
    "Flaka",
    "Aurora",
    "Ftesa",
    "Bleona",
    "Albina",
    "Fitore",
    "Dilara",
    "Elsa",
    "Rina",
    "Beneta",
    "Elona",
    "Eriona",
    "Dafina",
    "Adelina",
    "Era",
    "Erza",
    "Sofia",
    "Zana",
    "Mrika",
    "Rita",
    "Merita",
    "Afertida",
    "Nazife",
    "Valbone",
    "Diona",
    "Ationa",
    "Suzana",
    "Liza",
    "Eliona",
    "Arbresha",
    "Ana",
    "Miranda",
    "Mimoza",
    "Jeta",
    "Aulona",
    "Yllka",
    "Yllza",
    "Melisa",
    "Suela",
    "Englantina",
    "Margarita",
    "Drilona",
    "Genita",
    "Gentiana",
    "Arta",
    "Renea",
    "Enea",
    "Elisa",
    "Ariona",
    "Edita",
    "Diella",
    "Arbenita",
    "Dea",
    "Adea",
    "Megi",
    "Antigona",
    "Blerina",
    "Bukurije",
    "Qendresa",
    "Flandra",
    "Flutra",
    "Lira",
    "Elira",
    "Ardita",
    "Nazmie",
    "Shehide",
    "Fakete",
    "Valmire",
    "Medina",
    "Arnisa",
    "Bonita",
    ];
var selectedNames = [];
var clicked;
var random;
var selectedNames2 = [];

function boys(){
    clicked = "boys";
}
function girls(){
    clicked = "girls";
}

function randomN (){
    if (bn.length != selectedNames.length){                         //IFFFI I PAR
    //var x = document.createElement("LI");
    if (clicked == "boys"){
        random = Math.floor(Math.random()*bn.length);
        var empty =(bn[random]);
        selectedNames.push(empty);
        console.log(selectedNames);
        for (var i = 0; i < selectedNames.length; i++){
            if (empty == selectedNames[i - 1] ){
                //duplicate me mujt me hek krejt qe mos mu dok as n HTML
        empty = "duplicate";
                break;
       }
    }





if (empty == "duplicate"){
    randomN();
}
else{
//var t = document.createTextNode(empty);
//x.appendChild(t);
document.getElementById("myList").innerHTML = empty ;
}//y.appendChild(x);
//}
    }
}
else if (bn.length == selectedNames.length){
        document.getElementById("myList").innerHTML = "No boy names left";
}
                                                                    //IFFFI I PAR MSHELET









    if (gn.length != selectedNames2.length){                        //IFFFI I dyt
    if (clicked == "girls"){
        random = Math.floor(Math.random()*gn.length);
        var empty =(gn[random]);
        selectedNames2.push(empty);
        console.log(selectedNames2);
        for (var i = 0; i < selectedNames2.length; i++){
            if (empty == selectedNames2[i - 1] ){
        empty = "duplicate";
                break;

            }

        }





if (empty == "duplicate"){
    randomN();
}

else{
document.getElementById("myList").innerHTML = empty ;
}


    }

}



    else if (gn.length == selectedNames2.length){
        document.getElementById("myList").innerHTML = "No girl names left";
}                                                           //IFFI I DYT





if (bn.length == selectedNames.length && (girls == "clicked")){
    randomN();

}



if (gn.length == selectedNames2.length && (boys == "clicked")){
    randomN();

}


}
// i funksionit





