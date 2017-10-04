$(document).on("click", function(e){
    if($(e.target).is("#loan_btn")){
      $("#loan_div").toggle();
    }
});

$(document).on("click", function(e){
    if($(e.target).is("#return_btn")){
      $("#return_div").toggle();
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
    success: function(data){
        var row = data.data;
        $('#my_table').append('<tr><td>'+row[0]+'</td>' +
               '<td>'+row[1]+'</td>' +
               '<td>'+row[2]+'</td>' +
               '<td>'+row[3]+'</td>' +
               '<td>'+row[4]+'</td></tr>');
    },
    error: function(error){
        console.log(error);
    }
  });
};

function return_post() {
  $.ajax({
    url: '/return',
    dataType: 'json',
    type: 'post',
    contentType: 'application/json',
    data: JSON.stringify({"object": $('#return_id').val(), "name": $('#return_object').val()}),
    processData: false,
    success: function(data){
        var row = data.data;
        console.log(row)
    },
    error: function(error){
        console.log(error);
    }
  });
};

