

// function start(ws){
//     console.log("Start")
//     document.getElementById("section-1").innerHTML=""
//     document.getElementById("section-2").innerHTML=""
//     document.getElementById("section-3").innerHTML=""
//     document.getElementById("section-4").innerHTML=""
    
//     var request_date = document.getElementById("request_date").value
//     var planned_printing_date = document.getElementById("planned_printing_date").value
//     var sample_report_serial_number = document.getElementById("sample_report_serial_number").value
//     var sample_location = document.getElementById("sample_location").value
//     var type = document.getElementById("type").value
    

//     var start = 
//     {
//         Command: "Start",
//         Data:
//         {
//             "request_date" : request_date,
//             "planned_printing_date" : planned_printing_date,
//             "sample_report_serial_number" : sample_report_serial_number,
//             "sample_location": sample_location,
//             "type" : type
//         }
        
//     }
//     ws.send( JSON.stringify( start ) );
//     document.getElementById("startbutton").style.backgroundColor = "red"
    
//     // var test = document.getElementById('test')
//     // var clon = test.content.cloneNode(true);
//     // var section = document.getElementById('section-1')
//     // section.appendChild(clon)

// }

// function ok(){
//     document.getElementById("popup").classList.remove("open");
//     document.getElementById("continuepopup").classList.add("open");
// }

// function continueProcess(){
//     document.getElementById("continuepopup").classList.remove("open");
//     console.log("Continue")
//     var start = 
//     {
//         Command: "Continue",
//         Data:
//         {
            
//         }
//     }
//     ws.send( JSON.stringify( start ) );
// }

// function finished(){
//     document.getElementById("popupfinished").classList.remove("open");
// }

// function date_time_update() {
//     var now = new Date()
    
//     var day = now.getDate().toString()
//     var month = (now.getMonth() + 1).toString()
//     var year = now.getFullYear().toString()

//     if (day.length==1) {
//         day = '0' + day
//     }
//     if (month.length==1) {
//         month = '0' + month
//     }

//     datetime = day + '/' + month + '/' + year
//     document.getElementById("date-time").textContent = datetime
    
// }
// setInterval(date_time_update, 1000);

// function fullscreen(element){
//     console.log(element)
// }
