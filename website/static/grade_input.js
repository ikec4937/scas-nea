function getSelectBoardName() {
    let selectValue = document.getElementById("boardname").value;
}

function getSelectCourseType() {
    let selectValue = document.getElementById("coursetype").value;
    changeGradeList(selectValue);
}

function changeGradeList(selectValue) {
    let html = "";
    html += "<option value=\"not_selected\" selected>Select a grade</option>";
    html += "<option value=\"pending\" >Pending</option>";
    
    switch(selectValue){
        case "GCSE":
            let gcseGrades = ["U", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
            
            for(let i = 0; i < gcseGrades.length; i++){
                html += "<option value=\""+gcseGrades[i]+"\">"+gcseGrades[i]+"</option>";
            }

            document.getElementById("grade_score").innerHTML=html;

        break;

        case "BTEC":
            let btecGrades = ["Merit", "Distinction", "Pass"];

            for(let i = 0; i < btecGrades.length; i++){
                html += "<option value=\""+btecGrades[i]+"\">"+btecGrades[i]+"</option>";
            }

            document.getElementById("grade_score").innerHTML=html;
        
        break;
            
        case "iGCSE":
            let iGcseGrades = ["U", "P1", "M1", "P2", "M2", "D1", "D2", "2*"];

            for(let i = 0; i < iGcseGrades.length; i++){
                html += "<option value=\""+iGcseGrades[i]+"\">"+iGcseGrades[i]+"</option>";
            }

            document.getElementById("grade_score").innerHTML=html;
        
        break;

        case "CamNat":
            let camNatGrades = ["U", "P1", "M1", "P2", "M2", "D1", "D2", "2*"];

            for(let i = 0; i < camNatGrades.length; i++){
                html += "<option value=\""+camNatGrades[i]+"\">"+camNatGrades[i]+"</option>";
            }

            document.getElementById("grade_score").innerHTML=html;
        
        break;

        case "Other":
            let defaultGrades = ["U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Merit", "Distinction", "Pass"];
            
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