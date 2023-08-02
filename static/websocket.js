// var ws = new WebSocket( "ws://10.50.2.115:9000" );
// var ws = new WebSocket( "ws://192.168.1.139:9000" );
var ws = new WebSocket( "ws://" + document.location.hostname + ":9000");



function createText(textid,whichSectionId){
    var template = document.getElementById('text-template')
    var clon = template.content.cloneNode(true);
    var section = document.getElementById(whichSectionId)
    section.appendChild(clon)
    div = document.getElementById('text-div')
    div.id = textid
    div.innerText = incomingData.Data
}

function createImage(imageId,imagePath,whichSectionId){
    var template = document.getElementById('img-template')
    var clon = template.content.cloneNode(true);
    var section = document.getElementById(whichSectionId)
    section.appendChild(clon)
    img = document.getElementById('img')
    img.id = imageId
    img.src=imagePath
}

function connect(){
    // ws = new WebSocket( "ws://10.50.2.115:9000" );
    // ws = new WebSocket( "ws://192.168.1.139:9000" );
    ws = new WebSocket( "ws://" + document.location.hostname + ":9000");
    

    ws.onmessage = function(e)
    {
        incomingData = JSON.parse( e.data );
        console.log(incomingData)
        if ( incomingData.Command == "Clear" ) {
            document.getElementById("colourful-img-text").innerHTML = ""
            document.getElementById("colourful-img").src = ""
            document.getElementById("dataMatrix-text").innerHTML = ""
            document.getElementById("dataMatrix-img").src = ""
            document.getElementById("dataMatrix-data").innerHTML = ""
            document.getElementById("seriNo1-text").innerHTML = ""
            document.getElementById("seriNo1-result").innerHTML = ""
            document.getElementById("seriNo1-img").src = ""
            document.getElementById("seriNo2-text").innerHTML = ""
            document.getElementById("seriNo2-result").innerHTML = ""
            document.getElementById("seriNo2-img").src = ""
            document.getElementById("seriNo3-text").innerHTML = ""
            document.getElementById("seriNo3-result").innerHTML = ""
            document.getElementById("seriNo3-img").src = ""
            
        } else if (incomingData.Command == "colourful-img-text") {
            document.getElementById("colourful-img-text").innerHTML = "Renkli görüntü alınıyor..."
        } else if (incomingData.Command == "colourful-img") {
            document.getElementById("colourful-img").src = "../static/assets/test_1/1/colourful.png"
        } else if (incomingData.Command == "dataMatrix-text") {
            document.getElementById("dataMatrix-text").innerHTML = "Data matrix bulunuyor ..."
        } else if (incomingData.Command == "dataMatrix-img") {
            document.getElementById("dataMatrix-img").src = "../static/assets/test_1/1/dataMatrix.png"
        } else if (incomingData.Command == "dataMatrix-data") {
            if(incomingData.Data=="" || incomingData.Data==null){
                document.getElementById("dataMatrix-data").className = "false-data"
            } else {
                document.getElementById("dataMatrix-data").className = "true-data"
            }
            document.getElementById("dataMatrix-data").innerHTML = "Data matrix : " + incomingData.Data
        } else if (incomingData.Command == "seriNo1-text") {
            document.getElementById("seriNo1-text").innerHTML = "Altın üzerindeki 1. Seri numarası bulunuyor..."
        } else if (incomingData.Command == "seriNo1-result") {
            document.getElementById("seriNo1-result").innerHTML = "Bulunan seri no : " + incomingData.Data
        }




        // if (incomingData.Command == "Infrared Camera") {
        //     if (incomingData.Data == "Opened"){
        //         document.getElementById("ir-camera-icon").style.backgroundColor = "rgb(81, 220, 111)"
        //     }
        //     else if (incomingData.Data == "Closed"){
        //         document.getElementById("ir-camera-icon").style.backgroundColor = "rgb(255, 68, 68)"
        //     }
        // }
        // else if (incomingData.Command == "Colourful Camera"){
        //     if (incomingData.Data == "Opened"){
        //         document.getElementById("colourful-camera-icon").style.backgroundColor = "rgb(81, 220, 111)"
        //     }
        //     else if (incomingData.Data == "Closed"){
        //         document.getElementById("colourful-camera-icon").style.backgroundColor = "rgb(255, 68, 68)"
        //     }
        // }
        // else if (incomingData.Command == "Modbus"){
        //     if (incomingData.Data == "Opened"){
        //         document.getElementById("usb-icon").style.backgroundColor = "rgb(81, 220, 111)"
        //     }
        //     else if (incomingData.Data == "Closed"){
        //         document.getElementById("usb-icon").style.backgroundColor = "rgb(255, 68, 68)"
        //     }
        // }
        // else if (incomingData.Command == "Start"){
        //     document.getElementById("request_date").value = incomingData.Data.request_date
        //     document.getElementById("planned_printing_date").value = incomingData.Data.planned_printing_date
        //     document.getElementById("sample_report_serial_number").value = incomingData.Data.sample_report_serial_number
        //     document.getElementById("sample_location").value = incomingData.Data.sample_location
        //     document.getElementById("startbutton").style.backgroundColor = "red"
        //     document.getElementById("startbutton").disabled = true
        // }
        // // ******************** 1. aşama *********************************
        // else if (incomingData.Command == "white-led-text-1"){
        //     //sayfayı temizle
        //     document.getElementById("section-1").innerHTML=""
        //     document.getElementById("section-2").innerHTML=""
        //     document.getElementById("section-3").innerHTML=""
        //     document.getElementById("section-4").innerHTML=""
        //     createText("white-led-text-1","section-1")
        // }
        // else if (incomingData.Command == "colourful-img-1"){
        //     createImage('colourful-img-1',"../static/assets/test_1/1/colourful.png","section-1")
        // }
        // else if (incomingData.Command == "colourful-text-1"){
        //     createText("colourful-text-1","section-1")
        
        // }
        // else if (incomingData.Command == "green-text-1"){
        //     createText("green-text-1","section-1")
        // }
        // else if (incomingData.Command == "green-text-result-1"){
        //     createText("green-text-result-1","section-1")
        // }
        // else if (incomingData.Command == "blue-text-1"){
        //     createText("blue-text-1","section-1")
        // }
        // else if (incomingData.Command == "ir-camera-text-1"){
        //     createText("ir-camera-text-1","section-1")
        // }
        // else if (incomingData.Command == "original-img-1"){
        //     createImage("original-img-1","../static/assets/test_1/1/original_image.png","section-1")
        // }
        // else if (incomingData.Command ==  "original-text-1"){
        //     createText("original-text-1","section-1")
        // }
        // else if (incomingData.Command ==  "barcode-text-1"){
        //     createText("barcode-text-1","section-1")
        // }
        // else if (incomingData.Command == "barcode-img-1"){
        //     createImage("barcode-img-1","../static/assets/test_1/1/barcode_image.png","section-1")
        // }
        // else if (incomingData.Command ==  "barcode-text-result-1"){
        //     createText("barcode-text-result-1","section-1")
        // }
        // else if (incomingData.Command ==  "logo-verification-text-1"){
        //     createText("logo-verification-text-1","section-1")
        // }
        // else if (incomingData.Command == "logo-img-1"){
        //     createImage("logo-img-1","../static/assets/test_1/1/logo.png","section-1")
        // }
        // else if (incomingData.Command == "logo-text-result-1"){
        //     createText("logo-text-result-1","section-1")
        // }
        // else if (incomingData.Command ==  "area-text-1"){
        //     createText("area-text-1","section-1")
        // }
        // else if (incomingData.Command ==  "ir-led-text-1"){
        //     createText("ir-led-text-1","section-2")
        // }
        // else if (incomingData.Command ==  "ir-camera-ir-img-text-1"){
        //     createText("ir-camera-ir-img-text-1","section-2")
        // }
        // else if (incomingData.Command ==  "ir-img-1"){
        //     createImage("ir-img-1","../static/assets/test_1/1/verify_no_ink.png","section-2")
        // }
        // else if (incomingData.Command ==  "ir-result-1"){
        //     createText("ir-result-1","section-2")
        // }
        // else if (incomingData.Command ==  "sensor-text-2"){
        //     createText("sensor-text-2","section-3")
        // }
        // else if (incomingData.Command ==  "sensor-result-2"){
        //     createText("sensor-result-2","section-3")
        // }
        // else if (incomingData.Command ==  "intensities-img-2"){
        //     createImage("intensities-img-2","../static/assets/test_1/2/intensities.png","section-3")
        // }
        // else if (incomingData.Command ==  "rates-img-2"){
        //     createImage("rates-img-2","../static/assets/test_1/2/rates.png","section-3")
        //     document.getElementById("popup").classList.add("open");
        // }
        // // ******************** 2. aşama *********************************
        // else if (incomingData.Command == "white-led-text-2"){
        //     document.getElementById("popup").classList.remove("open");
        //     createText("white-led-text-2","section-3")
        // }
        // else if (incomingData.Command == "colourful-img-2"){
        //     createImage('colourful-img-2',"../static/assets/test_1/2/colourful.png","section-3")
        // }
        // else if (incomingData.Command == "colourful-text-2"){
        //     createText("colourful-text-2","section-3")
        // }
        // else if (incomingData.Command == "green-text-2"){
        //     createText("green-text-2","section-3")
        // }
        // else if (incomingData.Command == "green-text-result-2"){
        //     createText("green-text-result-2","section-3")
        // }
        // else if (incomingData.Command == "blue-text-2"){
        //     createText("blue-text-2","section-3")
        // }
        // else if (incomingData.Command == "ir-camera-text-2"){
        //     createText("ir-camera-text-2","section-3")
        // }
        // else if (incomingData.Command == "original-img-2"){
        //     createImage("original-img-2","../static/assets/test_1/2/original_image.png","section-3")
        // }
        // else if (incomingData.Command ==  "original-text-2"){
        //     createText("original-text-2","section-3")
        // }
        // else if (incomingData.Command ==  "barcode-text-2"){
        //     createText("barcode-text-2","section-4")
        // }
        // else if (incomingData.Command == "barcode-img-2"){
        //     createImage("barcode-img-2","../static/assets/test_1/2/barcode_image.png","section-4")
        // }
        // else if (incomingData.Command ==  "barcode-text-result-2"){
        //     createText("barcode-text-result-2","section-4")
        // }
        // else if (incomingData.Command ==  "logo-verification-text-2"){
        //     createText("logo-verification-text-2","section-4")
        // }
        // else if (incomingData.Command == "logo-img-2"){
        //     createImage("logo-img-2","../static/assets/test_1/2/logo.png","section-4")
        // }
        // else if (incomingData.Command ==  "area-text-2"){
        //     createText("area-text-2","section-4")
        // }
        // else if (incomingData.Command ==  "logo-text-result-2"){
        //     createText("logo-text-result-2","section-4")
        // }
        // else if (incomingData.Command ==  "ir-led-text-2"){
        //     createText("ir-led-text-2","section-4")
        // }
        // else if (incomingData.Command ==  "ir-camera-ir-img-text-2"){
        //     createText("ir-camera-ir-img-text-2","section-4")
        // }
        // else if (incomingData.Command ==  "ir-img-2"){
        //     createImage("ir-img-2","../static/assets/test_1/2/verify_no_ink.png","section-4")
        // }
        // else if (incomingData.Command ==  "ir-result-2"){
        //     createText("ir-result-2","section-4")
        // }
        // else if (incomingData.Command ==  "sensor-text-1"){
        //     createText("sensor-text-1","section-2")
        // }
        // else if (incomingData.Command ==  "sensor-result-1"){
        //     createText("sensor-result-1","section-2")
        // }
        // else if (incomingData.Command ==  "intensities-img-1"){
        //     createImage("intensities-img-1","../static/assets/test_1/1/intensities.png","section-2")
        // }
        // else if (incomingData.Command ==  "rates-img-1"){
        //     createImage("rates-img-1","../static/assets/test_1/1/rates.png","section-2")
        //     document.getElementById("popupfinished").classList.add("open");
        //     document.getElementById("startbutton").style.backgroundColor = ""
        //     document.getElementById("startbutton").disabled = false
        // }
        


        



        


        


        

        




    }

    ws.onopen = function(e)
    {
        console.log( "ws open" );
    }

    ws.onclose = function(e)
    {
        console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
        setTimeout(function() {
            connect();
          }, 1000);
    
    }

    ws.onerror = function( e )
    {
        console.log( "ws error" );
    };


}

connect();
