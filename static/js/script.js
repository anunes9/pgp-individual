$(document).on("click", function(e){
    if($(e.target).is("#loan_btn")){
      $("#loan_div").toggle();
      $('#loan_object').val('');
      $('#loan_name').val('');
    }
});

$(document).on("click", function(e){
    if($(e.target).is("#return_btn")){
      $("#return_div").toggle();
      $('#return_id').val('');
    }
});

function loan_post() {
  $.ajax({
    url: '/loan',
    dataType: 'json',
    type: 'post',
    contentType: 'application/json',
    data: JSON.stringify({"object": $('#loan_object').val(), "name": $('#loan_name').val()}),
    processData: false,
    success: function(data) {
        if (data.status == 'OK') {
            var row = data.data;
            $('#my_table').append('<tr><td>' + row[0] + '</td>' +
                '<td>' + row[1] + '</td>' +
                '<td>' + row[2] + '</td>' +
                '<td>' + row[3] + '</td>' +
                '<td>' + row[4] + '</td></tr>');
            $("#loan_div").toggle();
            $('#loan_object').val('');
            $('#loan_name').val('');
            alert("Object added!")
        } else {
            console.log(data.status)
        }
    }
  });
};

function return_post() {
    var id = $('#return_id').val();
  $.ajax({
    url: '/return_loan',
    dataType: 'json',
    type: 'post',
    contentType: 'application/json',
    data: JSON.stringify({"id": id}),
    processData: false,
    success: function(data) {
        if (data.status == 'OK') {
            var row = data.data;
            $('tr:eq(' + id + ') td:eq(4)', my_table).html("Returned");
            $("#return_div").toggle();
            $('#return_id').val('');
            alert("Object returned!")
        } else {
            $("#return_div").toggle();
            $('#return_id').val('');
            alert("That object was already returned!")
        }
    }
  });
};

