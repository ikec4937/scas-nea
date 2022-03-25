function getSelectBoardName() {
    let selectValue = document.getElementById("boardname").value;
}

function getSelectCourseType() {
    let selectValue = document.getElementById("coursetype").value;
    changeGradeList(coursetype);
}

function changeGradeList(coursetype) {
    let html = "";
    html += "<option value=\"not_selected\" selected>Select a grade</option>"
    html += "<option value=\"pending\" >Pending</option>"
    
    switch(coursetype){
        case "GCSE":
            let gcseGrades = ["U", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
            
            for(let i = 0; i < gcseGrades.length; i++){
                html += "<option value=\""+gcseGrades[i]+"\">"+gcseGrades[i]+"</option>"
                //<option value="pending" >Pending</option>
            }

        break;

        case "BTEC":
            let btecGrades = ["Merit", "Distinction", "Pass"];

            for(let i = 0; i < btecGrades.length; i++){
                html += "<option value=\""+gcseGrades[i]+"\">"+btecGrades[i]+"</option>"
                //<option value="pending" >Pending</option>
            }
        
        break;

        case "CamNat":
            

    }

}