//This is to provide routes to get data from the database and send more data in
function getData() {
    //console.log('Testing');
    $.post('/data', function(data, status) {
        //console.log(status);
        //console.log(data);

        if (data) {
            $("#msgTable").empty();
            let ret = '';
            data = JSON.parse(data);
            data.forEach(element => {
                if (element[2] == "0") {
                    ret += '<tr class="danger">';
                }
                else {
                    ret += '<tr>';
                }
                ret += '<td>' + element[0] + '</td>';
                ret += '<td>' + element[1] + '</td>';
                ret += '<td>' + element[3] + '</td>';
                ret += '<td><button onclick="updateMsg(' + element[0] + ',' + (element[2] == "0"? "1" : "0") + ')" class="btn btn-info">Toggle</button></td>';
                ret += '<td><button onclick="deleteMsg(' + element[0] + ')" class="btn btn-danger">Delete</button>';
                ret += '</tr>';
            });
            $("#msgTable").append(ret);
        }
    });
}

$( document ).ready(function() {
    //console.log('Test');
    getData();
});

function testTextClassification() {
    let msg = $("#msg").val();
    $.post("/classifymessage", {msg: msg}, function(data) {
        console.log("data",data, (data["output"] == "ham").toString());
        //data = JSON.parse(data);
        //console.log("data",data);
        $('#msgResult').text(data["output"] + " " + data["pred"] + "%");
        
        $("#typestr").val(data["output"] == "ham"? "1" : "0");
    });
}

function insertToDB() {
    let msg = $("#msg").val();
    let typestr = $("#typestr").val();
    $.post("/addtodb", {msg: msg, typestr: typestr}, function(data){
        getData();
    });
}

function retrainModel() {
    $.post("/retrainmodel", function(data){
        $('#lossStat').text(data.loss);
        $('#accStat').text(data.accuracy);
    });
}

function updateMsg(msgID, typeStr) {
    $.post("/updatemsg", {msgid: msgID, typestr: typeStr}, function(data) {
        getData();
    });
}

function deleteMsg(msgID) {
    $.post("/deletemsg", {msgid: msgID}, function(data) {
        getData()
    });
}