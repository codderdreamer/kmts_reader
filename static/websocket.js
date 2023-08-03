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
            document.getElementById("dataMatrix-result").innerHTML = ""
            document.getElementById("seriNo1-text").innerHTML = ""
            document.getElementById("seriNo1-result").innerHTML = ""
            document.getElementById("seriNo1-img").src = ""
            document.getElementById("seriNo2-text").innerHTML = ""
            document.getElementById("seriNo2-result").innerHTML = ""
            document.getElementById("seriNo2-img").src = ""
            document.getElementById("seriNo3-text").innerHTML = ""
            document.getElementById("seriNo3-result").innerHTML = ""
            document.getElementById("seriNo3-img").src = ""
            document.getElementById("digimark-result").innerHTML = ""
            document.getElementById("digimark-img").src = ""
            document.getElementById("digimark-text").innerHTML = ""
            document.getElementById("ink-text").innerHTML = ""
            document.getElementById("dataMatrix-result").className = ""
            document.getElementById("seriNo1-result").className = ""
            document.getElementById("seriNo2-result").className = ""
            document.getElementById("seriNo3-result").className = ""
            document.getElementById("digimark-result").className = ""
            document.getElementById("ink-result").innerHTML = ""
            document.getElementById(" result-img").src = ""
           

        } else if (incomingData.Command == "colourful-img-text") {
            document.getElementById("colourful-img-text").innerHTML = "Renkli görüntü alınıyor..."
        } else if (incomingData.Command == "colourful-img") {
            document.getElementById("colourful-img").src = "../static/assets/test_1/1/colourful.png?" + Math.random();
        } else if (incomingData.Command == "dataMatrix-text") {
            document.getElementById("dataMatrix-text").innerHTML = "Data matrix bulunuyor ..."
        } else if (incomingData.Command == "dataMatrix-img") {
            document.getElementById("dataMatrix-img").src = "../static/assets/test_1/1/dataMatrix.png?" + Math.random();
        } else if (incomingData.Command == "dataMatrix-result") {
            if(incomingData.Data=="" || incomingData.Data==null){
                document.getElementById("dataMatrix-result").className = "false-data"
            } else {
                document.getElementById("dataMatrix-result").className = "true-data"
            }
            document.getElementById("dataMatrix-result").innerHTML = "Data matrix : " + incomingData.Data
        } else if (incomingData.Command == "seriNo1-text") {
            document.getElementById("seriNo1-text").innerHTML = "Altın üzerindeki 1. Seri numarası bulunuyor..."
        } else if (incomingData.Command == "seriNo1-result") {
            if(incomingData.Data=="" || incomingData.Data==null){
                document.getElementById("seriNo1-result").className = "false-data"
            } else {
                document.getElementById("seriNo1-result").className = "true-data"
            }
            document.getElementById("seriNo1-result").innerHTML = "Bulunan seri no : " + incomingData.Data
        } else if (incomingData.Command == "seriNo1-img") {
            document.getElementById("seriNo1-img").src = "../static/assets/test_1/1/seriNo1.png?" + Math.random();
        } else if (incomingData.Command == "seriNo2-text") {
            document.getElementById("seriNo2-text").innerHTML = "Altın üzerindeki 2. Seri numarası bulunuyor..."
        } else if (incomingData.Command == "seriNo2-result") {
            if(incomingData.Data=="" || incomingData.Data==null){
                document.getElementById("seriNo2-result").className = "false-data"
            } else {
                document.getElementById("seriNo2-result").className = "true-data"
            }
            document.getElementById("seriNo2-result").innerHTML = "Bulunan seri no : " + incomingData.Data
        } else if (incomingData.Command == "seriNo2-img") {
            document.getElementById("seriNo2-img").src = "../static/assets/test_1/1/seriNo2.png?" + Math.random();
        } else if (incomingData.Command == "seriNo3-text") {
            document.getElementById("seriNo3-text").innerHTML = "Altın üzerindeki 3. Seri numarası bulunuyor..."
        } else if (incomingData.Command == "seriNo3-result") {
            if(incomingData.Data=="" || incomingData.Data==null){
                document.getElementById("seriNo3-result").className = "false-data"
            } else {
                document.getElementById("seriNo3-result").className = "true-data"
            }
            document.getElementById("seriNo3-result").innerHTML = "Bulunan seri no : " + incomingData.Data
        } else if (incomingData.Command == "seriNo3-img") {
            document.getElementById("seriNo3-img").src = "../static/assets/test_1/1/seriNo3.png?" + Math.random();
        } else if (incomingData.Command == "digimark-text") {
            document.getElementById("digimark-text").innerHTML = "Altın üzerindeki Digimark kodu bulunuyor..."
        } else if (incomingData.Command == "digimark-img") {
            document.getElementById("digimark-img").src = "../static/assets/test_1/1/digimark.png?" + Math.random();
            document.getElementById("digimark-result").innerHTML = "Bulunan digimark kodu : " + "ATLASTEK123"
            document.getElementById("digimark-result").className = "true-data"
        } else if (incomingData.Command == "ink-text") {
            document.getElementById("ink-text").innerHTML = "Altın Üzerindeki Mürekkep değerlerine bakılıyor..."
        } else if (incomingData.Command == "ink-result") {
            document.getElementById("ink-result").innerHTML = incomingData.Data
        } else if (incomingData.Command == "result-img") {
            document.getElementById("result-img").src = "../static/assets/test_1/1/result.png?" + Math.random();
        }

        
        

        
        

        


        



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
