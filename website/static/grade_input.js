//I'm using camelcase for Javascript because that's generally how it is for the language.
function getSelectQualifType() { //For qualification (I didn't know tha name at the time)
    let selectValue = document.getElementById("qualif").value; //As the course type is selected,
    changeGradeList(selectValue); //The below function is called
}

function changeGradeList(selectValue) {
    let html = ""; //empty Html empty string to replace the html in mang_grades.html.
    html += "<option value=\"not_selected\" selected>Select a grade</option>";
    html += "<option value=\"pending\" >Pending</option>";
    //By default, "Select a grade" and "Pending" are pushed into the html file.
    
    //Grades are declared.
    let gcseGrades = ["U", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    let btecGrades = ["Merit", "Distinction", "Pass"];
    let iGcseGrades = ["U", "P1", "M1", "P2", "M2", "D1", "D2", "2*"];
    let camNatGrades = ["U", "P1", "M1", "P2", "M2", "D1", "D2", "2*"];
    let defaultGrades = ["U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Merit", "Distinction", "Pass"];

    switch(selectValue){
        case "GCSE": //If selectValue is GCSE
            for(let i = 0; i < gcseGrades.length; i++){
                html += "<option value=\""+gcseGrades[i]+"\">"+gcseGrades[i]+"</option>";
            } //Each GCSE grade is pushed into html string text in the html syntax

            document.getElementById("grade_score").innerHTML=html;
            //Grabs the contents of whatever belongs to the element "grade_score" and replaces it all with the html string value

        break;

        case "BTEC": //BTEC

            for(let i = 0; i < btecGrades.length; i++){
                html += "<option value=\""+btecGrades[i]+"\">"+btecGrades[i]+"</option>";
            } //It's the same for every type of course

            document.getElementById("grade_score").innerHTML=html;
        
        break;
            
        case "iGCSE": //International GCSEs

            for(let i = 0; i < iGcseGrades.length; i++){
                html += "<option value=\""+iGcseGrades[i]+"\">"+iGcseGrades[i]+"</option>";
            }

            document.getElementById("grade_score").innerHTML=html;
        
        break;

        case "CamNat": //Cambridge Nationals

            for(let i = 0; i < camNatGrades.length; i++){
                html += "<option value=\""+camNatGrades[i]+"\">"+camNatGrades[i]+"</option>";
            }

            document.getElementById("grade_score").innerHTML=html;
        
        break;

        case "Other": //For exams that aren't GCSEs.
            
            for(let i = 0; i < defaultGrades.length; i++){
                html += "<option value=\""+defaultGrades[i]+"\">"+defaultGrades[i]+"</option>";
            }
            
            document.getElementById("grade_score").innerHTML=html;

        break;
        
        /*
        default:
            let defaultGrades = ["U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Merit", "Distinction", "Pass"];
            
            for(let i = 0; i < defaultGrades.length; i++){
                html += "<option value=\""+defaultGrades[i]+"\">"+defaultGrades[i]+"</option>";
            }
            
            document.getElementById("grade_score").innerHTML=html;
        */
    }

}

/*

function changeSubjects() {

}

 //All the below code is for later
let gcseSubjects = ["English Literature", "English Language", 
"Maths", "Physics", "Chemistry", "Biology", "Combined Science",
"French", "German", "Italian", "Spanish", "Latin",
"History", "Geography", "Religious Studies", 
"Art", "Fine art", "Photography", "Dance", "Music"];

let btecSubjects = ["Food Technology", "Health and Social Care"];

let iGcseSubjects = ["English Literature (UK)", "English Literature (US)", "English as an additional language", "English as a second language", 
"Maths", "Additional Maths", "Math (US)", "Physics", "Chemistry", "Biology", "Combined Science", "Co-Ordinated Science",
"French", "German", "Italian", "Spanish", "Latin",
"History", "Geography", "Religious Studies", 
"Art", "Fine art", "Photography", "Dance", "Music"];

let camNameSubjects = [""];*/