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
                ret += '<td>' + element[3] + '</td></tr>';
            });
            $("#msgTable").append(ret);
        }
    });
}

$( document ).ready(function() {
    //console.log('Test');
    getData();
});